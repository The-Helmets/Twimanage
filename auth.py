def auth():
    import tweepy

    consumer_key = "QS9Vk6mSmKTri97Oz4yNuY3sH"
    consumer_secret = "szyiAlz9d0i5PmGEEEkukeyReDYHrFEgaMW2kTkytaqI1W2lH0"
    callback= "oob"

    oauth1_user_handler = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret,
        callback)

    print("Visit this link to generate 6-digit PIN: ", oauth1_user_handler.get_authorization_url(access_type='write'))

    verifier = input("Input PIN: ")
    access_token, access_token_secret = oauth1_user_handler.get_access_token(verifier)

    with open("credentials.yaml", "w") as f:
        f.write("access_token: {}\n".format(access_token))
        f.write("access_token_secret: {}\n".format(access_token_secret))

    api = tweepy.API(oauth1_user_handler)

    print("Signed in as: ", api.verify_credentials().screen_name)

    return api