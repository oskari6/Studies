# This application will read the mailbox data (mbox.txt) 
# and count the number of email messages per organization 
# (i.e. domain name of the email address) using a database 
# with the following schema to maintain the counts.

import sqlite3

conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

filename = input("Enter filename: ")
if(len(filename) < 1): 
    filename = "mbox.txt"

handle = open(filename)

for line in handle:
    if not line.startswith("From: "): 
        continue
    pieces = line.split()
    org = pieces[1]
    pieces2 = org.split("@")
    org2 = pieces2[1]

    cur.execute("SELECT count FROM Counts WHERE org = ? ", (org2,))
    row = cur.fetchone()

    if row is None:
        cur.execute("INSERT INTO Counts (org, count) VALUES (? ,1)", (org2,))
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (org2,))

conn.commit()

sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
