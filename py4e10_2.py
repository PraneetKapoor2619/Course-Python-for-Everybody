'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

#hour_splitter
def hour_splitter(line) :
    wlist1 = line.split()
    wlist2 = wlist1[5].rsplit(':')
    return wlist2[0]
    
#main body
#opening the file and forming its handle
file_name = input("Enter the filename: ")
try :
    fhandle = open(file_name, 'r')
except :
    print("\aBAD FILENAME!!!")
    quit()
#initializing the variables
hour = None
dict_hour = dict()
#reading the file line by line
for line in fhandle :
    if not line.startswith("From ") : continue
    hour = hour_splitter(line)
    dict_hour[hour] = dict_hour.get(hour, 0) + 1
#initialize hour_count list
hour_count = list()
#convert dict_hour into a list of tuples
for hour, count in dict_hour.items() :
    hour_count.append( (hour, count) )
#sort by hour
hour_count = sorted(hour_count)
#print hours with their countS
for hour, count in hour_count :
    print(hour, count)