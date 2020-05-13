from twitterscraper import query_tweets
import pymongo
import pandas as pd
import json
from datetime import datetime,date,timedelta
import time
from textblob import TextBlob
from googletrans import Translator
import re
from mymodules.mongodb import dataframe_to_mongo

uri='mongodb://localhost:27017'

tweets_limit = 100
tweet_lang="english"

#init tweets period
end_date = date.today()
begin_date = end_date - timedelta(days=1)
translator = Translator()

def get_tweets(keywords,begin_date,end_date):

    try:

        tweets = query_tweets(keywords, limit = tweets_limit, begindate=begin_date, enddate=end_date, lang = tweet_lang)

        df= pd.DataFrame(t.__dict__ for t in tweets)

        print("before removinf duplicate :",df.size)

        df.drop_duplicates(subset ="tweet_id",keep = False, inplace = True)

        print("after removing duplicate :",df.size)

        print("adding sentiment analysis")

        df['text'] = df.text.apply(lambda text:  re.sub(r"http\S+", "", text))

        df['text'] = df.text.apply(lambda text:  translator.translate(text).text)
        
        df['sentiment'] = df.text.apply(lambda text: TextBlob(text).sentiment)

        return df

    except:
        
        print("une erreur est survenue")

def load_tweets(keywords,created_at):
    
    try:

        begin_date = end_date  - timedelta(days=1)

        tweets = get_tweets(keywords,begin_date,end_date)

        print(tweets.head())

        dataframe_to_mongo(tweets,"tweet_bulk","tweetcollection "+created_at)

    except Exception as e:
        
            print("une erreur est suvenue",e)
