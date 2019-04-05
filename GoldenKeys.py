# Hayden Riewe
# github.com/hriewe
# hrcyber.tech

# Golden Keys

import tweepy
import json
import sys
from tweepy import OAuthHandler
from twilio.rest import Client


# Set up access keys for twitter/tweepy
consumer_key = ''
consumer_secret = ''

access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Set up access keys for twilio
account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

# Get last 10 tweets from user
tweets = api.user_timeline(screen_name='Borderlands', count = 10, tweet_mode='extended')

tweetList = []
# Phone numbers to notify of new SHiFT keys
userList = ['', '']

for tweet in tweets:
  tweetList.append(tweet.full_text)

# Scan tweets for mention of SHiFT, write matching tweets
# to file to prevent duplicate messages, then text the tweets
# to the numbers in userList using Twilio
for tweet in tweetList:
  if "SHiFT" in tweet:
    with open('shiftcodes.txt', 'r+') as shiftcodes:
      if tweet in shiftcodes.read():
        sys.exit()
      else:
        shiftcodes.write(tweet)
        for number in userList:
          message = client.messages \
            .create(
            body=tweet,
            from_='',
            to=number
            )