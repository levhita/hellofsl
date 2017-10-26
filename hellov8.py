import tweepy

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.user.screen_name +": " + status.text)


#lyrics = []
songfile = open("despacito.txt")
for line in songfile:
    print line#.rstrip('\n')
    #lyrics.append(line.rstrip('\n'))

#print len(lyrics)

#for line in lyrics:
#    print line

#auth = tweepy.OAuthHandler("s1HpYlsrGRldf5fJoqYw2KWTT", "NPs562OojeHXHmlDGK1FXCemrrYGnKe2WIJ8yk4eiZYaVnoJ9A")
#auth.set_access_token("20459504-JsDzcDlUc0mLVLdQCqjYJEXI1RESZ1RuIYRHoy2Ni", "oZGCKJHe6IKgEPkmxdv5d2YbYkiGIe5akwtLTiYGGSbzm")

#api = tweepy.API(auth)
    
#listener = MyStreamListener()
#stream = tweepy.Stream(auth, listener)

#stream.userstream()   

