let
    Source = Csv.Document(File.Contents("../data/pollution_forecast_sample.csv"),[Delimiter=",", Columns=Table.ColumnCount(Table.PromoteHeaders(Csv.Document(File.Contents("../data/pollution_forecast_sample.csv")))), Encoding=65001, QuoteStyle=QuoteStyle.None]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true])
in
    Promoted
