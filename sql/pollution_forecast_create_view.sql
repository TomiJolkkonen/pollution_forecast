-- SQL example for pollution_forecast
CREATE OR REPLACE VIEW curated.pollution_forecast_view AS
SELECT * FROM parquet_scan('../lake/curated/pollution_forecast');
