# Gemini-CLI Workspace

This project serves as a workspace for interacting with Google's Gemini API using the Python `google-genai` SDK. It contains scripts for basic content generation, model exploration, practical applications like web page summarization, structured data extraction, and quota management.

## Prerequisites

1.  **Python 3.8+** installed.
2.  **Google GenAI API Key**: Set as an environment variable named `GOOGLE_API_KEY`.
    ```powershell
    $env:GOOGLE_API_KEY="your_api_key_here"
    ```
3.  **Google Cloud SDK (Required for `check_quota.py`)**:
    *   Install the [gcloud CLI](https://cloud.google.com/sdk/docs/install).
    *   Authenticate using Application Default Credentials (ADC):
        ```bash
        gcloud auth application-default login
        ```
    *   Set your Google Cloud Project ID:
        ```bash
        $env:GCP_PROJECT_ID="your-project-id"
        ```

## Installation

Install the required dependencies (now includes Google Cloud libraries):

```bash
pip install -r requirements.txt
```

## Available Scripts

### 1. List Available Models (`list_models.py`)
Lists all Gemini models available to your API key, showing their system names and display names.

```bash
python list_models.py
```

### 2. Web Page Summarizer (`summarize_url.py`)
Fetches content from a specified URL and uses **Gemini 2.5 Flash** to generate a comprehensive summary in **Traditional Chinese**.

*   **Current Target:** `https://murmurcats.com/margin-balance-market-guide/`
*   **Model:** `gemini-2.5-flash` (Optimized for speed and rate limits).

```bash
python summarize_url.py
```

### 3. Market Event Extractor (`stock_events_poc.py`)
Parses unstructured financial news text and extracts stock market events into a structured CSV file (`market_events.csv`) with Traditional Chinese headers (`類別`, `子類別`, `事件名稱`...).

*   **Model:** `gemini-2.5-flash`
*   **Output:** `market_events.csv`

```bash
python stock_events_poc.py
```

### 4. API Quota Checker (`check_quota.py`)
Queries the Google Cloud Service Usage API to report current "Requests Per Minute" (RPM), "Requests Per Day" (RPD), and "Tokens Per Minute" (TPM) limits for key Gemini models. This helps in debugging `429 RESOURCE_EXHAUSTED` errors.

*   **Requires:** `gcloud` authentication and `GCP_PROJECT_ID`.

```bash
python check_quota.py
```

### 5. Basic Generation (`genai.py`)
A proof-of-concept script demonstrating text generation and code generation using `gemini-2.5-flash`.

```bash
python genai.py
```

## Dependencies

*   `google-genai`: Official Python SDK for Gemini.
*   `requests`: For fetching web page content.
*   `beautifulsoup4`: For parsing HTML and extracting text.
*   `google-api-python-client` & `google-auth`: For interacting with Google Cloud APIs (Quota Checker).