from twitterscraper import query_tweets
import pymongo
import pandas as pd
import json
from datetime import datetime,date,timedelta
import time
from textblob import TextBlob
from mymodules.mongodb import dataframe_to_mongo
from googletrans import Translator
import re
from mymodules.preprocessing import tweet_preprocessing

uri='mongodb://mongodbcontainer:27017'

tweets_limit = 100
tweet_lang="english"

#init tweets period
translator = Translator()

def get_tweets(keywords,begin_date,end_date):

    try:
        #
        tweets = query_tweets(keywords, limit = tweets_limit, begindate=begin_date, enddate=end_date, lang = tweet_lang)

        df= pd.DataFrame(t.__dict__ for t in tweets)

        df = tweet_preprocessing(df)

        print("adding sentiment analysis")

        df['sentiment'] = df.text.apply(lambda text: TextBlob(text).sentiment)

        return df

    except:
        
        print("une erreur est survenue")

def load_tweets(keywords,created_at):
    
    try:
        end_date = date.today()

        begin_date = end_date  - timedelta(days=10)

        tweets = get_tweets(keywords,begin_date,end_date)

        print(tweets.head())

        dataframe_to_mongo(tweets,"tweet_bulk","tweetcollection "+created_at)

    except Exception as e:
        
            print("une erreur est suvenue",e)
