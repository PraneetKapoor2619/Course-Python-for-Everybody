score = float(input("Enter the score: "))

if (score > 1.0) or (score < 0.0):
    print("Score not in the range 0.0 to 1.0")
    quit()
elif score >= 0.9 :
    print("A")
elif score >= 0.8 :
    print("B")
elif score >= 0.7 :
    print("C")
elif score >= 0.6 :
    print("D")
else :
    print("F")