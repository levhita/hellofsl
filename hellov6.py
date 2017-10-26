import tweepy

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.user.screen_name +": " + status.text)

auth = tweepy.OAuthHandler("s1HpYlsrGRldf5fJoqYw2KWTT", "NPs562OojeHXHmlDGK1FXCemrrYGnKe2WIJ8yk4eiZYaVnoJ9A")
auth.set_access_token("20459504-JsDzcDlUc0mLVLdQCqjYJEXI1RESZ1RuIYRHoy2Ni", "oZGCKJHe6IKgEPkmxdv5d2YbYkiGIe5akwtLTiYGGSbzm")

api = tweepy.API(auth)
    
listener = MyStreamListener()
stream = tweepy.Stream(auth, listener)

stream.userstream()
