from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt

model = Prophet()
model = model.load("models/model.pkl")
df = pd.read_csv("data/processed/clean.csv")
df = df.rename(columns={"date": "ds", "pm2.5": "y"})
future = model.make_future_dataframe(periods=48, freq="H")
forecast = model.predict(future)
model.plot(forecast)
plt.savefig("dashboards/forecast.png")