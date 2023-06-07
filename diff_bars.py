import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('/users/lucaswiley/desktop/nondurable_goods.csv')

# Convert the 'date' column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

# Set the 'date' column as the index
df.set_index('DATE', inplace=True)

# Calculate the difference between the two series
diff = df['PCEND'] - df['PCEDG']

# Plotting the original series
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['PCEDG'], label='Durable Goods', color='blue')
plt.plot(df.index, df['PCEND'], label='Nondurable Goods', color='red')

# Highlighting the difference as bars at specific time points
highlight_dates = pd.to_datetime(['2000-01-01', '2005-01-01', '2010-01-01', '2015-01-01', '2020-01-01', '2023-01-01'])
highlight_values = diff[highlight_dates]
highlight_width = 150

for i, date in enumerate(highlight_dates):
    plt.bar(date, highlight_values[i], bottom=df['PCEDG'][date], color='green', alpha=0.5, width=highlight_width)
    plt.text(date, df['PCEDG'][date] + highlight_values[i] / 2, f'{highlight_values[i]:.2f}', ha='center', va='center', fontsize=8)

plt.xlabel('Date')
plt.ylabel('Consumption Expenditure ($Billions)')
plt.title('US Nondurable vs. Durable Goods - Absolute Consumption & Difference ($Billions)')
plt.grid(True)
plt.legend(['Durable Goods', 'Nondurable Goods', 'Difference'])
plt.show()
