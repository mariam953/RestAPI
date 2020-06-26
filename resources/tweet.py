from flask import Blueprint, Response, request
from bson.objectid import ObjectId
from pymongo import MongoClient
from mymodules.jsonencoder import JSONEncoder

uri='mongodb://mongodbcontainer:27017'

client = MongoClient(uri)

db=client.tweet_bulk

tweets = Blueprint('tweets', __name__)
tweet_collection = 'tweetcollection '

@tweets.route('/tweets/')
@tweets.route('/tweets/<date>')
def get_tweets(date=None):
    if date is None :
        colls = db.list_collection_names()
        coll = colls[len(colls)-1]
    else:
        coll = tweet_collection+date.replace('%20',' ')
        print("col is "+coll)
    tweets = db[coll].find({})
    return Response(JSONEncoder().encode([i for i in tweets]), mimetype="application/json", status=200)

@tweets.route('/tweets/<id>')
def get_tweet(id):
    tweet = db.tweetcollection.find_one({"_id": ObjectId(id)})
    print(tweet)
    return Response(JSONEncoder().encode(tweet), mimetype="application/json", status=200)

@tweets.route('/tweets/historic')
def get_tweets_historic():
    colls = db.list_collection_names()
    return Response(JSONEncoder().encode([i.replace("tweetcollection ","") for i in colls]), mimetype="application/json", status=200)