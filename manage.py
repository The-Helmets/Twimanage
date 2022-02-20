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

def get_tweets(username, api):
        tweets = api.user_timeline(username)
        tmp=[] 
  
        tweets_for_csv = [tweet.text for tweet in tweets]  
        for x in tweets_for_csv:
            tmp.append(x) 
            print(tmp)
