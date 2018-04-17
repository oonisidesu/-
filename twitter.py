import twitter
import tweepy
import time
import sys
from datetime import datetime

auth = twitter.OAuth(consumer_key="",
                     consumer_secret="",
                     token="",
                     token_secret="")

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")
#APIインスタンスを作成
api = tweepy.API(auth)

q = "忍野"
count = 100
search_results = api.search(q=q, count=count)

for result in search_results:
    username = result.user._json['screen_name']
    user_id = result.id #ツイートのstatusオブジェクトから、ツイートidを取得
    print(user_id)
    user = result.user.name #ツイートのstatusオブジェクトから、userオブジェクトを取り出し、名前を取得する
    print(user)
    tweet = result.text
    print(tweet)
    time = result.created_at
    print(time)
    try:
        api.create_favorite(user_id) #ファヴォる
        print(user)
        print("いいね")
        api.create_retweet(user_id)
        print(user)
        print("リツイート")
    except:
        print("ダメです")
    print("##################")

