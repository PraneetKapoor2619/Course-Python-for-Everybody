#main body
#entering the filename and creating its handle
fname = input("Enter the filename: ")
try :
    fhandle = open(fname, 'r')
except :
    print("\t\t\a   BAD FILENAME!! \n\t\tENDING THIS PROGRAM!!")
    quit()

#initialize list_of_words as an empty list
list_of_words = list()

#read file line by line
for line in fhandle :
    #split the line into words
    words = line.split()
    #start iterating throught each word in words list
    for word in words :
        if word in list_of_words : continue         #if word is in list_of_words, then continue, don't bother
        list_of_words.append(word)                  #if not then append the word to the end of the list_of_words

#sort list_of_words and print it out
list_of_words.sort()
print(list_of_words)