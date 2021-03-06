import tweepy
import schedule
import time
from datetime import datetime
import random
from quotes import quotesList, morningList, nightList
import os
from os import environ
import pytz
from pytz import timezone

print("Like script starting...")
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)



def likeCheck():
        search = ['Haru Okumura', "persona 5 haru", "makoto nijima", "persona 5 makoto"]
        nrTweets = 100
            
        for tweet in tweepy.Cursor(api.search, random.choice(search)).items(nrTweets):
            try:
                tweet.favorite()
                print('Recent tweet was liked!')
            except tweepy.TweepError as e:
                print(e.reason)
                print(tweet.text)
            except StopIteration:
                break
            break
def selfLike():
        nrTweets = 100
        for tweet in tweepy.Cursor(api.user_timeline).items(nrTweets):
            try:
                tweet.favorite()
                print('Timeline tweet was liked!')
            except tweepy.TweepError as e:
                print(e.reason)
                print(tweet.text)
            except StopIteration:
                break
            break
print("Passed 'haruLike.py'")