import tweepy
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("config.ini")
auth = tweepy.OAuthHandler(Config.get("twitter", "api_key") , Config.get("twitter", "api_secret") )
auth.set_access_token(Config.get("twitter", "access_token"), Config.get("twitter", "access_token_secret"))

api = tweepy.API(auth)

public_tweets = api.user_timeline("fslmx")
for tweet in public_tweets:
    print tweet.text
