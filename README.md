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
產生時間: 2025-12-11 13:33:49 CST

```text
Model Name: models/embedding-gecko-001
Display Name: Embedding Gecko
--------------------
Model Name: models/gemini-2.5-flash
Display Name: Gemini 2.5 Flash
--------------------
Model Name: models/gemini-2.5-pro
Display Name: Gemini 2.5 Pro
--------------------
Model Name: models/gemini-2.0-flash-exp
Display Name: Gemini 2.0 Flash Experimental
--------------------
Model Name: models/gemini-2.0-flash
Display Name: Gemini 2.0 Flash
--------------------
Model Name: models/gemini-2.0-flash-001
Display Name: Gemini 2.0 Flash 001
--------------------
Model Name: models/gemini-2.0-flash-exp-image-generation
Display Name: Gemini 2.0 Flash (Image Generation) Experimental
--------------------
Model Name: models/gemini-2.0-flash-lite-001
Display Name: Gemini 2.0 Flash-Lite 001
--------------------
Model Name: models/gemini-2.0-flash-lite
Display Name: Gemini 2.0 Flash-Lite
--------------------
Model Name: models/gemini-2.0-flash-lite-preview-02-05
Display Name: Gemini 2.0 Flash-Lite Preview 02-05
--------------------
Model Name: models/gemini-2.0-flash-lite-preview
Display Name: Gemini 2.0 Flash-Lite Preview
--------------------
Model Name: models/gemini-exp-1206
Display Name: Gemini Experimental 1206
--------------------
Model Name: models/gemini-2.5-flash-preview-tts
Display Name: Gemini 2.5 Flash Preview TTS
--------------------
Model Name: models/gemini-2.5-pro-preview-tts
Display Name: Gemini 2.5 Pro Preview TTS
--------------------
Model Name: models/gemma-3-1b-it
Display Name: Gemma 3 1B
--------------------
Model Name: models/gemma-3-4b-it
Display Name: Gemma 3 4B
--------------------
Model Name: models/gemma-3-12b-it
Display Name: Gemma 3 12B
--------------------
Model Name: models/gemma-3-27b-it
Display Name: Gemma 3 27B
--------------------
Model Name: models/gemma-3n-e4b-it
Display Name: Gemma 3n E4B
--------------------
Model Name: models/gemma-3n-e2b-it
Display Name: Gemma 3n E2B
--------------------
Model Name: models/gemini-flash-latest
Display Name: Gemini Flash Latest
--------------------
Model Name: models/gemini-flash-lite-latest
Display Name: Gemini Flash-Lite Latest
--------------------
Model Name: models/gemini-pro-latest
Display Name: Gemini Pro Latest
--------------------
Model Name: models/gemini-2.5-flash-lite
Display Name: Gemini 2.5 Flash-Lite
--------------------
Model Name: models/gemini-2.5-flash-image-preview
Display Name: Nano Banana
--------------------
Model Name: models/gemini-2.5-flash-image
Display Name: Nano Banana
--------------------
Model Name: models/gemini-2.5-flash-preview-09-2025
Display Name: Gemini 2.5 Flash Preview Sep 2025
--------------------
Model Name: models/gemini-2.5-flash-lite-preview-09-2025
Display Name: Gemini 2.5 Flash-Lite Preview Sep 2025
--------------------
Model Name: models/gemini-3-pro-preview
Display Name: Gemini 3 Pro Preview
--------------------
Model Name: models/gemini-3-pro-image-preview
Display Name: Nano Banana Pro
--------------------
Model Name: models/nano-banana-pro-preview
Display Name: Nano Banana Pro
--------------------
Model Name: models/gemini-robotics-er-1.5-preview
Display Name: Gemini Robotics-ER 1.5 Preview
--------------------
Model Name: models/gemini-2.5-computer-use-preview-10-2025
Display Name: Gemini 2.5 Computer Use Preview 10-2025
--------------------
Model Name: models/embedding-001
Display Name: Embedding 001
--------------------
Model Name: models/text-embedding-004
Display Name: Text Embedding 004
--------------------
Model Name: models/gemini-embedding-exp-03-07
Display Name: Gemini Embedding Experimental 03-07
--------------------
Model Name: models/gemini-embedding-exp
Display Name: Gemini Embedding Experimental
--------------------
Model Name: models/gemini-embedding-001
Display Name: Gemini Embedding 001
--------------------
Model Name: models/aqa
Display Name: Model that performs Attributed Question Answering.
--------------------
Model Name: models/imagen-4.0-generate-preview-06-06
Display Name: Imagen 4 (Preview)
--------------------
Model Name: models/imagen-4.0-ultra-generate-preview-06-06
Display Name: Imagen 4 Ultra (Preview)
--------------------
Model Name: models/imagen-4.0-generate-001
Display Name: Imagen 4
--------------------
Model Name: models/imagen-4.0-ultra-generate-001
Display Name: Imagen 4 Ultra
--------------------
Model Name: models/imagen-4.0-fast-generate-001
Display Name: Imagen 4 Fast
--------------------
Model Name: models/veo-2.0-generate-001
Display Name: Veo 2
--------------------
Model Name: models/veo-3.0-generate-001
Display Name: Veo 3
--------------------
Model Name: models/veo-3.0-fast-generate-001
Display Name: Veo 3 fast
--------------------
Model Name: models/veo-3.1-generate-preview
Display Name: Veo 3.1
--------------------
Model Name: models/veo-3.1-fast-generate-preview
Display Name: Veo 3.1 fast
--------------------
Model Name: models/gemini-2.5-flash-native-audio-latest
Display Name: Gemini 2.5 Flash Native Audio Latest
--------------------
Model Name: models/gemini-2.5-flash-native-audio-preview-09-2025
Display Name: Gemini 2.5 Flash Native Audio Preview 09-2025
--------------------
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
產生時間: 2025-12-10 06:05:17 CST

```text
-------------------------------------------------------------------------------------
Global                         | 15              | 30000           | -1             
gemini-2.0-flash               | 10000           | -1              | 10000000       
gemini-2.0-flash-lite          | 20000           | -1              | 10000000       
gemini-2.0-flash-live          | -1              | -1              | 10000000       
gemini-2.5-flash               | 5               | 10000           | 3000000        
gemini-2.5-flash-1p            | -               | -               | 3000000        
gemini-2.5-flash-lite          | 10              | -1              | 3000000        
gemini-2.5-flash-live          | -1              | -1              | 1000000        
gemini-2.5-pro                 | 1000            | 10000           | 5000000        
gemini-2.5-pro-1p-freebie      | 75              | 10000           | 1000000        
-------------------------------------------------------------------------------------
RPM = Requests Per Minute, RPD = Requests Per Day, TPM = Tokens Per Minute
'-' means no specific limit found (or unlimited if not explicitly set to -1).
```
<!-- END_QUOTA_OUTPUT -->

### 5. Basic Generation (`genai.py`)
A proof-of-concept script demonstrating text generation and code generation using `gemini-2.5-flash`.

<!-- START_GENAI_OUTPUT -->
產生時間: 2025-12-11 13:38:52 CST

```text
--- AI Explanation ---
人工智慧（AI）的核心運作原理，是讓電腦系統模仿人類的智能行為，但其方式並非天生具備智慧，而是透過「學習」而來。

這個學習過程首先需要龐大的「資料」（或稱數據）作為基礎。這些資料可以是圖像、文字、聲音，或是任何結構化的資訊。AI系統會使用特定的「演算法」來分析、處理這些資料，並從中「訓練」出能夠識別模式、建立關聯性與理解規律的「模型」。

想像成一個學生：資料就是課本和習題，演算法則是學習方法和思考邏輯，而學習後對知識的掌握，就是AI建立起來的「模型」。

當AI模型被訓練完成後，當它遇到新的、未曾見過的資料時，就能運用這些學到的知識進行「預測」、「判斷」或「決策」。例如，在圖像識別中，模型學會了貓的特徵，就能從新圖片中辨識出貓；在翻譯中，模型學習了兩種語言的對應關係，就能進行翻譯。

簡單來說，AI就是透過接收大量資料，利用演算法從中學習並建立模型，最終讓機器學會思考、分析和完成特定任務。它是一個不斷從經驗中改進，以達成人類智慧目標的過程。

--- Quota Code Example ---
Knowing the quota for Google Generative AI (GenAI) API is a crucial aspect of managing your application's usage and avoiding rate limits. Unlike some APIs that return quota information directly in response headers, Google Cloud generally manages quotas and usage through dedicated APIs:

1.  **Service Usage API**: To get the *configured quota limits* for a service in your project.
2.  **Cloud Monitoring API**: To get *current usage* metrics against those quotas.

The `google.generativeai` client library itself does not expose a direct method to check quotas. You need to use the Google Cloud client libraries for Service Usage and Monitoring.

Here's a Python script that demonstrates how to do this for the Generative Language API (the public API used by `google.generativeai` for PaLM/Gemini models).

---

### Prerequisites

1.  **Enable APIs**: Ensure the following APIs are enabled in your Google Cloud Project:
    *   `Service Usage API`
    *   `Cloud Monitoring API`
    *   `Generative Language API` (or `AI Platform API` if you're using Vertex AI)

2.  **Authentication**:
    *   **Local Development**: Run `gcloud auth application-default login` in your terminal.
    *   **Production**: Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your service account key file, or ensure your compute environment has appropriate service account permissions.

3.  **Permissions**: The service account or user running this script needs:
    *   `serviceusage.quotas.get` on the project.
    *   `monitoring.timeSeries.list` on the project.

4.  **Install Client Libraries**:
    ```bash
    pip install google-cloud-service-usage google-cloud-monitoring google-cloud-resource-manager google-auth
    ```

---

### Python Code

```python
import os
import google.auth
from google.cloud import service_usage_v1
from google.cloud import monitoring_v3
from google.api import metric_pb2, monitored_resource_pb2
from google.protobuf import timestamp_pb2
from datetime import datetime, timedelta

def get_project_id():
    """Attempts to determine the Google Cloud Project ID."""
    try:
        _, project_id = google.auth.default()
        if project_id:
            return project_id
    except Exception as e:
        print(f"Could not determine project ID automatically: {e}")
        print("Please ensure you are authenticated (e.g., `gcloud auth application-default login`) or set the GOOGLE_CLOUD_PROJECT environment variable.")

    # Fallback to environment variable
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    if project_id:
        return project_id

    raise ValueError("Google Cloud Project ID could not be determined. Please set GOOGLE_CLOUD_PROJECT environment variable or authenticate.")


def get_genai_api_quotas(project_id: str, service_name: str = "generativelanguage.googleapis.com"):
    """
    Retrieves the quota limits for the specified Generative AI service.

    Args:
        project_id: Your Google Cloud project ID.
        service_name: The API service name (e.g., 'generativelanguage.googleapis.com' for public Gemini/PaLM).
                      Use 'aiplatform.googleapis.com' for Vertex AI Gemini/PaLM.

    Returns:
        A dictionary containing quota limits, or None if an error occurs.
    """
    client = service_usage_v1.ServiceUsageClient()
    parent = f"projects/{project_id}"
    quotas_info = {}

    print(f"\n--- Quota Limits for Service: {service_name} ---")
    try:
        request = service_usage_v1.ListConsumerQuotasRequest(
            parent=parent,
            service=service_name,
            view=service_usage_v1.QuotaView.FULL,
        )
        response = client.list_consumer_quotas(request=request)

        found_genai_quotas = False
        for quota in response.quotas:
            # Filter for relevant GenAI quotas. Names might vary slightly.
            # Common ones include 'generative_language_api_requests_per_minute'
            # or 'model_requests_per_minute' etc.
            if "generative_language" in quota.metric or "model_requests" in quota.metric:
                found_genai_quotas = True
                for limit in quota.limits:
                    # Per-region or global limits
                    location = limit.metric_dimensions.get("location", "global")
                    quota_name = f"{quota.display_name} ({quota.metric}) [{location}]"
                    quotas_info[quota_name] = {
                        "metric": quota.metric,
                        "display_name": quota.display_name,
                        "unit": quota.unit,
                        "limit": limit.value,
                        "is_enforced": limit.is_enforced,
                        "location": location,
                        "quota_metric_name_for_monitoring": quota.metric # This is key for Monitoring API
                    }
                    print(f"  {quota_name}:")
                    print(f"    Limit: {limit.value} {quota.unit} (Enforced: {limit.is_enforced})")
                    print(f"    Metric Name (for Monitoring): {quota.metric}")

        if not found_genai_quotas:
            print(f"  No specific Generative AI quotas found for {service_name}. "
                  "This might mean you are looking at the wrong service or the quota names have changed.")
            print("  Listing first few general quotas found:")
            for i, quota in enumerate(response.quotas):
                if i >= 3: break
                print(f"    - {quota.display_name} ({quota.metric}): Limit {quota.limits[0].value if quota.limits else 'N/A'}")
            print("\nConsider checking the Google Cloud console for exact quota metric names.")


    except Exception as e:
        print(f"Error fetching quotas for {service_name}: {e}")
    return quotas_info

def get_genai_api_quota_usage(project_id: str, quota_metric_name: str, service_name: str = "generativelanguage.googleapis.com"):
    """
    Retrieves the current usage for a specific Generative AI quota metric.

    Args:
        project_id: Your Google Cloud project ID.
        quota_metric_name: The exact metric name obtained from get_genai_api_quotas
                           (e.g., 'generativelanguage.googleapis.com/model/requests').
        service_name: The API service name (e.g., 'generativelanguage.googleapis.com').
                      This is used as a filter in the monitoring query.

    Returns:
        The current usage (e.g., requests per minute) as an integer or float, or None if an error occurs.
    """
    client = monitoring_v3.MetricServiceClient()
    project_name = f"projects/{project_id}"

    now = datetime.utcnow()
    # Look at usage over the last 5 minutes, aggregated per minute
    start_time = now - timedelta(minutes=5)
    end_time = now

    interval = monitoring_v3.TimeInterval(
        end_time=timestamp_pb2.Timestamp(seconds=int(end_time.timestamp())),
        start_time=timestamp_pb2.Timestamp(seconds=int(start_time.timestamp())),
    )

    # For quota usage, we generally query 'serviceruntime.googleapis.com/quota/rate/net_usage'
    # and filter by the specific 'quota_metric' and 'service'
    filter_string = (
        f'metric.type = "serviceruntime.googleapis.com/quota/rate/net_usage" AND '
        f'resource.labels.project_id = "{project_id}" AND '
        f'metric.labels.quota_metric = "{quota_metric_name}" AND '
        f'metric.labels.service = "{service_name}"'
    )

    print(f"\n--- Current Usage for Quota Metric: {quota_metric_name} ---")
    try:
        # Aggregate the data. We want the most recent "mean" value over short intervals.
        aggregation = monitoring_v3.Aggregation(
            alignment_period=timestamp_pb2.Duration(seconds=60), # Align to 1 minute
            per_series_aligner=monitoring_v3.Aggregation.Aligner.ALIGN_RATE, # Calculate rate
            cross_series_reducer=monitoring_v3.Aggregation.Reducer.REDUCE_SUM, # Sum across regions/dimensions
            group_by_fields=['resource.location'] # Group by location if desired, then sum
        )

        results = client.list_time_series(
            name=project_name,
            filter=filter_string,
            interval=interval,
            view=monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
            aggregation=aggregation
        )

        current_usage = 0
        latest_point_value = None

        for series in results:
            if series.points:
                # Points are ordered by time, most recent last
                latest_point = series.points[-1]
                # Value type could be int64, double, etc.
                if latest_point.value.HasField("int64_value"):
                    latest_point_value = latest_point.value.int64_value
                elif latest_point.value.HasField("double_value"):
                    latest_point_value = latest_point.value.double_value
                
                current_usage += latest_point_value if latest_point_value is not None else 0
                
                location = series.resource.labels.get('location', 'global')
                print(f"  Usage in {location} ({latest_point.interval.end_time.ToDatetime().strftime('%H:%M:%S')}): {latest_point_value:.2f}")

        if latest_point_value is None:
            print(f"  No usage data found for '{quota_metric_name}' in the last 5 minutes.")
        else:
            print(f"  Total Estimated Usage (across all locations) in the last minute: {current_usage:.2f}")

        return current_usage

    except Exception as e:
        print(f"Error fetching usage for {quota_metric_name}: {e}")
        return None

def main():
    try:
        project_id = get_project_id()
        print(f"Using Google Cloud Project ID: {project_id}")

        # --- For Public Generative Language API (generativelanguage.googleapis.com) ---
        genai_service = "generativelanguage.googleapis.com"
        genai_quotas = get_genai_api_quotas(project_id, genai_service)

        if genai_quotas:
            print("\n--- Summary of Generative Language API Quotas and Usage ---")
            for quota_name, details in genai_quotas.items():
                quota_limit = details['limit']
                quota_metric_for_monitoring = details['quota_metric_name_for_monitoring']

                # Get the actual usage for this specific metric
                current_usage = get_genai_api_quota_usage(project_id, quota_metric_for_monitoring, genai_service)

                if current_usage is not None:
                    print(f"\nQuota: {quota_name}")
                    print(f"  Limit: {quota_limit} {details['unit']}")
                    print(f"  Current Usage (per minute): {current_usage:.2f} {details['unit']}")
                    remaining = quota_limit - current_usage
                    print(f"  Remaining: {remaining:.2f} {details['unit']}")
                else:
                    print(f"\nQuota: {quota_name}")
                    print(f"  Limit: {quota_limit} {details['unit']}")
                    print("  Could not retrieve current usage.")

        # --- Optional: For Vertex AI Generative AI (aiplatform.googleapis.com) ---
        # If you are using Vertex AI's managed Generative AI models (e.g., Gemini on Vertex AI),
        # their quotas and metrics are typically under the 'aiplatform.googleapis.com' service.
        # You would uncomment and adapt the following:
        #
        # vertex_ai_service = "aiplatform.googleapis.com"
        # vertex_quotas = get_genai_api_quotas(project_id, vertex_ai_service)
        # if vertex_quotas:
        #     print("\n--- Summary of Vertex AI Generative AI Quotas and Usage ---")
        #     for quota_name, details in vertex_quotas.items():
        #         # Vertex AI metrics might be named differently, e.g., 'aiplatform.googleapis.com/prediction/request_count'
        #         # You'd need to identify the exact quota_metric_name_for_monitoring for Vertex AI.
        #         # For example, if you found a quota with metric 'aiplatform.googleapis.com/prediction/request_count'
        #         # you would use that here.
        #         quota_metric_for_monitoring = details['quota_metric_name_for_monitoring']
        #         current_usage = get_genai_api_quota_usage(project_id, quota_metric_for_monitoring, vertex_ai_service)
        #         if current_usage is not None:
        #             print(f"\nQuota: {quota_name}")
        #             print(f"  Limit: {details['limit']} {details['unit']}")
        #             print(f"  Current Usage (per minute): {current_usage:.2f} {details['unit']}")
        #             print(f"  Remaining: {details['limit'] - current_usage:.2f} {details['unit']}")
        #         else:
        #             print(f"\nQuota: {quota_name}")
        #             print(f"  Limit: {details['limit']} {details['unit']}")
        #             print("  Could not retrieve current usage.")

    except ValueError as e:
        print(f"Configuration Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

---

### How to Use:

1.  **Save** the code as a Python file (e.g., `check_genai_quota.py`).
2.  **Ensure** you have completed the prerequisites (installed libraries, authenticated, enabled APIs, correct permissions).
3.  **Run** the script from your terminal:
    ```bash
    python check_genai_quota.py
    ```

### Expected Output (Example):

```
Using Google Cloud Project ID: your-gcp-project-id

--- Quota Limits for Service: generativelanguage.googleapis.com ---
  Generative Language API requests per minute (generativelanguage.googleapis.com/model/requests) [global]:
    Limit: 60 unit (Enforced: True)
    Metric Name (for Monitoring): generativelanguage.googleapis.com/model/requests

--- Summary of Generative Language API Quotas and Usage ---

--- Current Usage for Quota Metric: generativelanguage.googleapis.com/model/requests ---
  Usage in global (10:30:15): 2.00
  Total Estimated Usage (across all locations) in the last minute: 2.00

Quota: Generative Language API requests per minute (generativelanguage.googleapis.com/model/requests) [global]
  Limit: 60 unit
  Current Usage (per minute): 2.00 unit
  Remaining: 58.00 unit
```

### Explanation:

1.  **`get_project_id()`**: Tries to automatically get your GCP project ID from your `gcloud` configuration or the `GOOGLE_CLOUD_PROJECT` environment variable.
2.  **`get_genai_api_quotas()`**:
    *   Initializes `service_usage_v1.ServiceUsageClient`.
    *   Makes a `ListConsumerQuotasRequest` for the specified service (`generativelanguage.googleapis.com` for the public GenAI API).
    *   It then iterates through the returned quotas. Google Cloud services often have many quotas, so the code specifically looks for quotas related to "generative_language" or "model_requests" to filter for relevant GenAI API limits.
    *   It extracts the `display_name`, `metric` (which is crucial for the monitoring API), `unit`, `limit`, and `is_enforced` status.
3.  **`get_genai_api_quota_usage()`**:
    *   Initializes `monitoring_v3.MetricServiceClient`.
    *   Defines a time interval (e.g., the last 5 minutes).
    *   Constructs a `filter_string` for the monitoring API:
        *   `metric.type = "serviceruntime.googleapis.com/quota/rate/net_usage"`: This is the standard Google Cloud metric type for tracking *usage against a quota*.
        *   `metric.labels.quota_metric = "{quota_metric_name}"`: This links the usage to the *specific quota metric* identified by the `ServiceUsageClient`.
        *   `metric.labels.service = "{service_name}"`: Further filters by the API service.
    *   Configures `aggregation` to get the `ALIGN_RATE` over a `60-second` period, effectively giving you "requests per minute."
    *   It then iterates through the time series results to find the latest value, which represents the current usage rate.
4.  **`main()`**: Orchestrates the calls, first getting limits, then for each relevant limit, fetching its current usage and printing a summary.

This approach provides a comprehensive way to programmatically check both your Generative AI API quota limits and your current usage against those limits in Google Cloud.
```
<!-- END_GENAI_OUTPUT -->

## Dependencies

*   `google-genai`: Official Python SDK for Gemini.
*   `requests`: For fetching web page content.
*   `beautifulsoup4`: For parsing HTML and extracting text.
*   `google-api-python-client` & `google-auth`: For interacting with Google Cloud APIs (Quota Checker).