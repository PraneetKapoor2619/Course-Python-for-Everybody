score = float(input("Enter the score: "))

if (score > 1.0) or (score < 0.0):
    print("Score not in the range 0.0 to 1.0")
    quit()
else :
    if score >= 0.9 :
        print("A")
    else :
        if score >= 0.8 :
            print("B")
        else :
            if score >= 0.7 :
                print("C")
            else :
                if score >= 0.6 :
                    print("D")
                else :
                    print("F")