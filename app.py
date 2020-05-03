#~movie-bag/app.py

from flask import Flask
from resources.tweet import tweets

app = Flask(__name__)

app.register_blueprint(tweets)

app.run()