fhandle = open("C:\DOS\PROGRAMS\Python\FILES for DEMO\DEMO 1.txt", 'r')
stringo = fhandle.read()
print(stringo,"\nLength of this string is: " + str(len(stringo)))
print(stringo[:])