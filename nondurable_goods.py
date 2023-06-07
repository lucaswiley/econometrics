import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('/users/lucaswiley/desktop/nondurable_goods.csv')

# Convert the 'date' column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

# Calculate the rate of change
df['pcedg_diff'] = df['PCEDG'].diff()
df['pcend_diff'] = df['PCEND'].diff()

# Calculate the difference between the two series
df['series_diff'] = df['PCEND'] - df['PCEDG']
df['series_pct_diff'] = (df['PCEND'] - df['PCEDG']) / df['PCEDG']

# Calculate the relative difference between the two series
df['series_diff_relative'] = (df['PCEDG'] - df['PCEND']) / (df['PCEDG'] + df['PCEND'])

# Calculate the normalized difference between the two series
mean_diff = df['PCEND'] - df['PCEDG']
std_diff = mean_diff.std()
df['normalized_diff'] = mean_diff / std_diff

# Calculate the rates of change for PCEDG, PCEND, and the gap
df['pcedg_change'] = df['PCEDG'].diff() / (df['DATE'] - df['DATE'].shift()).dt.days
df['pcend_change'] = df['PCEND'].diff() / (df['DATE'] - df['DATE'].shift()).dt.days
df['gap_change'] = (df['PCEDG'] - df['PCEND']).diff() / (df['DATE'] - df['DATE'].shift()).dt.days


# Plotting the data
plt.figure(figsize=(10, 6))

# plt.plot(df['DATE'], df['PCEDG'], label='PCEDG')
# plt.plot(df['DATE'], df['PCEND'], label='PCEND')


# Highlighting the difference as bars at specific time points
# highlight_dates = pd.to_datetime(['2000-01-01', '2005-01-01', '2010-01-01', '2015-01-01', '2020-01-01'])
# highlight_values = mean_diff[highlight_dates]
# plt.bar(highlight_dates, highlight_values, color='orange', alpha=0.5, width=365*4)  # Width set to 4 years


plt.plot(df['DATE'], df['normalized_diff'], label='Normalized Difference')
# plt.plot(df['DATE'], df['series_diff_relative'], label='Relative Difference')

# plt.fill_between(df['DATE'], df['PCEND'], df['PCEDG'], where=(df['series_diff'] > 0), facecolor='green', alpha=0.3, label='Absolute Gap')
# plt.fill_between(df['DATE'], df['PCEND'], df['PCEDG'], where=(df['series_diff'] < 0), facecolor='red', alpha=0.3)

# plt.plot(df['DATE'], df['series_diff'], label='Gap between pcedg and pcend')
# plt.plot(df['DATE'], df['series_pct_diff'], label='% Gap between pcedg and pcend')

# plt.plot(df['DATE'], df['pcedg_change'], label='PCEDG Rate of Change')
# plt.plot(df['DATE'], df['pcend_change'], label='PCEND Rate of Change')
# plt.plot(df['DATE'], df['gap_change'], label='Gap qRate of Change')

plt.xlabel('Date')
plt.ylabel('Goods Consumed ($Billions)')
plt.title('Line Graph of PCEDG and PCEND')
plt.legend()
plt.grid(True)
plt.show()

# # Plotting the rate of change
# plt.figure(figsize=(10, 6))
# # plt.plot(df['DATE'], df['pcedg_diff'], label='pcedg_diff')
# plt.plot(df['DATE'], df['pcend_diff'], label='pcend_diff')
# plt.xlabel('Date')
# plt.ylabel('Rate of Change')
# plt.title('Rate of Change of pcedg and pcend')
# plt.ylim(-200, 200)  # Set the y-axis limits
# plt.legend()
# plt.grid(True)
# plt.show()

# # Plotting the gap between the two series
# plt.figure(figsize=(10, 6))
# plt.plot(df['DATE'], df['series_diff'], label='Gap between pcedg and pcend')
# plt.xlabel('Date')
# plt.ylabel('Difference')
# plt.title('Widening Gap between pcedg and pcend')
# plt.grid(True)
# plt.legend()
# plt.show()