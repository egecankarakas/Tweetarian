__author__ = 'Egecan-PC'

import json
import sqlite3
import sys

tweetsdataPath = 'tweets.txt'
tweets_data = []
tweets_file = open(tweetsdataPath, "r")
#    conn = sqlite3.connect('deneme.db')

for line in tweets_file:
    if line.startswith('{'):
        rtStatus = None
        data = json.loads(line)
        if(any(key.startswith("retweeted_status") for key in data)):
            for key in data:
                if(key.startswith("retweeted_status")):
                    value = data[key]
                    print(value['text'])
        """
        for key,value in data:
            userData = data['user']
            #rtStatus = data['retweeted_status']

            if(key.startsWith("retweeted_status")):
                print("ahha")
            created_at= data['created_at']
            text = data['text']
            screen_name= userData['screen_name']
            location= userData['location']
            time_zone= userData['time_zone']
            lang= data['lang']
            favorite_count= data['favorite_count']
            retweet_count= data['retweet_count']

            print(id)
        """