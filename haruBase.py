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

print("Running!")
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# define date format
global fmtS
fmtS = '%H:%M:%S'
# define eastern timezone
global eastern
eastern = timezone('US/Eastern')
# localized datetime
global loc_dt
loc_dt = datetime.now(eastern)
global currentTime
currentTime = loc_dt.strftime(fmtS)
print("Local time: Started at " + loc_dt.strftime(fmtS))
global fmt
fmt = '%H:%M'
global currentTimeSansSeconds
currentTimeSansSeconds = loc_dt.strftime(fmt)


global bedtime
bedtime = False #change to false

def timeLoop():
    def clock():
        global loc_dt
        loc_dt = datetime.now(eastern)
        global bedtime
        global currentTime
        currentTime = loc_dt.strftime(fmtS)
        global currentTimeSansSeconds
        currentTimeSansSeconds = loc_dt.strftime(fmt)
        print("Time set to " + currentTime)

    def quotesExecute():
        if bedtime == False:
            lastQuote = ""
            currentQuote = random.choice(quotesList)
            if currentQuote == lastQuote:
                #reroll quote
                currentQuote = random.choice(quotesList)
            else:
                #execute posting quote
                print(currentQuote)
                api.update_status(currentQuote)
                lastQuote = currentQuote
        else:
            print("Haru is sleeping...")
    schedule.every(60).minutes.do(quotesExecute)
    schedule.every(30).seconds.do(clock)
    def morningExecute():
        global bedtime
        if bedtime == True:
            print(random.choice(morningList))
            api.update_status(random.choice(morningList))
            bedtime = False
            print("Bedtime is set to " + str(bedtime))
            time.sleep(60)
        else:
            print("Error: Bedtime is already set to false.")
            print(str(bedtime))
            time.sleep(60)

    def nightExecute():
        global bedtime
        if bedtime == False:
            print(random.choice(nightList))
            api.update_status(random.choice(nightList))
            bedtime = True
            print("Bedtime is set to " + str(bedtime))
            time.sleep(60)
        else:
            print("Error: Bedtime is already set to true.")
            print(str(bedtime))
            time.sleep(60)

    while True:
        global currentTimeSansSeconds
        if currentTimeSansSeconds == "09:00": morningExecute() #set to 7
        elif currentTimeSansSeconds == "00:00": nightExecute()
    # Checks whether a scheduled task
    # is pending to run or not
        schedule.run_pending()
        time.sleep(1)

timeLoop()



