import pandas as pd
from babylon.data.twitter.api import Session
from tqdm import tqdm
from configparser import ConfigParser

cp = ConfigParser()
cp.read("../.secret/credentials.ini")

print("Creating a Twitter session...")
twitter_session = Session(
    cp['emas_twitter_credentials']['consumer_key'],
    cp['emas_twitter_credentials']['consumer_secret'],
    cp['emas_twitter_credentials']['access_token'],
    cp['emas_twitter_credentials']['access_token_secret']
)

print("Dowloading tweets (user: @bbc)")
bbc_id = twitter_session.user_id('bbc')
bbc_tweets = twitter_session.tweets(bbc_id)

print("Saving data to disk...")
columns = list(bbc_tweets[0].as_dict.keys())
tweets_df = pd.DataFrame(columns=columns)
for tweet in tqdm(bbc_tweets):
    tweets_df = tweets_df.append(tweet.as_dict, ignore_index=True)
tweets_df.to_csv("../input/tweets.csv")