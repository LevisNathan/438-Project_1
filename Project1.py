import flask
from flask import render_template
from random import randint, random
import os

app = flask.Flask(__name__)

import tweepy

def twit():
    consumer_key=  "qOYlXsiQhXjU5LHvF7nWokRCX"
    consumer_secret = "6wkXylgkKs4htvol2MysqJRhzZ900OqYMPhYlLeVJxux4joyWq"
    access_token = "322795723-rYG4Pe1zKl7W245ASt1Pm6dRpVxKyDFX04MOjalv"
    access_token_secret = "qUG4DmGu7TrBam9baVgYdtxS7wGRMASpgqSuFIHkVpUBs"
    callback_url=""
    
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    
    api = tweepy.API(auth)
    #getting tweets and making sure they are only in english
    public_tweets = tweepy.Cursor(api.search, q="Tech -RT", lang = "en").items(50)
    
    randTweet=sorted(public_tweets, key=lambda x:random())
    a = randint(0,50)
    t = randTweet[a]
    return t
# *******************************************************************
import requests
import json

def getty():
    res = {'comp'}
    url =\
    "https://api.gettyimages.com/v3/search/images?fields=id,title,thumb,referral_destinations&sort_order=best&phrase=circuitboards"
    
    my_headers = {
        "Api-Key" : "sdbc5evkwg5a5c2wzamyw9be"
    }
    
    responce = requests.get(url, headers=my_headers)#, params=res)
    json_body = responce.json() # to translate into python
    b = randint(0,25)
    pic= str(json_body["images"][b]["display_sizes"][0]["uri"])
    return pic

# //*****************************************************************

@app.route('/') 
def project():
    pic = getty()
    t = twit()
    print "This is a Debug statement hello"
    return render_template('index.html', tweety = t.text, user = t.user.screen_name, ID= t.id, picture = pic)

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)
