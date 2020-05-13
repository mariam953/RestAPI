#~movie-bag/app.py
from flask import Flask
from flask_cors import CORS
from resources.tweet import tweets
from resources.trend import trends
from mymodules.TwitterCrawler import init_tweets,load_tweets
from mymodules.TrendsCrawler import load_trends

from mymodules.setInterval import set_interval

# initialize mongodb tweets
#init_tweets()

#get tweets each 3 minutes
interval = 3 # in minutes
load_trends()
load_tweets()
#set_interval(tweets_to_mongo,60*interval)
app = Flask(__name__)
CORS(app)

app.register_blueprint(tweets)
app.register_blueprint(trends)

    
app.run(host='0.0.0.0')   