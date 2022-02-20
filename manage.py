import yaml

def new_tweeet(text, api):
    try:
        api.update_status(status=text)
        print( "Successfully tweeted ")
    except:
        print("Unsuccessfull ")
  

def del_tweet(id, api):
    try:
        api.destroy_status(id)
        print("Successfully deleted " , id)
    except:
        print("Unsuccessfull" , id)

def get_tweets(user_id, api, count):
    count = int(input("How many tweets would you like to grab? "))
    for i in range(count):
        tweets = api.user_timeline(screen_name = user_id, count = count, exclude_replies=True, include_rts = False)
    
    grabbed_tweets = {}
    i = 1

    for tweet in tweets:
        j = str("tweet_" + str(i))
        grabbed_tweets[j] = {}
        grabbed_tweets[j]['id'] = tweet.id
        grabbed_tweets[j]['text'] = tweet.text
        grabbed_tweets[j]['name'] = tweet.user.name
        i += 1
    
    with open("Data/grabbed_tweets.yaml", "w") as f:
        f.write(yaml.dump(grabbed_tweets, sort_keys=False, default_flow_style=False))

    print("Tweets saved to Data/grabbed_tweets.yaml")
