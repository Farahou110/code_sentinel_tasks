import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load your dataset
df = pd.read_csv('twitter_dataset.csv')

# Display available columns to verify the dataset structure
print("Available columns:", df.columns.tolist())

# Convert Timestamp to datetime if it's not already
if 'Timestamp' in df.columns:
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    # Extract date components for grouping
    df['Date'] = df['Timestamp'].dt.date
    df['Hour'] = df['Timestamp'].dt.hour
    df['DayOfWeek'] = df['Timestamp'].dt.day_name()

# Set up the visualization style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Example 1: Group by Username - Top 10 users by average likes
if all(col in df.columns for col in ['Username', 'Likes']):
    user_likes = df.groupby('Username')['Likes'].mean().sort_values(ascending=False).head(10).reset_index()
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Likes', y='Username', data=user_likes, palette='viridis')
    plt.title('Top 10 Users by Average Likes')
    plt.xlabel('Average Likes')
    plt.ylabel('Username')
    plt.tight_layout()
    plt.show()
    
    print("\nTop 10 users by average likes:")
    print(user_likes)

# Example 2: Group by Date - Likes over time
if all(col in df.columns for col in ['Date', 'Likes']):
    daily_likes = df.groupby('Date')['Likes'].sum().reset_index()
    
    plt.figure(figsize=(12, 6))
    plt.plot(daily_likes['Date'], daily_likes['Likes'], marker='o', linewidth=2)
    plt.title('Total Likes Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Likes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    print("\nTotal likes by date:")
    print(daily_likes.head(10))  # Show first 10 rows

# Example 3: Group by Retweets count - Distribution of retweet counts
if 'Retweets' in df.columns:
    retweet_groups = df.groupby('Retweets').size().reset_index(name='Count')
    
    plt.figure(figsize=(12, 6))
    sns.histplot(data=df, x='Retweets', bins=30, kde=True)
    plt.title('Distribution of Retweet Counts')
    plt.xlabel('Number of Retweets')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# Example 4: Group by Day of Week - Engagement by day
if all(col in df.columns for col in ['DayOfWeek', 'Likes']):
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['DayOfWeek'] = pd.Categorical(df['DayOfWeek'], categories=day_order, ordered=True)
    
    weekday_likes = df.groupby('DayOfWeek')['Likes'].mean().reset_index()
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x='DayOfWeek', y='Likes', data=weekday_likes, palette='viridis')
    plt.title('Average Likes by Day of Week')
    plt.xlabel('Day of Week')
    plt.ylabel('Average Likes')
    plt.tight_layout()
    plt.show()
    
    print("\nAverage likes by day of week:")
    print(weekday_likes)

# Example 5: Group by Hour of Day - Engagement by hour
if all(col in df.columns for col in ['Hour', 'Likes']):
    hourly_likes = df.groupby('Hour')['Likes'].mean().reset_index()
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Hour', y='Likes', data=hourly_likes, palette='viridis')
    plt.title('Average Likes by Hour of Day')
    plt.xlabel('Hour of Day')
    plt.ylabel('Average Likes')
    plt.tight_layout()
    plt.show()
    
    print("\nAverage likes by hour of day:")
    print(hourly_likes)