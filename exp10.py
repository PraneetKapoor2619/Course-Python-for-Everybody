#variable initialization
smallest = None
largest = None
number = None

#indefinite loop
while True :
    ivalue = input("Enter a number: ")
    if ivalue == 'done' :
        break
    try :
        number = int(ivalue)
    except :
        print("Invalid input")
    if (largest == None) and (smallest == None) :
        largest = number
        smallest = number
    else :
        if number > largest :
            largest = number
        elif number < smallest :
            smallest = number
print("Maximum is", largest) 
print("Minimum is", smallest)