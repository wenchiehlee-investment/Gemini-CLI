import os
from google import genai

# Retrieve API key from environment variable
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    print("Error: GOOGLE_API_KEY environment variable not set.")
    exit(1)

client = genai.Client(api_key=api_key)

try:
    # Attempt to list models
    # Common patterns in Google SDKs: client.models.list(), client.list_models()
    print("Fetching available models...")
    for model in client.models.list():
        print(f"Model Name: {model.name}")
        print(f"Display Name: {model.display_name}")
        print("-" * 20)

except Exception as e:
    print(f"An error occurred: {e}")
