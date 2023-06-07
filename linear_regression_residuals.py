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

# Add a constant term to the independent variable for the regression
X = sm.add_constant(time)

# Perform linear regression on the difference values
regression_model = sm.OLS(diff, X)
regression_results = regression_model.fit()
residuals = regression_results.resid

# Print the regression results summary
print(regression_results.summary())

plt.scatter(regression_results.fittedvalues, residuals, color='blue')
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')

# Display regression output
print(regression_results.summary())

plt.show()