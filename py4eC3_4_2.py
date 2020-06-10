#import urllib and BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Enter the initial URL, counter, and the position at which the next URL is to be found
url = input("Enter the intial url: ")
count = int(input("Enter the number of iterations of the program: "))
position = int(input("Enter position of the name and next URL to be accessed relative to the first name in the file: "))

#main loop!!
for iter in range(1, count + 1) :
    pos = 1
    html = urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[position - 1].get('href', None)
    print(tags[position - 1].contents[0])