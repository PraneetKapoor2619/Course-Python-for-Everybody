import urllib.request, urllib.parse, urllib.error
import json 
import ssl

#ignore SSL certification error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#API KEY
api_key = False

if api_key is False :
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'                 #preset saved file
else :
    service_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

#making a proper url
while True :
    address = input("Enter the address: ")
    params = dict()
    params['address'] = address
    if api_key is not False : 
        params["key"] = api_key
    URL = service_url + urllib.parse.urlencode(params)
    
    print("Retrieving:", URL)
    url_handle = urllib.request.urlopen(URL, context = ctx).read()
    data = url_handle.decode()
    print("Retrieved", len(data), "characters")
    
    try :
        object = json.loads(data)
    except :
        object = None
        
    if (not object) or ('status' not in object) or (object['status'] != 'OK') :
        print("=======FAILURE TO RETRIEVE=========")
        print(data)
        continue
    
    print(json.dumps(object, indent = 4))
    
    latitude = object['results'][0]['geometry']['bounds']['northeast']['lat']
    longitude = object['results'][0]['geometry']['bounds']['northeast']['lng']
    print("Latitude:", latitude, ", Longitude:", longitude)
    location = object['results'][0]['formatted_address']
    print(location)