import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read the CSV file or provide your own data
df = pd.read_csv('/users/lucaswiley/desktop/nondurable_goods.csv')

# Calculate the difference between the two series
diff = df['PCEND'] - df['PCEDG']

# Create a time variable for regression
time = np.arange(len(df))

# Perform exponential regression on the difference values
X = sm.add_constant(time)
y = np.log(diff)  # Apply logarithm transformation to the difference values
regression_model = sm.OLS(y, X)
regression_results = regression_model.fit()

# Calculate the predicted values
y_pred = regression_results.predict(X)

# Calculate the residuals
residuals = np.exp(y) - np.exp(y_pred)

# Plotting the residuals
plt.scatter(time, residuals, color='blue')
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Residuals')
plt.title('Residual Plot: Exponential Regression')
plt.show()
