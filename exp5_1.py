score = float(input("Enter the score: "))

if score > 1.0 :
    print("Score cannot be greater than 1.0!")
    quit()
elif score < 0.0 : 
    print("Score cannot be less than 0.0!")
    quit()
    
if score >= 0.9 :
    print("A")
elif score >= 0.8 :
    print("B")
elif score >= 0.7 :
    print("C")
elif score >= 0.6 :
    print("D")
else :
    print("F")