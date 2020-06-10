#import urllib and BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Enter url name and open the url
url = input("Enter the url: ")
html = urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#start taking in the numbers
sigma = 0
tags = soup('span')
for tag in tags :
    sigma = int(tag.contents[0]) + sigma

#print out the sum
print("The sum is:", sigma)