hours = float(input("Enter the number of hours: "))
rate = float(input("Enter the rate per hour: "))
if hours <= 40:
    pay = rate * hours
else:
    overtime = hours - 40
    pay = (1.5 * rate * overtime) + (rate * 40)
print(pay)