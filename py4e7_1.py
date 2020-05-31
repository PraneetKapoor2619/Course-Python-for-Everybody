fname = input("Enter the name of the file you wish to open: ")
try:
    fhandle = open(fname, 'r')
except :
    print("BAD FILENAME!!")
    quit()
for line in fhandle :
    line = line.rstrip()
    print(line.upper())