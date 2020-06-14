import json
data = '''{
            "name" : "Praneet Kapoor",
            "phone" :   {
                            "type" : "intl",
                            "number" : "+91 931931 1759"
                        },
            "email" :   {
                            "hide" : "NO",
                            "address" : "kapoorpraneet2619@gmail.com"
                        }
        }'''

#main body
object = json.loads(data)
print("Name:", object["name"])
print("Phone type:", object["phone"]["type"])
print("Phone No.:", object["phone"]["number"])
if object["email"]["hide"] != "YES" :
    print("Email:", object["email"]["address"])