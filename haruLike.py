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
        search = 'Haru Okumura'
        nrTweets = 50

        for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
            try:
                print('Recent tweet was liked!')
                tweet.favorite()
                time.sleep(70)
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

        for tweet in tweepy.Cursor(api.friends).items(nrTweets):
            try:
                print('Friend tweet was liked!')
                tweet.favorite()
                time.sleep(420)
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break