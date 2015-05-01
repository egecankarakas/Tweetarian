__author__ = 'egecan'
#from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import sqlite3

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key = "SKWLq4C9MJKL0GoIGM3I6gZuk"
consumer_secret = "ak24kY7I91sYE4CyzGguIX7ounQ2nd0pgKNiWFp8ENmWtn8ARu"
access_token = "1882548289-Np1BhoFPYPvYOzVrGzfoSEcXSyP06iQuTtzAVm1"
access_token_secret = "GISgqx1TqcikTEVaKN1ERKWWnASqvndBt0n8G70KYr7aq"

conn = sqlite3.connect('tvShows3.db')

c= conn.cursor()
c.executescript("""
    DROP TABLE IF EXISTS twitter;
    CREATE TABLE twitter(created_at ,id PRIMARY KEY , text, source , lang,
    user_id, user_screen_name, user_location, user_followers_count,
    user_friends_count, user_created_at, user_lang, user_time_zone,
    rt_status_created_at, rt_status_id, rt_status_source,
    rt_status_user_id, rt_status_user_screen_name, rt_status_user_location, rt_status_user_followers_count,
    rt_status_user_friends_count,rt_status_user_created_at, rt_status_user_lang, rt_status_user_time_zone,
    rt_status_retweet_count, rt_status_lang);
    """)

conn.commit()

created_at= None
id = None
text = None
source = None
lang = None

user_id = None
user_screen_name= None
user_location= None
user_followers_count = None
user_friends_count = None
user_created_at = None
user_lang = None
user_time_zone= None

rt_status_created_at = None
rt_status_id = None
rt_status_source = None

rt_status_user_id = None
rt_status_user_screen_name = None
rt_status_user_location = None
rt_status_user_followers_count = None
rt_status_user_friends_count = None
rt_status_user_created_at = None
rt_status_user_lang = None
rt_status_user_time_zone = None

rt_status_retweet_count = None
rt_status_lang = None

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, line):
        created_at= None
        id = None
        text = None
        source = None
        lang = None

        user_id = None
        user_screen_name= None
        user_location= None
        user_followers_count = None
        user_friends_count = None
        user_created_at = None
        user_lang = None
        user_time_zone= None

        rt_status_created_at = None
        rt_status_id = None
        rt_status_source = None

        rt_status_user_id = None
        rt_status_user_screen_name = None
        rt_status_user_location = None
        rt_status_user_followers_count = None
        rt_status_user_friends_count = None
        rt_status_user_created_at = None
        rt_status_user_lang = None
        rt_status_user_time_zone = None

        rt_status_retweet_count = None
        rt_status_lang = None

        rtStatusData = None
        rtStatusUserData = None

        if line.startswith('{'):
            data = json.loads(line)
            userData = data['user']

            created_at= data['created_at']
            id = data['id']
            text = data['text']
            source = data['source']
            lang = data['lang']

            user_id = userData['id']
            user_screen_name = userData['screen_name']
            user_location = userData['location']
            user_followers_count = userData['followers_count']
            user_friends_count = userData['friends_count']
            user_created_at = userData['created_at']
            user_lang = userData['lang']
            user_time_zone= userData['time_zone']

            if(any(key.startswith("retweeted_status") for key in data)):
                rtStatusData = data['retweeted_status']
                rtStatusUserData = rtStatusData['user']

                rt_status_created_at = rtStatusData['created_at']
                rt_status_id = rtStatusData['id']
                rt_status_source = rtStatusData['source']

                rt_status_user_id = rtStatusUserData['id']
                rt_status_user_screen_name = rtStatusUserData['screen_name']
                rt_status_user_location = rtStatusUserData['location']
                rt_status_user_followers_count = rtStatusUserData['followers_count']
                rt_status_user_friends_count = rtStatusUserData['friends_count']
                rt_status_user_created_at = rtStatusUserData['created_at']
                rt_status_user_lang = rtStatusUserData['lang']
                rt_status_user_time_zone = rtStatusUserData['time_zone']

                rt_status_retweet_count = rtStatusData['retweet_count']
                rt_status_lang = rtStatusData['lang']

        c.execute("INSERT INTO twitter VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                  (created_at ,id , text, source , lang,
                    user_id, user_screen_name, user_location, user_followers_count,
                    user_friends_count, user_created_at, user_lang, user_time_zone,
                    rt_status_created_at, rt_status_id, rt_status_source,
                    rt_status_user_id, rt_status_user_screen_name, rt_status_user_location, rt_status_user_followers_count,
                    rt_status_user_friends_count,rt_status_user_created_at, rt_status_user_lang, rt_status_user_time_zone,
                    rt_status_retweet_count, rt_status_lang)
                  )

        conn.commit()
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    aListener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, aListener)
    stream.filter(track=['Medcezir','Kara Ekmek','KaraEkmek','Karagul',"arka sokaklar","arkasokaklar","askinbedeli","askin bedeli"])