import xml.etree.ElementTree as ET
import sqlite3

#retrieve_xml function
def retrieve_xml(d, key) :
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None
    
#retrieve_row function
def retrieve_row (row) :
    if row is not None :
        return int(row[0])

#main body
#creating the database
conn = sqlite3.connect("tracks.sqlite")
cur = conn.cursor()
cur.executescript(''' DROP TABLE IF EXISTS Track;
                DROP TABLE IF EXISTS Artist;
                DROP TABLE IF EXISTS Album;
                DROP TABLE IF EXISTS Genre;
                CREATE TABLE Artist (
                id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name    TEXT UNIQUE
                );
                CREATE TABLE Genre (
                    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    name    TEXT UNIQUE
                );
                CREATE TABLE Album (
                    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    artist_id  INTEGER,
                    title   TEXT UNIQUE
                );
                CREATE TABLE Track (
                    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    title TEXT  UNIQUE,
                    album_id  INTEGER,
                    genre_id  INTEGER,
                    len INTEGER, rating INTEGER, count INTEGER
                )
            ''') 

#parsing of XML and creation of its tree
file_name = input("Enter the filename: ")
try :   
    fhandle = open(file_name, 'r')
except :
    print("BAD FILENAME!!")
    quit()
xml_string = fhandle.read()
xml_tree = ET.fromstring(xml_string)

#extraction of XML data and entry into the database
#parsing the tree dict/dict/dict
xml_list = xml_tree.findall('dict/dict/dict')
for item in xml_list :
    
    #exraction starring Chris Hemsworth
    track_title = retrieve_xml(item, 'Name')
    len = retrieve_xml(item, 'Total Time')
    rating = retrieve_xml(item, 'Rating')
    count = retrieve_xml(item, 'Track Count')
    artist_name = retrieve_xml(item, 'Artist')
    genre = retrieve_xml(item, 'Genre')
    album_title = retrieve_xml(item, 'Album')
    
    #life giving nothing
    if track_title is None or artist_name is None or album_title is None or genre is None : 
        continue
    
    #for Artist
    cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?)", (artist_name,))
    cur.execute("SELECT id FROM Artist WHERE name = ?", (artist_name,))
    artist_id = retrieve_row(cur.fetchone())
    
    #for Genre
    cur.execute("INSERT OR IGNORE INTO Genre (name) VALUES (?)", (genre,))
    cur.execute("SELECT id FROM Genre WHERE name = ?", (genre,))
    genre_id = retrieve_row(cur.fetchone())
   
    #for Album
    cur.execute("INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?, ?)", (artist_id, album_title))
    cur.execute("SELECT id FROM Album WHERE title = ?", (album_title,))
    album_id = retrieve_row(cur.fetchone())
    
    #for Track
    cur.execute(''' INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) 
                    VALUES (?, ?, ?, ?, ?, ?)''',
                    (track_title, album_id, genre_id, len, rating, count))    

conn.commit()

command = '''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3'''
for row in cur.execute(command) :
    print(str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]))