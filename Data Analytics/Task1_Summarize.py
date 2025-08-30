import pandas as pd

# Replace 'twitter_dataset.csv' with your actual CSV file path if different
df = pd.read_csv('twitter_dataset.csv')

# Print column names
print("Column Names:")
print(df.columns.tolist())

# Print number of rows
print("\nNumber of Rows:")
print(len(df))

# Print summary statistics
print("\nSummary Statistics:")
summary = df.describe(include='all')
print(summary)

# Save summary statistics to a new CSV file
summary.to_csv('summary.csv')