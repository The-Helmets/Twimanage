import tweepy

consumer_key = "QS9Vk6mSmKTri97Oz4yNuY3sH"
consumer_secret = "szyiAlz9d0i5PmGEEEkukeyReDYHrFEgaMW2kTkytaqI1W2lH0"
access_token = "1216406244358901760-m4oWrplywn1qx35Tr9dggLhQMq0ABZ"
access_token_secret = "Srgnz57Kwda6gQie9iJFb3VuDVYSmj75shqwHsBPhQygu"

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

print(api.verify_credentials().screen_name)

#tweet = 'Hello, world!'
#api.update_status(status=tweet)