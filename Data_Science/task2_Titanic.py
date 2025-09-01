import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

df = sns.load_dataset('titanic')


#missing values
df['age'].fillna(df['age'].median(), inplace=True)
df.dropna(subset=['embarked'], inplace=True)


df['sex'] = df['sex'].map({'male': 0, 'female': 1})
df['class'] = df['class'].map({'Third': 3, 'Second': 2, 'First': 1})


plt.figure(figsize=(8, 5))
sns.barplot(x='sex', y='survived', hue='class', data=df)
plt.xticks([0, 1], ['Male', 'Female'])
plt.xlabel('Gender')
plt.ylabel('Survival Rate')
plt.title('Survival Rate by Gender and Class')
plt.legend(title='Class')
plt.tight_layout()
plt.show()