fhandle = open('C:\DOS\PROGRAMS\Python\FILES for DEMO\DEMO 2.txt')
line_num = 0
for line in fhandle :
    line_num = line_num + 1
    line = line.rstrip()
    if not 'Dexter' in line :
        continue
    print(str(line_num) + ".", line)