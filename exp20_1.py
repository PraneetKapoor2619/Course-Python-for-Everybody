import sqlite3
import re

conn = sqlite3.connect("tasty.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS tasty")

cur.execute('''CREATE TABLE tasty (
            email TEXT,
            counts INTEGER)''')

file_name = input("Enter the filename: ")
fhandle = open(file_name, 'r')

for line in fhandle :
    emails = re.findall("^From (\S+@\S+)", line)
    for email in emails :
        cur.execute('SELECT counts FROM tasty WHERE email = ?', (email,))           #what if I put a little space after this email parameter?
        
        row = cur.fetchone()
        if row is None :
            cur.execute('INSERT INTO tasty (email, counts) VALUES (?, 1)', (email,))
        else :
            cur.execute('UPDATE tasty SET counts = counts + 1 WHERE email = ?', (email,))
        
    conn.commit()

for row in cur.execute('SELECT email, counts FROM tasty ORDER BY counts DESC LIMIT 10') :
    print(str(row[0]), row[1])