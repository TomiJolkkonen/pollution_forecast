import pandas as pd
df = pd.read_csv("data/raw/air_quality.csv")
df = df.dropna(subset=["pm2.5"])
df['date'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
df = df[['date', 'pm2.5']]
df.to_csv("data/processed/clean.csv", index=False)