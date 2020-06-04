'''
program to generate a list of prime numbers from 1 to x, where x is entered by the user
The algorithm for checking whether a given number is prime or not is as follows: 
1. n <- enter, flag = 0
2. for i from 2 to int(n/2), if n%i == 0, then set flag = 1, break and return
'''
#prime_check function
def prime_check(number) :
	flag = 0
	for x in range(2, int(number/2) + 1) :
		if number%x == 0 : 
			flag = 1
			break
		else : continue
	return flag
			
#main body
upper_limit = int(input("Enter the upper limit: "))
prime_list = list()
for number in range(1, upper_limit + 1) :
	if number == 1 : continue
	elif number == 2 : prime_list.append(2)
	else :
		if prime_check(number) == 0 : prime_list.append(number)
		else : continue

for pn in prime_list :
	print(pn)
print("END PROGRAM")