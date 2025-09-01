import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset (replace with your file if needed)
df = pd.read_csv('twitter_cleaned.csv')

# Bar plot: Top 10 users by tweet count
plt.figure(figsize=(10, 6))
top_users = df['Username'].value_counts().head(10)
sns.barplot(x=top_users.values, y=top_users.index, palette="coolwarm")
plt.title('Top 10 Users by Tweet Count')
plt.xlabel('Number of Tweets')
plt.ylabel('User')
plt.tight_layout()
plt.show()

# Histogram: Distribution of likes
if 'Likes' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Likes'].dropna(), bins=30, kde=True, color='skyblue')
    plt.title('Distribution of Likes')
    plt.xlabel('Likes')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()



