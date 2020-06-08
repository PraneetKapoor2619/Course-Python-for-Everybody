#From Dr. Chuck's Python for Everybody
#Section 11.9
#Exercise 1
import re
filename = input("Enter the filename: ")
try :
    fhandle = open(filename, 'r')
except :
    print('\a BAD FILENAME!!')
    quit()
regex = input('Enter the regular expression: ')
count = 0
for line in fhandle :
    line = line.rstrip()
    if re.search(regex, line) :
        print(line)
        count = count + 1
print("No. of lines which matched " + regex + " are " + str(count))