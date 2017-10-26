import tweepy
import ConfigParser

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.user.screen_name +": " + status.text)

Config = ConfigParser.ConfigParser()
Config.read("config.ini")
auth = tweepy.OAuthHandler(Config.get("twitter", "api_key") , Config.get("twitter", "api_secret") )
auth.set_access_token(Config.get("twitter", "access_token"), Config.get("twitter", "access_token_secret"))

api = tweepy.API(auth)
    
listener = MyStreamListener()
stream = tweepy.Stream(auth, listener)

stream.userstream()
