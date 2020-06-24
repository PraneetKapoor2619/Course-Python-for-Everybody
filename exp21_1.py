import sqlite3

conn = sqlite3.connect('table1.sqlite')
cur = conn.cursor()

cur.executescript('''
                        DROP TABLE IF EXISTS Table1;
                        CREATE TABLE Table1 (name TEXT, number INTEGER);
                        INSERT INTO Table1 (name, number) VALUES ('Praneet', 04115604918);
                        INSERT INTO Table1 (name, number) VALUES ('Rachit', 04315604918);
                ''')

cur.execute("SELECT * FROM Table1 WHERE name = 'Praneet'")
row = cur.fetchone()
print(row)
print(len(row))

cur.execute("SELECT * FROM Table1 WHERE name = 'HUUUUUU'")
row = cur.fetchone()
print(row)
print(len(row))

conn.commit()