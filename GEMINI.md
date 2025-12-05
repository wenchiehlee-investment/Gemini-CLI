# Gemini-CLI Project Context

## Project Overview
This project is a Python-based workspace for interacting with Google's Gemini API. It has evolved from simple text generation to include utility scripts for model exploration and practical tasks like web scraping and summarization.

## Key Files
- **`genai.py`**: Basic proof-of-concept script. Authenticates and generates text/code using `gemini-2.5-pro` and `gemini-2.5-flash`.
- **`list_models.py`**: Utility script to query the API and print a list of all available models (e.g., Flash, Pro, Experimental variants).
- **`summarize_url.py`**: A more advanced script that:
    1.  Fetches HTML content from a URL using `requests`.
    2.  Cleans and extracts text using `BeautifulSoup`.
    3.  Sends the text to `gemini-2.5-pro` to generate a summary in Traditional Chinese.
- **`requirements.txt`**: Project dependencies (`google-genai`, `requests`, `beautifulsoup4`).

## Setup and Usage

### Prerequisites
- Python 3.x installed.
- A Google GenAI API key.

### Installation
1.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

### Common Commands
- **List Models**: `python list_models.py`
- **Summarize Page**: `python summarize_url.py`
- **Run Basic Test**: `python genai.py`

## Development Notes & Observations
- **Security Update**: The hardcoded API key has been removed. Scripts now require the `GOOGLE_API_KEY` environment variable.
- **Model Selection**:
    - `list_models.py` confirms access to newer models like `gemini-2.5-flash`, `gemini-2.5-pro`, and experimental versions.
    - `summarize_url.py` specifically uses `gemini-2.5-pro` to handle large context windows required for full-page articles.
- **Language Support**: The summarization prompt is currently hardcoded to request Traditional Chinese.