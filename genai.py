import os
import argparse
import datetime # Import datetime
from google import genai

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

        # Generate timestamp
        now = datetime.datetime.now()
        timestamp_str = now.strftime("產生時間: %Y-%m-%d %H:%M:%S") + " CST"


        new_content = (
            readme_content[:start_pos + len(start_marker)]
            + f"\n{timestamp_str}\n\n```text\n" + content + "\n```\n"
            + readme_content[end_pos:]
        )
        
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print(f"Successfully updated {readme_path}")
        
    except Exception as e:
        print(f"Error updating README: {e}")

# Retrieve API key from environment variable
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set")

client = genai.Client(api_key=api_key)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Basic GenAI Test")
    parser.add_argument("--update-readme", action="store_true", help="Update the README.md file with the output")
    args = parser.parse_args()
    
    output_buffer = []

    response1 = client.models.generate_content(
        model="gemini-2.5-flash", contents="Explain how AI works in a 100+ words in traditional chinese"
    )
    print(response1.text)
    output_buffer.append("--- AI Explanation ---\n" + response1.text)

    response2 = client.models.generate_content(
        model="gemini-2.5-flash", contents="provide python code how to know the quota of google genai api"
    )
    print(response2.text)
    output_buffer.append("\n--- Quota Code Example ---\n" + response2.text)
    
    if args.update_readme:
        full_output = "\n".join(output_buffer)
        update_readme(full_output, "<!-- START_GENAI_OUTPUT -->", "<!-- END_GENAI_OUTPUT -->")