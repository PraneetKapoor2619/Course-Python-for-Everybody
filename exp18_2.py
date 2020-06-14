import json
data = '''  [   
                {   
                    "Agent No." : "007",
                    "Name" : "James Bond",
                    "Note" : "Most of his missions can be completed on time if he stops trusting every female he encounters"
                },
                {
                    "Agent No." : "009",
                    "Name" : "Mar gaya Salla!!",
                    "Note" : "Don't be a joker"
                }
            ]'''

#main body
object = json.loads(data)
print("No. of agents:", len(object))
for agent in object :
    print("Agent No.:", agent["Agent No."])
    print("Name:", agent["Name"])
    print("Note:", agent["Note"], "\n")
print("In short, choose quality personnel!!!")