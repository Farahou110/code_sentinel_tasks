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
if 'likes' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df['likes'].dropna(), bins=30, kde=True, color='skyblue')
    plt.title('Distribution of Likes')
    plt.xlabel('Likes')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# Pie chart: Verified vs Non-Verified users
if 'verified' in df.columns:
    plt.figure(figsize=(6, 6))
    verified_counts = df['verified'].value_counts()
    plt.pie(verified_counts, labels=verified_counts.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#ff9999'])
    plt.title('Verified vs Non-Verified Users')
    plt.tight_layout()
    plt.show()

# Boxplot: Likes by user location (if not too many unique locations)
if 'user_location' in df.columns and df['user_location'].nunique() < 10:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='user_location', y='likes', data=df)
    plt.title('Likes by User Location')
    plt.xlabel('User Location')
    plt.ylabel('Likes')
    plt.tight_layout()
    plt.show()