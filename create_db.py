#!/usr/bin/python

import sqlite3


conn = sqlite3.connect('noddus.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE PERSON
         (ID     INTEGER  PRIMARY KEY AUTOINCREMENT,
         NAME    TEXT     NOT NULL,
         AGE     INT      NOT NULL,
         CREATED DATETIME DEFAULT CURRENT_TIMESTAMP);''')

print("Table created successfully")

conn.close()
print("Closed database successfully")
