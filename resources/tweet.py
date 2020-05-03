from flask import Blueprint, Response, request
from bson.objectid import ObjectId
from pymongo import MongoClient
from mymodules.jsonencoder import JSONEncoder

client = MongoClient('localhost:27017')

db=client.teetdbbilal

tweets = Blueprint('tweets', __name__)

@tweets.route('/tweets')
def get_tweets():
 tweets = db.tweetcollection.find({})
 print(tweets)
 return Response(JSONEncoder().encode([i for i in tweets]), mimetype="application/json", status=200)

@tweets.route('/tweets/<id>')
def get_tweet(id):
    tweet = db.tweetcollection.find_one({"_id": ObjectId(id)})
    print(tweet)
    return Response(JSONEncoder().encode(tweet), mimetype="application/json", status=200)