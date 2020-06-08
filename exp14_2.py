#From Dr. Chuck's Python for Everybody
#Section 11.9
#Exercise 2
import re
filename = input("Enter filename: ")
try :
    fhandle = open(filename, 'r')
except :
    print("\a BAD FILENAME!")
    quit()
number = 0
count = 0
for line in fhandle :
    line = line.rstrip()
    extracted = re.findall('^New Revision: ([0-9]+)', line)
    if len(extracted) > 0 :
        number = number + int(extracted[0])
        count = count + 1
average = number / count
print(int(average))