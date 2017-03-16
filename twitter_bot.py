import tweepy
import requests
import os
from twitter_cred import *


def tweet(sent):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    if len(sent) <= 119:
        api.update_status(status=sent)
    else:
        tweets = []
        for i in range(1,int(len(sent)/119)+2):
            counter = (" ({}/{})".format(i, int(len(sent)/119)+1))
            tweets.append(sent[(i-1)*119:i*119] + counter)
        [api.update_status(status=t) for t in tweets]

def tweet_image(url, message):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")

def make_tweet(original, fancy):
    fancy = fancy.split()
    part1 = fancy[:7]
    part2 = fancy[7:]
    part1 = " ".join(str(x) for x in part1)
    part2 = " ".join(str(x) for x in part2)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    url = "https://api.imgflip.com/caption_image"

    payload = "template_id=61535&username=ralladez&password=password&text0=" + part1 + "&text1=" + part2
    headers = {
        'content-type': "application/x-www-form-urlencoded",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    imgflipjson = response.json()
    url = imgflipjson["data"]["url"]


    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)
    else:
        print("Unable to download image")


    if len(original) <= 135:
        api.update_with_media(filename, status=original)
    else:
        tweets = []
        for i in range(1,int(len(original)/134)+2):
            counter = (" ({}/{})".format(i, int(len(original)/134)+1))
            tweets.append(original[(i-1)*134:i*134] + counter)
        [api.update_with_media(filename, status=t) for t in tweets]

    os.remove(filename)