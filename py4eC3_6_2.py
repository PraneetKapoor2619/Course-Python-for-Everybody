import urllib.request, urllib.parse, urllib.error
import json
import ssl

#ignore SSL certification error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#API KEY: If in future I get my own API key, then I will remove that false statement and use my own key
api_key = False
#dealing with service_url as per the value of api_key set above
if api_key is False :
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else :
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

#an infinite while loop
while True :
    #creating a proper URL on the basis of the address entered by the user
    address = input("Enter the address: ")
    #creating a dictionary to include the parameters
    params = dict()
    params["address"] = address
    if api_key is not False :
        params["key"] = api_key
    #create a proper URL using service_url and params by string concatenation
    URL = service_url + urllib.parse.urlencode(params)
    #open the URL using urllib, read it and decode to UTF-8
    urlhandle = urllib.request.urlopen(URL, context = ctx).read()
    data = urlhandle.decode()
    print("Retrieved", len(data), " characters.")
    
    #use JSON library to create a list type object 
    try :
        object = json.loads(data)
    except :
        object = None
    
    #check if the status is OK or NOT
    if (not object) or ('status' not in object) or (object['status'] != 'OK') :
        print("=======FAILURE TO RETRIEVE=========")
        print(data)
        continue
    
    place_id = object['results'][0]['place_id']
    print("Place ID:", place_id)