fhandle = open("C:\DOS\PROGRAMS\Python\FILES for DEMO\DEMO 1.txt", 'r')
flag = None
for line in fhandle :
    if line.startswith('It is') :
        flag = 1
        break
if flag == 0 :
    print('Not found')
else :
    print('Line is:', line)