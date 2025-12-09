import os
import sys

# Try to import required libraries
try:
    from googleapiclient.discovery import build
    from google import auth
except ImportError:
    print("Error: Missing required libraries.")
    print("Please install them using: pip install google-api-python-client google-auth")
    sys.exit(1)

def get_project_id():
    """Attempts to retrieve the Google Cloud Project ID."""
    # 1. Try environment variable
    project_id = os.environ.get("GCP_PROJECT_ID") or os.environ.get("GOOGLE_CLOUD_PROJECT")
    if project_id:
        return project_id
    
    # 2. Try to get from default credentials
    try:
        _, project_id = auth.default()
        if project_id:
            return project_id
    except Exception:
        pass

    return None

import argparse

def update_readme(content, start_marker, end_marker):
    """Updates the README.md file between specific markers."""
    readme_path = "README.md"
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            readme_content = f.read()
        
        start_pos = readme_content.find(start_marker)
        end_pos = readme_content.find(end_marker)
        
        if start_pos == -1 or end_pos == -1:
            print(f"Warning: Markers {start_marker} and {end_marker} not found in {readme_path}")
            return

        new_content = (
            readme_content[:start_pos + len(start_marker)]
            + "\n```text\n" + content + "\n```\n"
            + readme_content[end_pos:]
        )
        
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print(f"Successfully updated {readme_path}")
        
    except Exception as e:
        print(f"Error updating README: {e}")

def check_quota(project_id, update_readme_flag=False):
    """
    Fetches and displays the quota for the Generative Language API using the Service Usage API v1beta1.
    """
    print(f"Checking quotas for Project ID: {project_id}...")
    
    output_buffer = []
    
    def log(message):
        print(message)
        output_buffer.append(message)

    try:
        # Build the Service Usage API client
        # We need v1beta1 to access consumerQuotaMetrics nicely or we can use serviceusage v1
        # Let's try the 'serviceusage' API (v1beta1 often exposes more details for quotas)
        service = build('serviceusage', 'v1beta1')
        
        service_name = "generativelanguage.googleapis.com"
        parent = f"projects/{project_id}/services/{service_name}"

        # 1. Check State
        request = service.services().get(name=parent)
        response = request.execute()
        
        if response.get('state') != 'ENABLED':
            log(f"Service '{service_name}' is NOT ENABLED for this project.")
            return
            
        log(f"Service '{service_name}' is ENABLED. Fetching consumer quota metrics...")

        request = service.services().consumerQuotaMetrics().list(parent=parent)
        response = request.execute()
        
        metrics = response.get('metrics', [])
        
        limits_by_model = {}

        for metric in metrics:
            metric_full_name = metric.get('name', '')
            metric_id = metric_full_name.split('/')[-1] # e.g. "generate_content_free_tier_requests"

            # Filter for relevant generative metrics
            if not (("generate_content" in metric_id or "generate_requests" in metric_id) and
                    ("requests" in metric_id or "token_count" in metric_id or "tokens" in metric_id)):
                continue

            limit_type = ""
            if "per_day" in metric_id:
                limit_type = "Requests per Day"
            elif "token_count" in metric_id or "tokens" in metric_id:
                limit_type = "Tokens per Minute"
            elif "requests" in metric_id:
                limit_type = "Requests per Minute"
            else:
                continue # Should not happen with current filter

            for limit in metric.get('consumerQuotaLimits', []):
                for bucket in limit.get('quotaBuckets', []):
                    effective_limit = bucket.get('effectiveLimit', 'N/A')
                    dims = bucket.get('dimensions', {})
                    model_name = dims.get('model', 'Global')

                    if effective_limit == -1: # -1 often means unlimited
                        effective_limit = "Unlimited"
                    
                    if effective_limit == 'N/A':
                        continue # Skip entries with no effective limit

                    if model_name not in limits_by_model:
                        limits_by_model[model_name] = {}
                    
                    # Store the most restrictive (lowest) limit if multiple apply for a type
                    current_limit = limits_by_model[model_name].get(limit_type)
                    if current_limit is None or (isinstance(current_limit, (int, float)) and isinstance(effective_limit, (int, float)) and effective_limit < current_limit):
                        limits_by_model[model_name][limit_type] = effective_limit
                    elif isinstance(effective_limit, str) and effective_limit == "Unlimited" and current_limit != "Unlimited":
                        # "Unlimited" is always preferred over a number
                        limits_by_model[model_name][limit_type] = effective_limit
                    elif current_limit == "Unlimited" and isinstance(effective_limit, (int, float)):
                        # If current is unlimited, and new is a number, keep unlimited
                        pass # Do nothing
                    elif current_limit is None: # First entry
                         limits_by_model[model_name][limit_type] = effective_limit

        # Define the specific models we want to see in the table
        target_models = [
            "gemini-2.5-flash",
            "gemini-2.5-pro",
            "gemini-2.0-flash",
            "gemini-1.5-flash",
            "gemini-1.5-pro",
            "Global" # Global limits
        ]

        log(f"\n{'Model Name':<30} | {'RPM':<15} | {'RPD':<15} | {'TPM':<15}")
        log("-" * 85)

        # Sort: Target models first, then alphabetical for others if they contain "flash" or "pro"
        # But for "Summary Table Only" request, let's stick to the targets + major versions
        
        displayed_models = []
        
        # First pass: Get all models present in limits_by_model
        all_models = sorted(limits_by_model.keys())
        
        for model in all_models:
            # Filter: Show if it's in our target list OR looks like a main version (e.g. gemini-2.5-flash-001)
            is_target = model in target_models
            is_relevant_variant = any(x in model for x in ["gemini-2.5", "gemini-2.0", "gemini-1.5"]) and \
                                  not any(x in model for x in ["exp", "preview", "audio", "image", "tts", "robotics"])
            
            if is_target or is_relevant_variant:
                rpm = limits_by_model[model].get("Requests per Minute", "-")
                rpd = limits_by_model[model].get("Requests per Day", "-")
                tpm = limits_by_model[model].get("Tokens per Minute", "-")
                
                log(f"{model:<30} | {str(rpm):<15} | {str(rpd):<15} | {str(tpm):<15}")

        log("-" * 85)
        log("RPM = Requests Per Minute, RPD = Requests Per Day, TPM = Tokens Per Minute")
        log("'-' means no specific limit found (or unlimited if not explicitly set to -1).")

        if update_readme_flag:
             full_output = "\n".join(output_buffer)
             # Remove the initial "Checking quotas..." and "Service ENABLED" logs for cleaner README
             clean_output = "\n".join(output_buffer[2:]) 
             update_readme(clean_output, "<!-- START_QUOTA_OUTPUT -->", "<!-- END_QUOTA_OUTPUT -->")
                        
    except Exception as e:
        log(f"Error fetching quotas: {e}")
        log("\nTroubleshooting:")
        log("1. Ensure you have run 'gcloud auth application-default login'.")
        log("2. Ensure your account has 'Service Usage Consumer' role.")
        log("3. Ensure the Project ID is correct.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check Gemini API Quotas")
    parser.add_argument("--update-readme", action="store_true", help="Update the README.md file with the output")
    args = parser.parse_args()

    print("--- Gemini API Quota Checker (Discovery) ---")
    
    # Prerequisite Check
    proj_id = get_project_id()
    
    if not proj_id:
        print("Could not automatically determine Google Cloud Project ID.")
        print("Please set the 'GCP_PROJECT_ID' environment variable.")
        sys.exit(1)
        
    check_quota(proj_id, args.update_readme)