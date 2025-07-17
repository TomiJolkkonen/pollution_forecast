from prophet import Prophet
import pandas as pd

df = pd.read_csv("data/processed/clean.csv")
df = df.rename(columns={"date": "ds", "pm2.5": "y"})
model = Prophet()
model.fit(df)
model.save("models/model.pkl")