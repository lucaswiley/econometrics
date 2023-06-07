import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Read the CSV file or provide your own data
df = pd.read_csv('/users/lucaswiley/desktop/nondurable_goods.csv')

# Convert the 'DATE' column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

# Calculate the difference between the two series
diff = df['PCEND'] - df['PCEDG']

# Create a time variable for regression
time = np.arange(len(df))

# Perform exponential regression on the difference values
X = sm.add_constant(time)
y = np.log(diff)  # Apply logarithm transformation to the difference values
regression_model = sm.OLS(y, X)
regression_results = regression_model.fit()

# Print the regression results summary
print(regression_results.summary())

# Plotting the difference values and regression line
plt.figure(figsize=(10, 6))
plt.scatter(df['DATE'], diff, color='blue', label='Difference ($Billions)')
plt.plot(df['DATE'], np.exp(regression_results.fittedvalues), color='red', linewidth=2, label='Regression Line')
plt.xlabel('Date')
plt.ylabel('Difference ($Billions)')
plt.title('Exponential Trend Analysis: Expenditure Diff between Nondurable and Durable Goods')
plt.legend()

# Determine the trend based on the coefficient
if regression_results.params[1] > 0:
    trend = 'Increasing'
elif regression_results.params[1] < 0:
    trend = 'Decreasing'
else:
    trend = 'No trend'

# Print the trend result
print(f'Trend: {trend}')

plt.show()
