try :
    number = int(input("Enter a number: "))
except :
    print("That is not a number!! One more chance idiot!!")
    try :
        number = int(input("Enter a number: "))
    except :
        print("Fuck you Chev Chelios!!")
        quit()
print("That's it!!")