from twitter_stream import TwitterStreamListener
import tweepy
from twitter_cred import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

ts = TwitterStreamListener()
stream = tweepy.Stream(auth = api.auth, listener=ts)

stream.filter(track=['@DucreuxFancy'])