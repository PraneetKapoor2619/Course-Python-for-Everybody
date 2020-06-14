import urllib.request, urllib.parse, urllib.error
import json
import ssl

#ignore SSL certification error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Enter the URL and open it using urllib
URL = input("Enter the URL: ")
url_handle = urllib.request.urlopen(URL, context = ctx).read()
data = url_handle.decode()
#make a list type object of the decoded data
object = json.loads(data)
if len(object) == 0 :
    print("NO DATA READ!!")
    quit()
#iteration and summing variable intialization
sum = 0
itr = 0
#loop to iterate through each dictionary in the list
for item in object['comments'] :
    number = item['count']
    sum = sum + number
    itr = itr + 1
#print out the total number of comments and sum of numbers in the list
print("Total number of comments in the list:", itr)
print("The sum of the numbers given in the JSON file is", sum)