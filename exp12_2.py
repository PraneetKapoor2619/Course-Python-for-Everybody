file_name = input("Enter the name of the file: ")
try :
    fhandle = open(file_name, 'r')
except :
    print("\a BAD FILENAME!!")
    quit()

word_list = list()
word_count = dict()

for line in fhandle :
    word_list = line.split()
    for word in word_list :
        word_count[word] = word_count.get(word, 0) + 1

print("File reading stopped!")

max_count = None 
max_word = None

for word, count in word_count.items() :
    if (max_word == None) or count > max_count :
        max_word = word
        max_count = count

print("The word which occured the maximum number of times is:", max_word, "and it occured", max_count, "times")