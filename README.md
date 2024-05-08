# AdvertiseX Data Engineering Solution

## Overview
This project is designed to handle data ingestion, processing, correlation, and alerting for AdvertiseX's advertising campaigns. It demonstrates how to work with data in various formats (JSON, CSV, Avro) and how to unify and enrich that data to generate meaningful insights.

### Project Structure
- `ingestion/`
  - `impressions_ingest.py`: Ingests JSON-based ad impression data.
  - `clicks_ingest.py`: Ingests CSV-based clicks and conversion data.
  - `bids_ingest.py`: Ingests Avro-based bid request data.
- `processing/`
  - `standardize.py`: Standardizes data from different formats.
  - `enrichment.py`: Enriches data with additional demographic information.
  - `correlate.py`: Correlates ad impressions with clicks and conversions.
- `alerting/`
  - `monitoring.py`: Monitors data quality and logs alerts for anomalies.
- `README.md`: This documentation file.

## Getting Started
### Prerequisites
- Python 3.x
- Python libraries: kafka-python, fastavro

### Installation
1. Clone this repository:  
   ```bash
   git clone https://github.com/yourusername/AdvertiseX-Data-Engineering.git
   ```
2. Install required libraries:  
   ```bash
   pip install kafka-python fastavro
   ```

### Running the Scripts
1. **Ingestion:**  
   - Make sure that your data sources are available and configured correctly.
   - Adjust paths in the ingestion scripts to match the actual file locations or data streams.
   - Execute the ingestion scripts one by one.

   Example:
   ```bash
   python ingestion/impressions_ingest.py
   python ingestion/clicks_ingest.py
   python ingestion/bids_ingest.py
   ```

2. **Processing:**  
   - Utilize functions from `processing` to standardize and enrich the ingested data.

   Example:
   ```python
   from processing.standardize import standardize_impressions
   from processing.enrichment import enrich_data
   ```

3. **Alerting:**  
   - Run the monitoring script to check data quality.
   ```bash
   python alerting/monitoring.py
   ```

### Contribution
Feel free to open issues or submit pull requests with improvements and bug fixes.

### License
This project is open-source and licensed under the MIT License.
