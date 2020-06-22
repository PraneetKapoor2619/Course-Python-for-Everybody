import sqlite3
import json


#main body

#creation of a new database and database cursor
conn = sqlite3.connect("rosterdb.sqlite")
cur = conn.cursor()

#dropping of any pre-existing tables
cur.executescript('''
                        DROP TABLE IF EXISTS User;
                        DROP TABLE IF EXISTS Course;
                        DROP TABLE IF EXISTS Member;
                ''')

#creation of new tables 
cur.executescript('''
                        CREATE TABLE User (
                                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                            name TEXT UNIQUE
                                            );
                        CREATE TABLE Course (
                                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                            title TEXT UNIQUE
                                            );
                        CREATE TABLE Member (
                                            user_id INTEGER,
                                            course_id INTEGER, 
                                            role INTEGER,
                                            PRIMARY KEY (user_id, course_id)
                                            );
                    ''')

#reading of JSON file and its conversion into a python list (read the roster_data.json file. Square brackets are used there.)
file_name = input("Enter the filename: ")
fhandle = open(file_name, 'r')
json_string = fhandle.read()
json_list = json.loads(json_string)

#reading of items in the list and filling of tables
for entry in json_list :
    
    #retrievale of user name, course name (in coded form), and role from the entry in the JSON file
    user = entry[0]
    course = entry[1]
    role = entry[2]
    
    #filling of User table and extraction of user_id
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (user,))
    cur.execute('SELECT id FROM User WHERE name = ?', (user,))
    user_id = cur.fetchone()[0]
    
    #filling of Course table and extraction of course_id
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (course,))
    course_id = cur.fetchone()[0]
    
    #filling of Member table
    cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)', (user_id, course_id, role))

conn.commit()

while True :
    command = input("Enter the command to run: ")
    cur.execute(command)
    list = cur.fetchone()
    for row in list :
        print(row)