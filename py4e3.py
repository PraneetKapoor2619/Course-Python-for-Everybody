#computepay(): This functions computes the gross pay.
#No. of hours above 40 are considered as overtime
def computepay(hours, rate) :
    if hours <= 40 :
        pay = hours * rate
    else :
        overtime = hours - 40
        pay = (1.5 * rate * overtime) + (rate * 40)
    return pay

#main body of the program
hours = float(input('Enter the number of hours: '))
rate = float(input('Enter the rate per hour: '))
pay = computepay(hours, rate)
print("Pay", pay)