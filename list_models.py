from google import genai

client = genai.Client(api_key="AIzaSyA-GZvh_EYBPb6A5970Ka4ypEfJsdkGzDc")

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
