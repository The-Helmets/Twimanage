import tweepy
import yaml

from auth import *
from manage import *


print("Welcome to Twimanage! This is a simple Twitter management tool.")

with open("credentials.yaml", "r") as f:
    credentials = yaml.safe_load(f)

# Load credentials and authenticate
try:
    auth_1 = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
    auth_1.set_access_token(credentials['access_token'], credentials['access_token_secret'])
    api = tweepy.API(auth_1)
    print("Authentication successful!")
    
except:
    if input("Credentials not found. Do you want to sign in using 3 PIN Authentication? (y/n): ") == "y":
        api = auth()
        print("3 PIN Authentication successful!")
    else:
        print("Authentication failed! Please check your credentials.yaml file.")
        exit()

while True:
    user_choice = (int(input("What would you like to do?\n1. New Tweet\n2. Delete Tweet(Needs Tweet ID)\n3. Quit\n>>>")))
    if user_choice == 1:
        tweet = input("What would you like to tweet? ")
        new_tweeet(tweet, api)
        print("Tweet sent!")

    elif user_choice == 2:
        id = input("What is the ID of the tweet you want to delete? ")
        del_tweet(id, api)
        print("Tweet deleted!")

    elif user_choice == 3:
        print("Goodbye!")
        exit()