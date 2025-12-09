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

<!-- START_MODELS_OUTPUT -->
```bash
python list_models.py
```
<!-- END_MODELS_OUTPUT -->

### 2. Web Page Summarizer (`summarize_url.py`)
Fetches content from a specified URL and uses **Gemini 2.5 Flash** to generate a comprehensive summary in **Traditional Chinese**.

*   **Current Target:** `https://murmurcats.com/margin-balance-market-guide/`
*   **Model:** `gemini-2.5-flash` (Optimized for speed and rate limits).

<!-- START_SUMMARY_OUTPUT -->
```bash
python summarize_url.py
```
<!-- END_SUMMARY_OUTPUT -->

### 3. Market Event Extractor (`stock_events_poc.py`)
Parses unstructured financial news text and extracts stock market events into a structured CSV file (`market_events.csv`) with Traditional Chinese headers (`類別`, `子類別`, `事件名稱`...).

*   **Model:** `gemini-2.5-flash`
*   **Output:** `market_events.csv`

<!-- START_EVENTS_OUTPUT -->
產生時間: 2025-12-09 08:02:13 CST

```csv
類別,子類別,事件名稱,開始日期,結束日期,備註
市場機制,其他,TPEx 政府債券公開招標,2025-12-03,2025-12-03,TPEx 主辦
市場機制,指數調整,FTSE 成分股權重調整公告,2025-12-05,2025-12-05,盤後生效。實際調整生效日為第三個週五。
公司行動,法說會,TWSE 上市公司法人說明會,2025-12-01,2025-12-07,於資訊中心舉行
公司行動,法說會,勤益控 (1437) 法人說明會,2025-12-08,2025-12-08,
公司行動,法說會,鴻海 (2317) 法人說明會,2025-12-08,2025-12-08,
公司行動,法說會,致茂 (2360) 法人說明會,2025-12-08,2025-12-08,
公司行動,法說會,聯亞 (3081) 法人說明會,2025-12-08,2025-12-08,
公司行動,法說會,日電貿 (3090) 法人說明會,2025-12-08,2025-12-08,
市場機制,暫停交易,期街口布蘭特正2 (00715L) 暫停交易,2025-12-08,2025-12-08,
市場機制,暫停交易,斐成 (3313) 暫停交易,2025-12-08,2025-12-08,
市場機制,恢復交易,瀚荃 (8103) 恢復交易,2025-12-08,2025-12-08,減資後恢復交易
市場機制,融券暫停,TSMC (2330) 融券暫停,2025-12-08,2025-12-08,
市場機制,融券暫停,00940 融券暫停,2025-12-08,2025-12-08,
公司行動,股息/權利,華建 (2530) 除權息,2025-12-09,2025-12-09,
公司行動,股息/權利,宏正 (6277) 除權息,2025-12-09,2025-12-09,
公司行動,法說會,TECO (1504) 法人說明會,2025-12-09,2025-12-09,
公司行動,法說會,Lite-On (2301) 法人說明會,2025-12-09,2025-12-09,
公司行動,法說會,Foxconn (2317) 法人說明會,2025-12-09,2025-12-09,
公司行動,法說會,Compal (2324) 法人說明會,2025-12-09,2025-12-09,
公司行動,法說會,Quanta (2382) 法人說明會,2025-12-09,2025-12-09,
公司行動,股東會,麗升能源 (8087) 股東會,2025-12-09,2025-12-09,
經濟數據,外匯存底,11月外匯存底公布,2025-12-09,2025-12-09,
全球事件,利率決策,美國 FOMC 利率決策,2025-12-11,2025-12-11,台北時間約02:00公布。對台股開盤影響大
公司行動,財報發布,Broadcom 財報發布,2025-12-11,2025-12-11,
公司行動,財報發布,Oracle 財報發布,2025-12-11,2025-12-11,
```
<!-- END_EVENTS_OUTPUT -->

### 4. API Quota Checker (`check_quota.py`)
Queries the Google Cloud Service Usage API to report current "Requests Per Minute" (RPM), "Requests Per Day" (RPD), and "Tokens Per Minute" (TPM) limits for key Gemini models. This helps in debugging `429 RESOURCE_EXHAUSTED` errors.

*   **Requires:** `gcloud` authentication and `GCP_PROJECT_ID`.

<!-- START_QUOTA_OUTPUT -->
產生時間: 2025-12-09 08:02:51 CST

```text
-------------------------------------------------------------------------------------
Global                         | 15              | 30000           | -1             
gemini-2.0-flash               | 10000           | -               | 10000000       
gemini-2.0-flash-lite          | 20000           | -               | 10000000       
gemini-2.0-flash-live          | -1              | -               | 10000000       
gemini-2.5-flash               | 5               | -               | 3000000        
gemini-2.5-flash-1p            | -               | -               | 3000000        
gemini-2.5-flash-lite          | 10              | -               | 3000000        
gemini-2.5-flash-live          | -1              | -               | 1000000        
gemini-2.5-pro                 | 1000            | 300             | 5000000        
gemini-2.5-pro-1p-freebie      | 75              | -               | 1000000        
-------------------------------------------------------------------------------------
RPM = Requests Per Minute, RPD = Requests Per Day, TPM = Tokens Per Minute
'-' means no specific limit found (or unlimited if not explicitly set to -1).
```
<!-- END_QUOTA_OUTPUT -->

### 5. Basic Generation (`genai.py`)
A proof-of-concept script demonstrating text generation and code generation using `gemini-2.5-flash`.

<!-- START_GENAI_OUTPUT -->
```bash
python genai.py
```
<!-- END_GENAI_OUTPUT -->

## Dependencies

*   `google-genai`: Official Python SDK for Gemini.
*   `requests`: For fetching web page content.
*   `beautifulsoup4`: For parsing HTML and extracting text.
*   `google-api-python-client` & `google-auth`: For interacting with Google Cloud APIs (Quota Checker).