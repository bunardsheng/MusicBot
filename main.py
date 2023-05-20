import requests
from requests_oauthlib import OAuth1
import os
import random
from random import shuffle

consumer_key = os.environ.get("Consumer_Key")
consumer_secret = os.environ.get("Consumer_Secret")
access_token = os.environ.get("Access_Token")
access_token_secret = os.environ.get("Access_Token_Secret")

def get_tweets():
    tweets = [
    "What should I read today? How about ",
    "I'm bored, maybe I'll pick up ",
    "Check this out! " 
    ]   
    return tweets

def random_book():
    trending = requests.get("https://openlibrary.org/trending/daily.json").json()
    books = trending["works"]
    book_title_auth = []

    for book in books:
        author = book.get("author_name", [None])[0]
        if not author: author = "oops there's no author"
        book_title_auth.append([book["title"], author])
    
    length = len(book_title_auth) - 1
    num = random.randint(0, length)

    return book_title_auth[num]

def format_book(book, comments):
   shuffle(comments)
   return {"text": "{tweet}{title} by {author}".format(tweet = comments[0], title = book[0], author = book[1])}


def connect_to_oauth(consumer_key, consumer_secret, acccess_token, access_token_secret):
   url = "https://api.twitter.com/2/tweets"
   auth = OAuth1(consumer_key, consumer_secret, acccess_token, access_token_secret)
   return url, auth

def hello_pubsub(event, context):
   book = random_book()
   tweets = get_tweets()
   payload = format_book(book, tweets)
   
   url, auth = connect_to_oauth(
       consumer_key, consumer_secret, access_token, access_token_secret
   )
   request = requests.post(
       auth=auth, url=url, json=payload, headers={"Content-Type": "application/json"}
   )

