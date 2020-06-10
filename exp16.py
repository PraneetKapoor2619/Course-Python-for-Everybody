#a simpler program to retrieve web pages
import urllib.request, urllib.parse, urllib.error

#create handle
fhandle = urllib.request.urlopen("https://en.wikipedia.org/wiki/Richard_Feynman")

for line in fhandle :
    print(line.decode().strip())