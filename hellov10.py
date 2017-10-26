import tweepy
from pprint import pprint

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
                        
lyrics = [line.rstrip('\n') for line in open("despacito.txt")]
length = len(lyrics)
counter = 0

auth = tweepy.OAuthHandler("s1HpYlsrGRldf5fJoqYw2KWTT", "NPs562OojeHXHmlDGK1FXCemrrYGnKe2WIJ8yk4eiZYaVnoJ9A")
auth.set_access_token("20459504-JsDzcDlUc0mLVLdQCqjYJEXI1RESZ1RuIYRHoy2Ni", "oZGCKJHe6IKgEPkmxdv5d2YbYkiGIe5akwtLTiYGGSbzm")

api = tweepy.API(auth)
    
listener = MyStreamListener()
stream = tweepy.Stream(auth, listener)

stream.userstream()   
