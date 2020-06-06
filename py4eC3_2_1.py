#lin_sum function
def lin_sum(snlist) :
    lsum = 0                #initialize the summing variable
    for snum in snlist :
        lsum = lsum + int(snum)
    return lsum

#main body of the program
#import regular expression library
import re
#open the file
fhandle = open('regex_sum_571313.txt', 'r')
#start extracting integers from the file
int_sum = 0                 #initialize the summing variable
sumline = None              #initialize the variable which sums the integers in a line
#line extraction loop
for line in fhandle :
    snumber = re.findall('[0-9]+', line)
    sumline = lin_sum(snumber)
    int_sum = int_sum + sumline
#print out the answer
print("The sum of all the integers in the given file is:", int_sum)