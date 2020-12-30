import sqlite3
import csv

db = sqlite3.connect('dates.sqlite')
cur = db.cursor()
with open("dates.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rowdate = row['date']
        #print(rowdate)
        rowevent = row['event']
        cur.execute('INSERT INTO dates (date, event) VALUES(?,?)', (rowdate, rowevent))

db.commit()
db.close()
