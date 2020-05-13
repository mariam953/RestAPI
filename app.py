#~movie-bag/app.py
from flask import Flask
from flask_cors import CORS
from resources.tweet import tweets
from resources.trend import trends
from mymodules.TwitterCrawler import init_tweets,load_tweets
from mymodules.TrendsCrawler import load_trends
import threading
from mymodules.setInterval import set_interval

# initialize mongodb tweets
interval = 10*60 # in minutes

#init_tweets()
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def load():
    print("wlaila khedama")
    load_trends()
    load_tweets()


set_interval(load,interval)
#get tweets each 3 minutes
#set_interval(tweets_to_mongo,60*interval)
app = Flask(__name__)
CORS(app)

app.register_blueprint(tweets)
app.register_blueprint(trends)

    
app.run(host='0.0.0.0')   