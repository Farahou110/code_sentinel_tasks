import pandas as pd
from sklearn.datasets import load_iris

# Load Iris dataset from sklearn
iris = load_iris(as_frame=True)
df = iris.frame

# Display column names
print("Column Names:")
print(df.columns.tolist())
print()

# Display number of rows
print(f"Number of Rows: {len(df)}\n")

# Display data types
print("Data Types:")
print(df.dtypes)
print()

# Show summary statistics
print("Summary Statistics:")
print(df.describe(include='all'))
print()

# Check for missing values
print("Missing Values per Column:")
print(df.isnull().sum())