from twitterscraper import query_tweets
import pymongo
import pandas as pd
import json
from datetime import datetime,date,timedelta
import time

#uri='mongodb://mongodbcontainer:27017'
uri='mongodb://localhost:27017'

tweets_limit = 1000
tweet_lang="english"
#init tweets period
end_date = date.today()
begin_date = end_date - timedelta(days=5)

def get_tweets(keywords,begin_date,end_date):

    tweets = query_tweets(keywords, limit = tweets_limit, begindate=begin_date, enddate=end_date, lang = tweet_lang)

    df= pd.DataFrame(t.__dict__ for t in tweets)

    return df

def save_to_mongo(dataframe,database,collection):
    try:
        db = pymongo.MongoClient(uri)[database]
        
        items = json.loads(dataframe.T.to_json()).values()
        
        db[collection].insert_many(items)
        
        db[collection].count_documents({})        
                
    except Exception as e:
            print(e)

#tweets = get_tweets()

#print("auto execute")

#save_to_mongo(tweets,"tweet_bulk","tweetcollection"+end_date.strftime("%Y-%m-%d"))


def tweets_to_mongo():
    
    try:
        keywords="covid"

        tweets = get_tweets(keywords,begin_date,end_date)

        #end_date_string = end_date.strftime("%Y-%m-%d")

        print(tweets.head())
        current_timestamp = time.time()
        st = datetime.fromtimestamp(current_timestamp).strftime('%Y-%m-%d %H:%M:%S')

        save_to_mongo(tweets,"tweet_bulk","tweetcollection "+st)

        save_to_mongo(pd.DataFrame(data={"batch":"batch "+st,"items_number":tweets.size,"started_at":st,"status":"succeed"}, index=[0]),"batch","tweets_batch")
    except Exception as e:
            print(e)

def init_tweets():
    
    try:
        keywords="covid"

        tweets = get_tweets(keywords,begin_date,end_date)

        print(tweets.head())

        current_timestamp = time.time()
        st = datetime.fromtimestamp(current_timestamp).strftime('%Y-%m-%d %H:%M:%S')

        save_to_mongo(tweets,"tweet_bulk","tweetcollection "+st)

        save_to_mongo(pd.DataFrame(data={"batch":"batch "+st,"items_number":tweets.size,"started_at":st,"status":"succeed"}, index=[0]),"batch","tweets_batch")
    except Exception as e:
            print(e)

def load_tweets():
    
    try:
        keywords="covid"

        begin_date = end_date  - timedelta(days=1)

        tweets = get_tweets(keywords,begin_date,end_date)

        print(tweets.head())

        current_timestamp = time.time()
        st = datetime.fromtimestamp(current_timestamp).strftime('%Y-%m-%d %H:%M:%S')

        save_to_mongo(tweets,"tweet_bulk","tweetcollection "+st)

        save_to_mongo(pd.DataFrame(data={"batch":"batch "+st,"items_number":tweets.size,"started_at":st,"status":"succeed"}, index=[0]),"batch","tweets_batch")
    except Exception as e:
            print(e)
