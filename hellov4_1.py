import tweepy
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("config.ini")
auth = tweepy.OAuthHandler(Config.get("twitter", "api_key") , Config.get("twitter", "api_secret") )
auth.set_access_token(Config.get("twitter", "access_token"), Config.get("twitter", "access_token_secret"))

auth = tweepy.OAuthHandler(api_key , api_secret )
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status('Enviado desde el @FSLMx')
