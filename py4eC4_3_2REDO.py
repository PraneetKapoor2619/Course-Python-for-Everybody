import xml.etree.ElementTree as ET
import sqlite3

#retrieve function
def retrieve(entry, tag) :
    flag = False
    for item in entry :
        if item.tag == 'key' and item.text == tag : 
            flag = True
            continue
        if flag == True :
            if item.tag == 'string' :
                return item.text
            elif item.tag == 'integer' :
                return int(item.text)
    return None

#row_extract function
def row_extract(row) :
    if row is not None :
        return int(row[0])
#main body
#creation of SQL cursor 
conn = sqlite3.connect("tracks.sqlite3")
cur = conn.cursor()

#deletion of pre-existing tables from the database
cur.executescript('''
                    DROP TABLE IF EXISTS Track;
                    DROP TABLE IF EXISTS Artist;
                    DROP TABLE IF EXISTS Album;
                    DROP TABLE IF EXISTS Genre
                ''')

#creation of new tables
cur.executescript('''
                    CREATE TABLE Artist ( 
                                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                            name TEXT UNIQUE
                                        );
                    CREATE TABLE Genre (
                                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                            name TEXT UNIQUE
                                        );
                    CREATE TABLE Album (
                                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                            artist_id INTEGER,
                                            title TEXT UNIQUE
                                        );
                    CREATE TABLE Track (
                                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                            title TEXT UNIQUE,
                                            len INTEGER,
                                            rating INTEGER,
                                            count INTEGER,
                                            album_id INTEGER,
                                            genre_id INTEGER
                                        )
                  ''')

#opening XML file and converting it into a string
file_name = input("Enter the filename: ")
fhandle = open(file_name, 'r')
xml_string = fhandle.read()

#converion of XML string data into a tree
xml_tree = ET.fromstring(xml_string)

#producing a list with dict/dict elements out of xml_tree
xml_list = xml_tree.findall('dict/dict/')

#main loop which fills the tables in the database
for item in xml_list :
    
    #retrieving TEXT elements in each table and checking them
    track_name = retrieve(item, 'Name')
    artist_name = retrieve(item, 'Artist')
    album_name = retrieve(item, 'Album')
    genre_name = retrieve(item, 'Genre')
    
    if track_name is None and artist_name is None and album_name is None and genre_name is None : continue
    
    #filling of Genre and extraction of genre_id
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre_name,))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre_name,))
    genre_id = row_extract(cur.fetchone())
    
    #filling of Artist and exraction of artist_id
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist_name,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist_name,))
    artist_id = row_extract(cur.fetchone())
    
    #filling of Album extraction of album_id
    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album_name, artist_id,))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album_name,))
    album_id = row_extract(cur.fetchone())
    
    #filling of Track 
    length = retrieve(item, 'Total Time')
    rating = retrieve(item, 'Rating')
    count = retrieve(item, 'Count')
    cur.execute('INSERT OR IGNORE INTO Track (title, len, rating, count, album_id, genre_id) VALUES (?, ?, ?, ?, ?, ?)', 
                (track_name, length, rating, count, album_id, genre_id,))
    
#writing the database in the RAM to permanent memoryview
conn.commit()

#running an SQL query to check whether I have got the right database or not
query = '''
        SELECT Track.title, Artist.name, Album.title, Genre.name 
        FROM Track JOIN Genre JOIN Artist JOIN Album
        ON Track.genre_id = Genre.id AND Track.album_id = Album.id AND Album.artist_id = Artist.id
        ORDER BY Artist.name LIMIT 3
        '''

for row in cur.execute(query) :
    print(str(row[0]), str(row[1]), str(row[2]), str(row[3]))