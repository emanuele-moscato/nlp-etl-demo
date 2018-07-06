from babylon.sentiment import sentiment_scores
import pandas as pd
from tqdm import tqdm

print("Loading tweets from disk...")
tweets_df = pd.read_csv("../input/tweets.csv")

print("Computing sentiment scores...")
for i in tqdm(range(len(tweets_df))):
    tweets_df.at[i, 'sentiment'] = sentiment_scores(
        tweets_df.iloc[i]['text'],
        polarity='compound'
    )
    
print("Saving data to disk...")
tweets_df.to_csv("../output/tweets_with_sentiment.csv", index=False)