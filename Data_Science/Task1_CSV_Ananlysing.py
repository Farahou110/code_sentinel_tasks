import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame


print("Column Names:")
print(df.columns.tolist())
print()


print(f"Number of Rows: {len(df)}\n")


print("Data Types:")
print(df.dtypes)
print()

print("Summary Statistics:")
print(df.describe(include='all'))
print()


print("Missing Values per Column:")
print(df.isnull().sum())