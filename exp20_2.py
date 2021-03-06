import xml.etree.ElementTree as ET
data = '''
        <dict>
	<key>Major Version</key><integer>1</integer>
	<key>Minor Version</key><integer>1</integer>
	<key>Date</key><date>2015-11-24T11:12:10Z</date>
	<key>Application Version</key><string>12.3.1.23</string>
	<key>Features</key><integer>5</integer>
	<key>Show Content Ratings</key><true/>
	<key>Music Folder</key><string>file:///Users/csev/Music/iTunes/iTunes%20Music/</string>
	<key>Library Persistent ID</key><string>B7006C9E9799282E</string>
	<key>Tracks</key>
	<dict>
		<key>369</key>
		<dict>
			<key>Track ID</key><integer>369</integer>
			<key>Name</key><string>Another One Bites The Dust</string>
			<key>Artist</key><string>Queen</string>
			<key>Composer</key><string>John Deacon</string>
			<key>Album</key><string>Greatest Hits</string>
			<key>Genre</key><string>Rock</string>
			<key>Kind</key><string>MPEG audio file</string>
			<key>Size</key><integer>4344295</integer>
			<key>Total Time</key><integer>217103</integer>
			<key>Disc Number</key><integer>1</integer>
			<key>Disc Count</key><integer>1</integer>
			<key>Track Number</key><integer>3</integer>
			<key>Track Count</key><integer>17</integer>
			<key>Year</key><integer>1980</integer>
			<key>Date Modified</key><date>2006-02-14T16:13:02Z</date>
			<key>Date Added</key><date>2006-02-14T16:12:53Z</date>
			<key>Bit Rate</key><integer>160</integer>
			<key>Sample Rate</key><integer>44100</integer>
			<key>Play Count</key><integer>55</integer>
			<key>Play Date</key><integer>3518868190</integer>
			<key>Play Date UTC</key><date>2015-07-04T19:23:10Z</date>
			<key>Skip Count</key><integer>1</integer>
			<key>Skip Date</key><date>2015-10-14T23:31:47Z</date>
			<key>Rating</key><integer>100</integer>
			<key>Album Rating</key><integer>100</integer>
			<key>Album Rating Computed</key><true/>
			<key>Normalization</key><integer>1511</integer>
			<key>Compilation</key><true/>
			<key>Persistent ID</key><string>21130E105F3B8845</string>
			<key>Track Type</key><string>File</string>
			<key>File Type</key><integer>1297106739</integer>
			<key>Location</key><string>file:///Users/csev/Music/iTunes/iTunes%20Music/Compilations/Greatest%20Hits/03%20Another%20One%20Bites%20The%20Dust.mp3</string>
			<key>File Folder Count</key><integer>4</integer>
			<key>Library Folder Count</key><integer>1</integer>
		</dict>
        </dict>
    </dict>
        '''

tree = ET.fromstring(data)
print(tree)
lst = tree.findall('dict/dict/')
key_value = input("Enter the key_value you are looking for: ")
flag = False
retrieved = None
for item in lst :
    if item.tag == 'key' and item.text == key_value : 
        flag = True
        continue
    if flag == True :
        if item.tag == 'string' :
            retrieved = item.text
        elif item.tag == 'integer' :
            retrieved = int(item.text)
        break 
print("Retrieved: ", retrieved)