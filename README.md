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
產生時間: 2025-12-11 13:40:35 CST

```text
以下是針對您提供文章的詳細摘要，重點關注融資餘額和市場相關性：

---

**大盤融資餘額與市場相關性之深入解析**

本文深入探討了台灣金融市場中「大盤融資餘額」的定義、解讀方法及其與市場走勢的密切相關性，為投資人提供了理解資金流動和風險管理的關鍵視角。

**一、 大盤融資餘額的定義與基本概念**
「大盤融資餘額」是指全市場投資人透過向券商借錢購買股票所累積的總金額。這筆尚未償還的欠款，是衡量市場熱度的重要指標。
*   **市場熱度指標：** 融資餘額越高，通常表示市場熱度升溫，投資人看好後市，積極借錢買股；若快速減少，則可能代表投資人對股市不看好，市場進入冷卻期。

**二、 融資餘額與市場情緒的直接相關性**
融資餘額的變動能快速反映市場情緒與籌碼面變化：
*   **行情轉熱：** 當行情升溫時，融資餘額往往會率先跳動，顯示投資人加碼意願高昂。
*   **大盤修正：** 當市場修正、信心動搖時，融資餘額會快速下滑，引發連鎖反應。例如，文章中提到2025年4月台股因國際局勢衝擊劇烈下跌，K線長黑，融資餘額便快速下降，代表投資人恐慌性賣出或被追繳斷頭。

**三、 融資維持率與市場影響**
「大盤融資維持率」是衡量市場槓桿風險的重要指標，其計算公式為：所有融資股票市值／大盤融資餘額。
*   **市場情緒指標：** 維持率高低直接反映市場多空情緒。穩定或上升的維持率代表多頭信心充足；反之，持續下滑通常意味著市場恐慌，或投資人平倉降低槓桿並觀望市場。
*   **逆勢反彈契機：** 當維持率探低並造成大量斷頭後，市場籌碼可能被清洗，為後續的反彈奠定基礎，可作為波段買入點的參考。

**四、 上櫃融資餘額與大盤的相關性**
「上櫃融資餘額」主要反映中小型股市場的融資狀況，其與加權指數的表現存在特殊相關性。
*   **市場過熱警訊：** 透過「上櫃融資張數除以上市融資張數之年增率」指標觀察，當上櫃融資餘額相對上市融資餘額較高（指標藍線在0軸之上）時，通常代表市場情緒過熱，投資人熱衷追捧中小型股，此時須留意股市反轉風險。

**五、 個股融資餘額與大盤數據的關聯**
個股的融資餘額變化也與股價走勢及大盤有著密切關聯，可反映主力與散戶的對作情形：
*   **融資增、股價跌：** 若個股融資餘額增加但股價卻下跌，可能暗示有大戶趁機出貨，投資人需小心風險。
*   **融資減、股價漲：** 若融資餘額減少但股價卻上漲，通常代表散戶在退出市場，而有大戶悄悄進場承接，這往往是股價築底回升的訊號。
*   **與大盤方向一致：** 文章舉例2025年4月陽明海運(2609)股價因國際關稅與負面新聞大跌，其融資餘額亦銳減，顯示個股融資變化與大盤趨勢及突發事件的連動性。

**六、 融資餘額歷史資料與長期趨勢分析**
從2020年至2025年9月，台股大盤的融資餘額與加權指數長期呈現密切的**正相關**。然而，不同時期也會有其特殊變化：
*   **市場危機時期：** 在2022年美股升息等市場危機期間，融資餘額會快速下滑，反映投資人恐慌性賣出，這往往是多頭結束、空頭來臨的訊號。
*   **寬鬆貨幣政策影響：** 近年來，受寬鬆貨幣政策導致借貸成本降低的影響，投資人更願意進行融資，使融資餘額保持在高位。特別是2023至2025年間，融資餘額增幅明顯超過指數漲幅，這表明散戶和投資人利用槓桿加碼，市場追捧情緒高漲，但也同時反映了**潛在的風險累積**。
*   **市場反彈後的觀望：** 2025年4月大盤快速下跌時，融資也迅速減少；即使到了2025年8月大盤創新高後，許多投資人仍保持觀望，融資餘額尚未恢復到4月下跌前的水平，顯示市場情緒趨於謹慎。

**結論**
綜上所述，大盤融資餘額不僅能快速反映市場情緒，更是觀察籌碼面變化的重要指標。正確解讀融資餘額的增減、維持率變化及其歷史趨勢，有助於投資人更有效地進行資金風險控管，並掌握市場的佈局時機。
```
<!-- END_SUMMARY_OUTPUT -->

### 3. Market Event Extractor (`stock_events_poc.py`)
Parses unstructured financial news text and extracts stock market events into a structured CSV file (`market_events.csv`) with Traditional Chinese headers (`類別`, `子類別`, `事件名稱`...).

*   **Model:** `gemini-2.5-flash`
*   **Output:** `market_events.csv`

<!-- START_EVENTS_OUTPUT -->
產生時間: 2026-02-16 03:36:04 CST

```csv
類別,子類別,事件名稱,開始日期,結束日期,備註,Link1,Link2
市場機制,市場休市,農曆春節前最後交易日,2026-02-11,2026-02-11,台灣證券交易所與櫃檯買賣中心於農曆年前最後一個交易日,,
市場機制,市場休市,農曆春節假期,2026-02-12,2026-02-13,市場休市，僅辦理結算交割作業,,
市場機制,市場休市,農曆春節假期,2026-02-15,2026-02-19,農曆春節連續假期,,
市場機制,市場休市,美國總統日,2026-02-16,2026-02-16,美國股市休市,,
市場機制,市場休市,農曆春節補假,2026-02-20,2026-02-20,農曆春節補假日,,
市場機制,市場開市,農曆春節後開始交易日,2026-02-23,2026-02-23,台灣證券交易所與櫃檯買賣中心於農曆年後第一個交易日,,
經濟數據,就業數據,美國非農就業報告 (1月份),2026-02-11,2026-02-11,美國勞工部公布1月份非農就業報告,,
經濟數據,通貨膨脹,美國PPI數據發布 (部分),2026-02-12,2026-02-12,美國生產者物價指數 (不含食品和能源年增率) 數據發布,,
經濟數據,通貨膨脹,美國CPI報告 (1月份),2026-02-13,2026-02-13,美國勞工統計局公布1月份消費者物價指數報告,,
公司行動,除息,Apple (AAPL) 除息基準日,2026-02-09,2026-02-09,Apple股息支付的股東登記日,,
公司行動,除息,Apple (AAPL) 股息支付日,2026-02-12,2026-02-12,Apple股息支付日,,
```
<!-- END_EVENTS_OUTPUT -->

### 4. API Quota Checker (`check_quota.py`)
Queries the Google Cloud Service Usage API to report current "Requests Per Minute" (RPM), "Requests Per Day" (RPD), and "Tokens Per Minute" (TPM) limits for key Gemini models. This helps in debugging `429 RESOURCE_EXHAUSTED` errors.

*   **Requires:** `gcloud` authentication and `GCP_PROJECT_ID`.

<!-- START_QUOTA_OUTPUT -->
產生時間: 2026-02-23 01:00:11 CST

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
gemini-2.5-pro                 | 1000            | 1000            | 5000000        
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