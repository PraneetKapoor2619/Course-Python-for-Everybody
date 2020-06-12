import xml.etree.ElementTree as ET
data = '''<person>
       <name>PK</name>
       <phone type = "intl">+91 9319311759</phone>
        <email hide = "yes"/>
        </person>
      '''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Phone Attr:', tree.find('phone').get('type'))
print('Phone No.:', tree.find('phone').text.strip("\n\n"))
print('Attr:', tree.find('email').get('hide'))