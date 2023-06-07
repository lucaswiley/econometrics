import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Read the CSV file
df = pd.read_csv('/users/lucaswiley/desktop/nondurable_goods.csv')

# Convert the 'date' column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

# Create a new DataFrame for forecasting
forecast_df = pd.DataFrame()

# Set the 'date' column as the index
df.set_index('DATE', inplace=True)

# Calculate the difference between the two series
diff = df['PCEND'] - df['PCEDG']

# Forecasting for PCEDG
model_pcedg = ExponentialSmoothing(df['PCEDG'], trend='add', seasonal='add', seasonal_periods=12)
model_pcedg_fit = model_pcedg.fit()
forecast_pcedg = model_pcedg_fit.predict(start=len(df), end=len(df) + 119)  # Forecasting for 10 years (120 months)
forecast_df['PCEDG'] = forecast_pcedg

# Forecasting for PCEND
model_pcend = ExponentialSmoothing(df['PCEND'], trend='add', seasonal='add', seasonal_periods=12)
model_pcend_fit = model_pcend.fit()
forecast_pcend = model_pcend_fit.predict(start=len(df), end=len(df) + 119)  # Forecasting for 10 years (120 months)
forecast_df['PCEND'] = forecast_pcend

# Highlighting the difference as bars at specific time points
highlight_dates = pd.to_datetime(['2000-01-01', '2005-01-01', '2010-01-01', '2015-01-01', '2020-01-01', '2023-01-01'])
highlight_values = diff[highlight_dates]
highlight_width = 150

for i, date in enumerate(highlight_dates):
    plt.bar(date, highlight_values[i], bottom=df['PCEDG'][date], color='green', alpha=0.5, width=highlight_width)
    plt.text(date, df['PCEDG'][date] + highlight_values[i] / 2, f'{highlight_values[i]:.2f}', ha='center', va='center')

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
