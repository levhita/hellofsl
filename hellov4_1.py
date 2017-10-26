import tweepy

auth = tweepy.OAuthHandler("s1HpYlsrGRldf5fJoqYw2KWTT", "NPs562OojeHXHmlDGK1FXCemrrYGnKe2WIJ8yk4eiZYaVnoJ9A")
auth.set_access_token("20459504-JsDzcDlUc0mLVLdQCqjYJEXI1RESZ1RuIYRHoy2Ni", "oZGCKJHe6IKgEPkmxdv5d2YbYkiGIe5akwtLTiYGGSbzm")

api = tweepy.API(auth)

api.update_status('Enviado desde el @FSLMx')
