from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = 'PxfiletfKmIKyZrHxvBPTBmdP'
consumer_secret = 'M5vTz37wzEqrDbvLSHqDGqa7VJdaLLiy9GK1eS9gaxhUQyoOqc'

access_token = '324606030-OE05Hn9vaIruvNcufY2w7ZtwWd3MY5xwKDOuNAfR'
access_token_secret = 'qoQnAl641ISal5ji4IvjWpP1UlHWdnE2RChhcLZBozrW1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    # t = [[]]
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})


#---------------------------------------------------------------------------


