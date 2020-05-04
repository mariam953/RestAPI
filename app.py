#~movie-bag/app.py
from flask import Flask
from resources.tweet import tweets
from mymodules.TwitterCrawler import init_tweets,load_tweets
from mymodules.setInterval import set_interval

# initialize mongodb tweets
#init_tweets()

#get tweets each 3 minutes
interval = 3 # in minutes
load_tweets()
#set_interval(tweets_to_mongo,60*interval)
app = Flask(__name__)

app.register_blueprint(tweets)

    
app.run(host='0.0.0.0')   