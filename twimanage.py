import tweepy
import yaml

from auth import *
from manage import *


print("Welcome to Twimanage! This is a simple Twitter management tool. /n")

# Load credentials and authenticate
try:
    api = auth()
    print("Authentication successful!")

except:
    print("Authentication failed! Please check your credentials.yaml file.")
    exit()

user_choice = (int(input("1. New Tweet\n2. Delete Tweet(Needs Tweed ID)\n3. Quit\n>>>")))
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