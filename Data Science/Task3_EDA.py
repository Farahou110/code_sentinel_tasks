import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset('titanic')

# Correlation matrix heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()

# Top 5 most frequent values in selected columns
for col in ['embarked', 'sex', 'pclass']:
    print(f"\nTop 5 most frequent values in '{col}':")
    print(df[col].value_counts().head(5))

# Distribution plots (histograms and boxplots)
num_cols = ['age', 'fare']
for col in num_cols:
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    sns.histplot(df[col].dropna(), kde=True)
    plt.title(f'Histogram of {col}')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.tight_layout()
    plt.show()