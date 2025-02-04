import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import re


# Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to clean tweets
def clean_tweet(tweet_text):
    # Remove URLs
    tweet_text = re.sub(r"http\S+|www\S+|https\S+", "", tweet_text, flags=re.MULTILINE)
    # Remove mentions (@username)
    tweet_text = re.sub(r"@\w+", "", tweet_text)
    # Remove hashtags (#hashtag)
    tweet_text = re.sub(r"#\w+", "", tweet_text)
    # Remove special characters and numbers
    tweet_text = re.sub(r"[^\w\s]", "", tweet_text)
    # Convert to lowercase
    tweet_text = tweet_text.strip().lower()
    return tweet_text

# Function to analyze sentiment using VADER
def analyze_sentiment(tweet_text):
    vs = analyzer.polarity_scores(tweet_text)
    if vs['compound'] >= 0.05:
        return 'Positive'
    elif vs['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Main Execution
if __name__ == "__main__":
    # Load the dataset
    try:
        df = pd.read_csv("apollopharmacy_tweets.csv")
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        exit()

    print("Performing sentiment analysis...")

    # Clean tweets and analyze sentiment
    df['cleaned_text'] = df['text'].apply(clean_tweet)
    df['sentiment'] = df['cleaned_text'].apply(analyze_sentiment)

    # Save results to a new CSV file
    output_filename = "apollopharmacy_sentiment_analysis.csv"
    try:
        df.to_csv(output_filename, index=False, encoding='utf-8')
        print(f"Sentiment analysis results saved to {output_filename}.")
    except Exception as e:
        print(f"Error saving sentiment analysis results: {e}")

    # Visualize sentiment distribution
    sentiment_counts = df['sentiment'].value_counts()
    print("\nSentiment Distribution:")
    print(sentiment_counts)

    # Plot sentiment distribution
    plt.figure(figsize=(8, 6))
    sentiment_counts.plot(kind='bar', color=['green', 'red', 'blue'])
    plt.title('Sentiment Analysis Results')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Tweets')
    plt.xticks(rotation=0)
    plt.show()