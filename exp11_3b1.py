fhandle = open('C:\DOS\PROGRAMS\Python\FILES for DEMO\DEMO 2.txt')
for line in fhandle :
    line = line.rstrip()
    if line.startswith('From: ') :
        print(line)