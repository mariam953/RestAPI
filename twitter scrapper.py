from apscheduler.scheduler import Scheduler

from twitterscraper import query_tweets
import pymongo
import pandas as pd
import json
from datetime import date,timedelta

uri='mongodb://localhost:27017'
tweets_limit = 1000
tweet_lang="english"
end_date = date.today()
begin_date = end_date - timedelta(days=5)

sched = Scheduler()
sched.start()


def get_tweets():

    tweets = query_tweets("covid", limit = tweets_limit, begindate=begin_date, enddate=end_date, lang = tweet_lang)

    #data = pd.read_json(r"D:\Desktop\New folder\v3\tweets.json") 
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

tweets = get_tweets()

print("auto execute")

save_to_mongo(tweets,"tweet_bulk","tweetcollection"+end_date.strftime("%Y-%m-%d"))

def some_job():
    print("executeeeeeeeeeeeeeee")
sched.add_interval_job(some_job, seconds = 10)
