import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Read the CSV file or provide your own data
df = pd.read_csv('/users/lucaswiley/desktop/nondurable_goods.csv')

# Calculate the difference between the two series
diff = df['PCEND'] - df['PCEDG']

# Fit the SARIMA model to the difference values
model = SARIMAX(diff, order=(1, 0, 0), seasonal_order=(1, 0, 0, 12))  # Specify the order and seasonal order of the SARIMA model
model_fit = model.fit()

# Obtain the residuals
residuals = model_fit.resid

# Plotting the residuals
plt.plot(residuals)
plt.xlabel('Time')
plt.ylabel('Residuals')
plt.title('Residual Plot: SARIMA Model')
plt.show()
