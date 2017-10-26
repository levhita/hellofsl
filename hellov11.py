import tweepy
import ConfigParser
from pprint import pprint
import requests.packages.urllib3

class MyStreamListener(tweepy.StreamListener):
 
    def on_direct_message(self, status):
        global counter, lyrics        
        from_screen_name = status._json['direct_message']['sender']['screen_name']
        if from_screen_name == "atihvel":
            api.send_direct_message(screen_name=from_screen_name, text=lyrics[counter])
            print lyrics[counter]
            if counter < length-1:
                counter += 1
            else:
                print "Finished"
                exit(0)

requests.packages.urllib3.disable_warnings()                        

lyrics = [line.rstrip('\n') for line in open("despacito.txt")]
length = len(lyrics)
counter = 0

Config = ConfigParser.ConfigParser()
Config.read("config.ini")
auth = tweepy.OAuthHandler(Config.get("twitter", "api_key") , Config.get("twitter", "api_secret") )
auth.set_access_token(Config.get("twitter", "access_token"), Config.get("twitter", "access_token_secret"))

api = tweepy.API(auth)
    
listener = MyStreamListener()
stream = tweepy.Stream(auth, listener)

print lyrics[counter]
api.send_direct_message(screen_name="atihvel", text=lyrics[counter])
counter += 1

stream.userstream()   
