import tweepy

credentials = {"api_key": "bajjVZ8pfi9z8Vo247p3y4fAA", "api_secret": "IFQjPXf1YsbYzOyaeR0mFgmEULMAyOrdvog9Q4EVXJZ3KVGiHb", "access_token": "1216406244358901760-kD4x5rZamNTHVCWElT2DrMqPwUStl2", "access_token_secret": "QDMqyejEwps1l8SyKThZtweEFj6uN6XNuMmMVKdQ9gjbX"}

auth = tweepy.OAuthHandler(credentials["api_key"], credentials["api_secret"])
auth.set_access_token(credentials["access_token"], credentials["access_token_secret"])
api = tweepy.API(auth)

tweet = 'Hello, world!'
api.update_status(status=tweet)