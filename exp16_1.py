#a simpler program to retrieve web pages
import urllib.request, urllib.parse, urllib.error

#create handle
fhandle = urllib.request.urlopen("https://en.wikipedia.org/wiki/Richard_Feynman")

count = dict()
for line in fhandle :
    word = line.decode().strip()
    count[word] = count.get(word, 0) + 1

sno = 1 
for word, num in count.items() :
    print(sno, ".", word, num)
    sno = sno + 1