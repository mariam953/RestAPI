from flask import Blueprint, Response, request
from bson.objectid import ObjectId
from pymongo import MongoClient
from mymodules.jsonencoder import JSONEncoder

#uri='mongodb://mongodbcontainer:27017'
uri='mongodb://localhost:27017'

client = MongoClient(uri)

db=client.tweet_bulk

tweets = Blueprint('tweets', __name__)

@tweets.route('/tweets')
def get_tweets():
 colls = db.list_collection_names()
 coll = colls[len(colls)-1]
 tweets = db[coll].find({})
 return Response(JSONEncoder().encode([i for i in tweets]), mimetype="application/json", status=200)

@tweets.route('/tweets/<id>')
def get_tweet(id):
    tweet = db.tweetcollection.find_one({"_id": ObjectId(id)})
    print(tweet)
    return Response(JSONEncoder().encode(tweet), mimetype="application/json", status=200)