#main body
#Open the file with the user entered filename and create its handle
fname = input("Please enter the filename: ")
try :
    fhandle = open(fname)
except :
    print("\t\t\a   BAD FILENAME!! \n\t\tENDING THIS PROGRAM!!")
    quit()
    
#initialize the line counter variable
counter = 0

#start reading the file line by line
for line in fhandle :
    if not line.startswith("From ") : continue
    ind_words = line.split()
    print(ind_words[1])
    counter = counter + 1

#print the result
print("There were " + str(counter) + " lines in the file with From as the first word")