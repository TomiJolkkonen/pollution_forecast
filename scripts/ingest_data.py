import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00381/Beijing%20PM2.5%20Data.csv"
df = pd.read_csv(url)
df.to_csv("data/raw/air_quality.csv", index=False)