import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset (replace with your file if needed)
df = pd.read_csv('twitter_dataset.csv')


# Example 2: Average likes by verified status
if 'verified' in df.columns and 'likes' in df.columns:
    avg_likes_verified = df.groupby('verified')['likes'].mean().reset_index()
    plt.figure(figsize=(8, 5))
    sns.barplot(x='verified', y='likes', data=avg_likes_verified, palette='viridis')
    plt.xticks([0, 1], ['Non-Verified', 'Verified'])
    plt.title('Average Likes by Verified Status')
    plt.xlabel('Verified Status')
    plt.ylabel('Average Likes')
    plt.tight_layout()
    plt.show()
    print("\nAverage likes by verified status:")
    print(avg_likes_verified)

