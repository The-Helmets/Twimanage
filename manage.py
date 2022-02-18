def new_tweeet(text):
    api.update_status(status = text)

def del_tweet(id):
    api.destroy_status(id)
  



