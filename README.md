# Gemini-CLI Workspace

This project serves as a workspace for interacting with Google's Gemini API using the Python `google-genai` SDK. It contains scripts for basic content generation, model exploration, and practical applications like web page summarization.

## Prerequisites

1.  **Python 3.x** installed.
2.  **Google GenAI API Key** (The scripts currently use a hardcoded key, but it is recommended to use environment variables for security).

## Installation

Install the required dependencies:

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
Fetches content from a specified URL and uses **Gemini 2.5 Pro** to generate a comprehensive summary in **Traditional Chinese**.

*   **Current Target:** `https://murmurcats.com/margin-balance-market-guide/`
*   **Model:** `gemini-2.5-pro` (Selected for high token context and reasoning).

```bash
python summarize_url.py
```

### 3. Basic Generation (`genai.py`)
A proof-of-concept script demonstrating text generation and code generation using `gemini-2.5-pro` and `gemini-2.5-flash`.

```bash
python genai.py
```

## Dependencies

*   `google-genai`: Official Python SDK for Gemini.
*   `requests`: For fetching web page content.
*   `beautifulsoup4`: For parsing HTML and extracting text.