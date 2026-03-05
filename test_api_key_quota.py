import os
from googleapiclient.discovery import build
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Use environment variables instead of hardcoded strings
api_key = os.environ.get("GEMINI_API_KEY")
project_id = os.environ.get("GCP_PROJECT_ID")

if not api_key:
    print("Error: GEMINI_API_KEY environment variable not set.")
    sys.exit(1)

if not project_id:
    print("Error: GCP_PROJECT_ID environment variable not set.")
    sys.exit(1)

try:
    print(f"Testing Service Usage API with API Key for project: {project_id}...")
    # developerKey allows using an API Key instead of default credentials for certain APIs
    service = build('serviceusage', 'v1beta1', developerKey=api_key)
    service_name = "generativelanguage.googleapis.com"
    parent = f"projects/{project_id}/services/{service_name}"
    
    print("1. Checking Service State...")
    request = service.services().get(name=parent)
    response = request.execute()
    print(f"State: {response.get('state')}")

    print("2. Checking Consumer Quota Metrics...")
    request = service.services().consumerQuotaMetrics().list(parent=parent)
    response = request.execute()
    metrics = response.get('metrics', [])
    print(f"Success! Found {len(metrics)} metrics.")
    
except Exception as e:
    print(f"Failed: {e}")
