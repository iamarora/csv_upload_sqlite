#!/usr/bin/python

import sqlite3


conn = sqlite3.connect('noddus.db')
print("Opened database successfully")

cursor = conn.execute('SELECT ID, NAME, AGE, CREATED FROM PERSON order by ID desc limit 10')
print cursor
for row in cursor:
    print("ID={} NAME={} AGE={} CREATED={}".format(row[0], row[1], row[2], row[3]))

conn.close()
print("Closed database successfully")
