import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
import re

nltk.download('stopwords')


df = pd.read_csv(r'twitter_dataset.csv')  
print(df.columns) 
# Preprocess text: lowercase, remove non-alphabetic, remove stopwords
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = [word for word in text.split() if word not in stop_words]
    return ' '.join(words)

df['clean_text'] = df['Text'].astype(str).apply(preprocess)

# Sentiment scoring using TextBlob
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

df['sentiment'] = df['clean_text'].apply(get_sentiment)
df['sentiment_label'] = df['sentiment'].apply(lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral'))


sentiment_counts = df['sentiment_label'].value_counts()[['positive', 'negative', 'neutral']]

sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])
plt.title('Tweet Sentiment Counts')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.tight_layout()
plt.show()