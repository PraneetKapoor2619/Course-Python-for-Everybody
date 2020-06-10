#import urllib and BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import os
from bs4 import BeautifulSoup
import ssl

#fucky stuff
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the url: ")
html = urllib.request.urlopen(url, context = ctx).read()
#print("Printing string html: \n", html)
os.system("PAUSE")
soup = BeautifulSoup(html, 'html.parser')
#print("Printing soup object???\n", soup)
os.system("PAUSE")

#retrieve all of the anchor tags
tags = soup('a')
print("Printing tags \n", tags)
#for tag in tags :
#    print(tag.get('href', None))