__author__ = 'egecan'
import tweepy

consumer_key = "5OYzAxY5fvyALAgAT9Zw"
consumer_secret = "2C8fzswV8BpQLMVbQCjFV5kLQjJU9x3MsrKN7effEpg"
access_token = "306364100-C9gvcTN7Sy4EOGeEwhHnCRyhqck3jc1IBr16mpUY"
access_token_secret = "jdhXcDDqnzVzp5tpc0vRrgZuyk3sWmXrS5uKcOVWIesm3"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

b = api.me()

print(b)