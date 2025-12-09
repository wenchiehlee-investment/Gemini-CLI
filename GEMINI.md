# Gemini-CLI Project Context

## Project Overview
This project is a Python-based workspace for interacting with Google's Gemini API. It has evolved from simple text generation to include utility scripts for model exploration, practical tasks like web scraping/summarization, and quota management.

## Key Files
- **`genai.py`**: Basic proof-of-concept script. Authenticates and generates text/code using `gemini-2.5-flash`.
- **`list_models.py`**: Utility script to query the API and print a list of all available models (e.g., Flash, Pro, Experimental variants).
- **`summarize_url.py`**: A more advanced script that:
    1.  Fetches HTML content from a URL using `requests`.
    2.  Cleans and extracts text using `BeautifulSoup`.
    3.  Sends the text to `gemini-2.5-flash` to generate a summary in Traditional Chinese.
- **`stock_events_poc.py`**: A data extraction POC that parses unstructured market text and outputs a structured CSV (`market_events.csv`) with Traditional Chinese headers (`類別`, `子類別`, etc.).
- **`check_quota.py`**: A management utility that queries the Google Cloud Service Usage API to report current API quotas (RPM, RPD, TPM) for various models. **Requires Google Cloud SDK authentication.**
- **`requirements.txt`**: Project dependencies (`google-genai`, `requests`, `beautifulsoup4`, `google-api-python-client`, `google-auth`, `google-cloud-service-usage`).

## Setup and Usage

### Prerequisites
- Python 3.x installed.
- A Google GenAI API key.
- **For `check_quota.py` only**:
    - Google Cloud SDK installed (`gcloud` CLI).
    - Application Default Credentials (ADC) configured via `gcloud auth application-default login`.
    - `GCP_PROJECT_ID` environment variable set.

### Installation
1.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Common Commands
- **List Models**: `python list_models.py`
- **Summarize Page**: `python summarize_url.py`
- **Run Basic Test**: `python genai.py`
- **Extract Market Events**: `python stock_events_poc.py`
- **Check API Quotas**: `python check_quota.py`

## Development Notes & Observations
- **Security Update**: The hardcoded API key has been removed. Scripts now require the `GOOGLE_API_KEY` environment variable.
- **Model Selection**:
    - `genai.py` and `summarize_url.py` have been switched to **`gemini-2.5-flash`** to avoid strict rate limits (2 RPM) on the Pro model's free tier.
    - `stock_events_poc.py` also uses `gemini-2.5-flash` for reliability.
- **Quota Management**:
    - `check_quota.py` uses the `google-api-python-client` (Discovery) to query the `serviceusage` API.
    - It requires a real Google Cloud Project ID (not just an API key) and `Service Usage Consumer` permissions.
    - The output is filtered to show a clean table of key models (Flash, Pro) and their RPM/RPD limits.
- **Language Support**:
    - `summarize_url.py`: Summaries are requested in Traditional Chinese.
    - `stock_events_poc.py`: CSV headers and content are explicitly requested in Traditional Chinese.