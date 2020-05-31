'''7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.'''

def extract_float(line) :
    pos = None
    for chr in line :
        if chr.isdigit() :
            pos = line.find(chr)
            break
    return float(line[pos:])

#main body
fname = input("Enter the name of the file you wish to open: ")
try :
    fhandle = open(fname, 'r')
except :
    print("BAD FILENAME!!")
    quit()

#variable initialization   
count = 0
flnum = 0.0

for line in fhandle :
    #read for the lines starting with X-DSPAM-Confidence:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        flnum = flnum + extract_float(line)

#print out average
average = flnum/count
print("Average spam confidence:", average)