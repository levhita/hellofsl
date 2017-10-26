import tweepy
import ConfigParser

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.user.screen_name +": " + status.text)

api_key         = Config.get("twitter", "api_key")
api_secret      = Config.get("twitter", "api_secret")
access_token    = Config.get("twitter", "access_token")
access_token_secret   = Config.get("twitter", "access_token_secret")

auth = tweepy.OAuthHandler(api_key , api_secret )
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
    
listener = MyStreamListener()
stream = tweepy.Stream(auth, listener)

stream.userstream()
