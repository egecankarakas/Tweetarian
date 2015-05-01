__author__ = 'Egecan-PC'

import json
import sqlite3
import sys

try:
    tweets_data_path = 'tweets.txt'

    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    conn = sqlite3.connect('deneme.db')

    id=0

    c= conn.cursor()
    c.executescript("""
        DROP TABLE IF EXISTS twitter;
        CREATE TABLE twitter(id PRIMARY KEY , created_at , text , user_screen_name, user_location, user_time_zone, lang, favorite_count, retweet_count);
        """)
#    c.execute('CREATE TABLE twitter'
#              ' (created_at , text PRIMARY KEY, user_screen_name, user_location, user_time_zone, lang, favorite_count, retweet_count)')

    conn.commit()

    for line in tweets_file:
        if line.startswith('{'):
            data = json.loads(line)
            userData = data['user']

            id = data['id']
            created_at= data['created_at']
            text = data['text']
            screen_name= userData['screen_name']
            location= userData['location']
            time_zone= userData['time_zone']
            lang= data['lang']
            favorite_count= data['favorite_count']
            retweet_count= data['retweet_count']

#            tuple = (created_at,text,screen_name,location,time_zone,lang,favorite_count,retweet_count)

#             cur.execute("SELECT Name, Price FROM Cars WHERE Id=:Id", {"Id": uId})
#            c.execute("INSERT INTO twitter VALUES (:cre,:text,:scr,:loc,:tim,:lang,:fav,:ret)",({"cre":created_at},{"text":text},{"scr":screen_name},{"loc":location},{"tim":time_zone},{"lang":lang},{"fav":favorite_count},{"ret":retweet_count}))
            c.execute("INSERT INTO twitter VALUES (?,?,?,?,?,?,?,?,?)",(id,created_at,text,screen_name,location,time_zone,lang,favorite_count,retweet_count))
            id+=1
#            c.execute("INSERT INTO twitter VALUES (:cre,:text)",({"cre":created_at},{"text":text}))
            conn.commit()

except sqlite3.Error as e:

    if conn:
        conn.rollback()

    print("Error ?:",(e.args[0]))
    sys.exit(1)

finally:

    if conn:
        conn.close()
