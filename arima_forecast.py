import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pmdarima.arima import auto_arima
# from statsmodels.tsa.arima.model import ARIMA

# Read the CSV file
df = pd.read_csv('/users/lucaswiley/desktop/nondurable_goods.csv')

# Convert the 'date' column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

# Create a new DataFrame for forecasting
forecast_df = pd.DataFrame()

# Set the 'date' column as the index
df.set_index('DATE', inplace=True)

# Model Selection and Forecasting for PCEDG
model_pcedg = auto_arima(df['PCEDG'], seasonal=False, suppress_warnings=True)
model_pcedg_fit = model_pcedg.fit(df['PCEDG'])
forecast_pcedg = model_pcedg_fit.predict(n_periods=120)  # Forecasting for 10 years (120 months)
forecast_df['PCEDG'] = forecast_pcedg

# Model Selection and Forecasting for PCEND
model_pcend = auto_arima(df['PCEND'], seasonal=False, suppress_warnings=True)
model_pcend_fit = model_pcend.fit(df['PCEND'])
forecast_pcend = model_pcend_fit.predict(n_periods=120)  # Forecasting for 10 years (120 months)
forecast_df['PCEND'] = forecast_pcend


# Plotting the original series and the forecasted values
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['PCEDG'], label='PCEDG')
plt.plot(df.index, df['PCEND'], label='PCEND')
plt.plot(forecast_df.index, forecast_df['PCEDG'], label='PCEDG Forecast')
plt.plot(forecast_df.index, forecast_df['PCEND'], label='PCEND Forecast')
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Forecast of PCEDG and PCEND')
plt.grid(True)
plt.legend()
plt.show()
