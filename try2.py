import time

__author__ = 'egecan'
import tweepy

consumer_key = "5OYzAxY5fvyALAgAT9Zw"
consumer_secret = "2C8fzswV8BpQLMVbQCjFV5kLQjJU9x3MsrKN7effEpg"
access_token = "306364100-C9gvcTN7Sy4EOGeEwhHnCRyhqck3jc1IBr16mpUY"
access_token_secret = "jdhXcDDqnzVzp5tpc0vRrgZuyk3sWmXrS5uKcOVWIesm3"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

ids = []
userid = "egecankarakas"

cursor = tweepy.Cursor(api.followers_ids, screen_name=userid)
for page in cursor.pages():
    ids.extend(page)
    time.sleep(1)



print(len(ids), "following have been gathered from", userid)

users = []

#def lookupUsers(userid):
#    userids = [userid]
#    users.extend(api.lookup_users(user_ids=userids))


#for x in range(0,len(ids)):
#    subid = ids[x]
#    print(x)
#    lookupUsers(subid)
#    time.sleep(1)


users = api.lookup_users(user_ids=ids)  # ieterates through the list of users and prints them
for u in users:
    print(u.screen_name)