import pandas as pd
import numpy as np

# Load dataset (replace 'titanic.csv' with your file name)
df = pd.read_csv('twitter_dataset.csv')

# Handle missing values
if 'likes' in df.columns:
    df['likes'].fillna(df['likes'].median(), inplace=True)

# Example: Drop rows where a key categorical column is missing
if 'user_location' in df.columns:
    df.dropna(subset=['user_location'], inplace=True)

# Example: Label encoding for a binary categorical column
if 'verified' in df.columns:
    df['verified'] = df['verified'].map({'no': 0, 'yes': 1})

# Example: One-hot encoding for a categorical column
if 'user_location' in df.columns:
    df = pd.get_dummies(df, columns=['user_location'])

# Save cleaned data
df.to_csv('twitter_cleaned.csv', index=False)

print("Data cleaned and saved to twitter_cleaned.csv")