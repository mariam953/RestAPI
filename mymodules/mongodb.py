import pymongo
import pandas as pd
import json

uri='mongodb://mongodbcontainer:27017'

def dataframe_to_mongo(dataframe,database,collection):
    try:
        db = pymongo.MongoClient(uri)[database]
        
        items = json.loads(dataframe.T.to_json()).values()
        
        db[collection].insert_many(items)
        
        count = db[collection].count_documents({})

        print("Saved =",count)
                
    except Exception as e:
            print(e)