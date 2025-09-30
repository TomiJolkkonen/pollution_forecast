# Pollution Forecast
This project is converted to be Fabric + Power BI ready.

## Contents
- `data/` sample CSV for local testing
- `notebooks/01_ingest_transform.ipynb` — PySpark notebook to ingest CSV and write parquet to `../lake/curated/pollution_forecast`
- `notebooks/02_analysis_or_model.ipynb` — analysis / model notebook
- `sql/` SQL scripts to create views over curated data
- `powerbi/` Power Query M and instructions to build the report
- `lake/` (not included) — intended target for curated parquet in Fabric Lakehouse

## How to use in Fabric
1. Upload the `data/` files to your ADLS Gen2 or Lakehouse `lake/raw/pollution_forecast/`.
2. Open the notebooks in Fabric, run `01_ingest_transform` to produce parquet under `lake/curated/pollution_forecast`.
3. Use Power BI to connect to the curated location and create a report. See `powerbi/report_instructions.md`.

