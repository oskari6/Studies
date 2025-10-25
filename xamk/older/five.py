import json
import sqlite3

conn = sqlite3.connect("rosterdb.sqlite")
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
                   
CREATE TABLE User (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
);
CREATE TABLE Course (
    id INTEGER PRIMARY KEY,
    title TEXT UNIQUE
);
CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
) 
''')
                          

filename = input("Enter file: ")
if len(filename) < 1:
    filename = "roster_data.json"

str_data = open(filename).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    cur.execute("INSERT OR IGNORE INTO User (name) VALUES (?)", (name,))
    cur.execute("SELECT id FROM User WHERE name = ?", (name,))
    user_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Course (title) VALUES (?)", (title,))
    cur.execute("SELECT id FROM Course WHERE title = ?", (title,))
    course_id = cur.fetchone()[0]

    cur.execute("""INSERT OR REPLACE INTO Member (user_id, course_id, role) 
                VALUES (?, ?, ?)""", (user_id, course_id, role))
    
conn.commit()
                


