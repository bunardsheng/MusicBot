# import requests
# from requests_oauthlib import OAuth1
import os
import random
from random import shuffle

consumer_key = os.environ.get("Consumer_Key")
consumer_secret = os.environ.get("Consumer_Secret")
access_token = os.environ.get("Access_Token")
access_token_secret = os.environ.get("Access_Token_Secret")

def get_songs():
    songs = [
        "Sibelius Violin Concerto",
        "Tchaikovsky Violin Concerto",
        "Bach Chaconne",
        "Brahms Sonata No. 1",
        "Waxman Carmen Fantasie",
        "Symphony No. 5 in E Minor"
    ]
    return songs

def get_tweets():
    tweets = [
    "What should I listen to today? How about ",
    "I'm bored, maybe I'll pick up ",
    "Check this out! ",
    "I feel like listening to: ",
    "What's up y'all! I love music, today I'm listening to: ",
    ]   
    return tweets

def random_song():
    # trending = requests.get("https://openlibrary.org/trending/daily.json").json()
    songs = get_songs()
    song = songs[random.randint(0, len(songs))]
    return song

def format_song(song, comments):
   shuffle(comments)
   return {"text": "{title}{tweet}".format(tweet = song, title = comments[random.randint(0, len(comments) - 1)])}


def connect_to_oauth(consumer_key, consumer_secret, acccess_token, access_token_secret):
   url = "https://api.twitter.com/2/tweets"
#    auth = OAuth1(consumer_key, consumer_secret, acccess_token, access_token_secret)
   return url, auth

def hello_pubsub(event, context):
   song = random_song()
   tweets = get_tweets()
   payload = format_song(song, tweets)
   
   url, auth = connect_to_oauth(
       consumer_key, consumer_secret, access_token, access_token_secret
   )
#    request = requests.post(
#     #    auth=auth, url=url, json=payload, headers={"Content-Type": "application/json"}
#    )


def run():
    song = random_song()
    tweets = get_tweets()
    payload = format_song(song, tweets)
    print(payload)

run()