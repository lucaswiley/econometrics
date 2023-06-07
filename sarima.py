import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Read the CSV file or provide your own data
df = pd.read_csv('/users/lucaswiley/desktop/nondurable_goods.csv')

# Calculate the difference between the two series
diff = df['PCEND'] - df['PCEDG']

# Fit the ARIMA model to the difference values
model = ARIMA(diff, order=(1, 0, 0))
model_fit = model.fit()

# Get the predicted values using the ARIMA model
predicted_values = model_fit.predict()

# Plotting the original difference values and the ARIMA predictions
plt.figure(figsize=(10, 6))
plt.plot(df['DATE'], diff, color='blue', label='Difference')  # Plot the original difference values
plt.plot(df['DATE'], predicted_values, color='red', linewidth=2, label='ARIMA Predictions')  # Plot the ARIMA predictions
plt.xlabel('Time')
plt.ylabel('Difference')
plt.title('ARIMA Modeling: Difference between Series1 and Series2')
plt.legend()
plt.show()
