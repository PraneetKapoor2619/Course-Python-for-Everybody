#Name: Okayish calculator
#Written by: P.K.
#System time: 11:26 AM, 26.05.2020

def add(N1, N2) :
    return N1 + N2 

def subtract(N1, N2) :
    return N1 - N2
    
def multiply(N1, N2) :
    return N1 * N2

def divide(N1, N2) :
    return N1 / N2
    
def mod(N1, N2) :
    return N1 % N2

def exponent(N1, N2) :
    return N1 ** N2

#main program body
import os
a = 1
result = 0
while a == 1 :
    os.system("CLS")
    print("\t\t\t\tMENU")
    if result != "LOL" :
        N = float(input("Enter first real number, N: "))                #no provison for dealing with bad input is here. 
        P = float(input("Enter second real number, P: "))               #left as an exercise for the viewer :-)
    else :
        print("N = " + str(N) + "\nP = " + str(P))
    print("1. -> ADD \t 3. -> MULTIPLY \t 5. -> MOD")
    print("2. -> SUBTRACT \t 4. -> DIVIDE \t 6. -> EXPONENT")
    try :
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= 6 :
            if choice == 1 :
                result = add(N, P)
            elif choice == 2 :
                result = subtract(N, P)
            elif choice == 3 :
                result = multiply(N, P)
            elif choice == 4 :
                result = divide(N, P)
            elif choice == 5 :
                result = mod(N, P)
            elif choice == 6 :
                result = exponent(N, P)
            print("Result is", result)
            os.system("PAUSE")
        else :
            print("WRONG CHOICE COMRADE!!")
            result = "LOL"
            os.system("PAUSE")
    except :
        print("\a Dikhai nhi deyta? \a Number maang raha hu, NUMBER!!")
        result = "LOL"
        os.system("PAUSE")