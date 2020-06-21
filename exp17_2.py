import xml.etree.ElementTree as ET
input = '''<stuff>
            <users>
                <user x = '41'>
                    <id>041156014918</id>
                    <name>Praneet Kapoor</name>
                </user>
                <user x = "43">
                    <id>04315604918</id>
                    <name>Rachit Jain</name>
                </user>
            </users>
           </stuff>'''

tree = ET.fromstring(input)
lst = tree.findall("users/user")
print(lst)
print("User count:", len(lst))
for item in lst :
    print('User Attr:', item.get('x'))
    print('Name:', item.find('name').text)
    print('Roll No.:', item.find('id').text, "\n")
print("ALL DONE!!")