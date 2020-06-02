'''
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

file_name = input("Enter the filename: ")
try :
    fhandle = open(file_name, 'r')
except :
    print("BAD FILENAME!!")
    quit()

word_count = dict()
for line in fhandle :
    if line.startswith("From ") :
        words = line.split()
        word_count[words[1]] = word_count.get(words[1], 0) + 1      #second word is the name of the sender

max_sender = None
max_count = None

for sender, count in word_count.items() :
    if (max_sender == None) or (count > max_count) :
        max_sender = sender
        max_count = count

print(max_sender, max_count)