__author__ = 'Egecan-PC'

import sqlite3

conn = None
conn = sqlite3.connect('twitter.db')

cur = conn.cursor()

t=cur.execute('SELECT text from twitter3 WHERE created_at LIKE "Thu Apr 16%" ')
for row in t.fetchall():
    print(row)
