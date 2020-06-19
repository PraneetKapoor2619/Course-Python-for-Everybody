import re
import sqlite3

conn = sqlite3.connect("Counts.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")
#cur.execute("DELETE FROM Counts")

file_name = input("Enter the filename: ")
fhandle = open(file_name)

for line in fhandle :
    org_name = re.findall('^From \S+@(\S+)', line)
    if len(org_name) == 0 : continue
    organization = org_name[0]
    
    cur.execute('SELECT count FROM Counts WHERE org = ?', (organization,))
    row = cur.fetchone()
    if row is None :
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (organization,))
    else :
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (organization,))

conn.commit()

for row in cur.execute('SELECT org, count FROM Counts ORDER BY count DESC') :
    print(str(row[0]), row[1])