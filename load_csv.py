#!/usr/bin/python

import csv
import sqlite3
import sys


filename = None

if len(sys.argv)==2:
    filename = sys.argv[1]
    print('File name to import :: {}'.format(filename))
else:
    print('No file name provided or invalid input. Please run "./load_csv.py <csv-filename>"')
    sys.exit()


def read_csv(filename):
    try:
        with open(filename) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                yield line['name'], line['age']
    except IOError:
        raise IOError('{} filename not found!!'.format(filename))


conn = sqlite3.connect('noddus.db')
print("Opened database successfully")

#Not using string formatting here to avoid https://xkcd.com/327/ :)
query = "INSERT INTO PERSON(NAME, AGE) VALUES(?, ?)"

lines_inserted = 0
for data in read_csv(filename):
    cur = conn.execute(query, (data))
    lines_inserted += 1

conn.commit()

cursor = conn.execute('SELECT count(*) from PERSON')
total_records = cursor.fetchone()[0]

conn.close()
print("Closed database successfully")

print("{} records inserted, total records are {}.".format(lines_inserted, total_records))
