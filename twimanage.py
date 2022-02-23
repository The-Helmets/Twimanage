from itertools import count
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
    user_name = api.verify_credentials().screen_name
    user_id = api.verify_credentials().id_str
    print("Signed in as: ", user_name, " User ID: ", user_id)
    
except:
    if input("Credentials not found. Do you want to sign in us3ing 3 PIN Authentication? (y/n): ") == "y":
        api, user_name, user_id = auth()
        print("3 PIN Authentication successful!")
        print(user_name)
    else:
        print("Authentication failed! Please check your credentials.yaml file.")
        exit()

# Main menu
while True:
    user_choice = (int(input("What would you like to do?\n1. New Tweet\n2. Get Tweets\n3. Delete Tweets\n4. Quit\n>>>")))
    if user_choice == 1:
        tweet = input("What would you like to tweet? ")
        new_tweeet(tweet, api)
        print("Tweet sent!")

    elif user_choice == 2:
        get_tweets(user_name, api, count)

    elif user_choice == 3:
        del_tweet(api)

    elif user_choice == 4:
        print("Goodbye!")
        exit()