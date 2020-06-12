import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#Ignore SSL certification error 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#open the url
url = "http://py4e-data.dr-chuck.net/comments_571317.xml"
xmlString = urllib.request.urlopen(url, context = ctx).read()

#make an XML tree out of xmlString
tree = ET.fromstring(xmlString)

#make a list of numbers: parsing order is commentinfo/comments/comment/count
numList = tree.findall('comments/comment')
sigma = 0
for item in numList :
    sigma = sigma + int(item.find('count').text)
print("The sum of all the numbers in the node 'count' in the given XML file is:", sigma)