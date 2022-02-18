def new_tweeet(text, api):
    api.update_status(status = text)

def del_tweet(id, api):
    api.destroy_status(id)
  