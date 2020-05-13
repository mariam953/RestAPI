from flask import Blueprint, Response, request
from bson.objectid import ObjectId
from pymongo import MongoClient
from mymodules.jsonencoder import JSONEncoder

#uri='mongodb://mongodbcontainer:27017'
uri='mongodb://localhost:27017'

client = MongoClient(uri)

db=client.trend_bulk

trends = Blueprint('trends', __name__)
trendcollection = "trendcollection "

@trends.route('/trends/')
@trends.route('/trends/<date>')
def get_trends(date=None):
    if date is None :
        colls = db.list_collection_names()
        coll = colls[len(colls)-1]
    else:
        coll = trendcollection+date
        print("col is "+coll)
    trends = db[coll].find({})
    return Response(JSONEncoder().encode([i for i in trends]), mimetype="application/json", status=200)

@trends.route('/trends/<id>')
def get_trend(id):
    trend = db.trendcollection.find_one({"_id": ObjectId(id)})
    print(trend)
    return Response(JSONEncoder().encode(trend), mimetype="application/json", status=200)