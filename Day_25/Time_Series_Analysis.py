!pip install pandas matplotlib seaborn statsmodels prophet
import pandas as pd

df = pd.read_csv('1_Daily_minimum_temps.csv')  # format: Date, Temp
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
print(df.head())
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(15,5))
sns.lineplot(data=df, x='Date', y='Temp')
plt.title("Daily Minimum Temperatures in Melbourne")
plt.show()
# Step 1: Inspect the problematic values
print(df['Temp'].unique())  # See what values exist

# Step 2: Clean the data - convert to numeric, force errors to NaN
df['Temp'] = pd.to_numeric(df['Temp'], errors='coerce')

# Step 3: Drop rows where conversion failed (i.e., was non-numeric like '?0.2')
df = df.dropna(subset=['Temp'])

# Step 4: Rerun ADF Test
from statsmodels.tsa.stattools import adfuller

result = adfuller(df['Temp'])
print(f'ADF Statistic: {result[0]}')
print(f'p-value: {result[1]}')
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(df['Temp'], order=(5,1,0))
model_fit = model.fit()
forecast = model_fit.forecast(steps=30)

plt.figure(figsize=(10,4))
plt.plot(df['Temp'][-100:], label='Past')
plt.plot(pd.date_range(start=df.index[-1], periods=31, freq='D')[1:], forecast, label='Forecast')
plt.legend()
plt.title("ARIMA Forecast - Next 30 Days")
plt.show()
from prophet import Prophet

df_prophet = df.reset_index().rename(columns={"Date": "ds", "Temp": "y"})
model = Prophet()
model.fit(df_prophet)df = df.asfreq('D')
df['Temp'] = df['Temp'].interpolate()  # or use .fillna(method='ffill')


future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

model.plot(forecast)
plt.title("Prophet Forecast")
plt.show()
df = df.asfreq('D')  # 'D' = daily frequency
print(df.index.freq)
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np

# Split again
train = df[:'1989']
test = df['1990':]

model = ARIMA(train['Temp'], order=(5,1,0))
model_fit = model.fit()

preds = model_fit.forecast(steps=len(test))
rmse = np.sqrt(mean_squared_error(test['Temp'], preds))

print(f'RMSE: {rmse}')

