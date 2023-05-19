import requests
from requests_oauthlib import OAuth1
import os

consumer_key = os.environ.get("Consumer_Key")
consumer_secret = os.environ.get("Consumer_Secret")
access_token = os.environ.get("Access_Token")
access_token_secret = os.environ.get("Access_Token_Secret")

def random_fact():
    fact = requests.get("https://catfact.ninja/fact?max_length=280").json()
    return fact["fact"]

def format_fact(fact):
   return {"text": "{}".format(fact)}

def connect_to_oauth(consumer_key, consumer_secret, acccess_token, access_token_secret):
   url = "https://api.twitter.com/2/tweets"
   auth = OAuth1(consumer_key, consumer_secret, acccess_token, access_token_secret)
   return url, auth

def hello_pubsub(event, context):
   fact = random_fact()
   payload = format_fact(fact)
   url, auth = connect_to_oauth(
       consumer_key, consumer_secret, access_token, access_token_secret
   )
   request = requests.post(
       auth=auth, url=url, json=payload, headers={"Content-Type": "application/json"}
   )