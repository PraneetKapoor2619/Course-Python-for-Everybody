#File length counter
fhandle = open("C:\DOS\PROGRAMS\Python\FILES for DEMO\DEMO 1.txt", 'r')
count = 0
for line in fhandle :
    count = count + 1
print("The no. of lines in the file is", count)