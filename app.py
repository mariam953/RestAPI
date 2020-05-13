from flask import Flask
from flask_cors import CORS
from resources.tweet import tweets
from resources.trend import trends

import threading
from datetime import datetime,date,timedelta
import time

from mymodules.TwitterCrawler import load_tweets
from mymodules.TrendsCrawler import load_trends

interval = 10*60 # in minutes

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def load():
    current_timestamp = time.time()        
    created_at = datetime.fromtimestamp(current_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    popular_topic = load_trends(created_at)
    print("===========================================popular topic :",popular_topic)
    load_tweets(popular_topic,created_at)


set_interval(load,interval)

app = Flask(__name__)
CORS(app)

app.register_blueprint(tweets)
app.register_blueprint(trends)


    
app.run(host='0.0.0.0')   