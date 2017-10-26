import tweepy
import ConfigParser
from pprint import pprint
import requests.packages.urllib3
import sys
#import time

class MyStreamListener(tweepy.StreamListener):
 
    def on_direct_message(self, status):
        global counter, lyrics, say_hello_to       
        from_screen_name = status._json['direct_message']['sender']['screen_name']
        if from_screen_name == say_hello_to:
            #time.sleep(5)
            api.send_direct_message(screen_name=say_hello_to, text=lyrics[counter])
            print lyrics[counter]
            if counter < length-1:
                counter += 1
            else:
                print "Finished"
                exit(0)

if __name__ == '__main__':
    Config = ConfigParser.ConfigParser()
    Config.read("config.ini")
    requests.packages.urllib3.disable_warnings()
    
    say_hello_to    = sys.argv[1]
    songfile        = sys.argv[2]
    
    lyrics = [line.rstrip('\n') for line in open(songfile)]
    length = len(lyrics)
    counter = 0

    api_key         = Config.get("twitter", "api_key")
    api_secret      = Config.get("twitter", "api_secret")
    access_token    = Config.get("twitter", "access_token")
    access_token_secret   = Config.get("twitter", "access_token_secret")

    auth = tweepy.OAuthHandler(api_key , api_secret )
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
        
    listener = MyStreamListener()
    stream = tweepy.Stream(auth, listener)

    print lyrics[counter]
    api.send_direct_message(screen_name=say_hello_to, text=lyrics[counter])
    counter += 1

    stream.userstream()   
