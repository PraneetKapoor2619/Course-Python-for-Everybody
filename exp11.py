#This is a program to open and read a flat text file
fhandle = open('C:\DOS\PROGRAMS\Python\FILES for DEMO\DEMO 1.txt','r')
for line in fhandle :
    print(line.rstrip())