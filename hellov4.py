import tweepy
import ConfigParser

api_key         = Config.get("twitter", "api_key")
api_secret      = Config.get("twitter", "api_secret")
access_token    = Config.get("twitter", "access_token")
access_token_secret   = Config.get("twitter", "access_token_secret")

auth = tweepy.OAuthHandler(api_key , api_secret )
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.user_timeline("fslmx")
for tweet in public_tweets:
    print tweet.text
