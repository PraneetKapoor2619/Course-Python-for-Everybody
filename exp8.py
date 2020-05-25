#pay_calc()
def pay_calc(hours, rate) :
    print("Hours id:", id(hours))
    print("Rate id:", id(rate))
    pay = hours * rate
    return pay

#main program body
hours = int(input("Enter number of hours: "))
rate = float(input("Enter the rate per hour: "))
pay = pay_calc(hours, rate)
print("Pay:", pay)