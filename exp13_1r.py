#word_stripper: strips the words of bullshit
def word_stripper(word) :
    if  not word[-1].isalpha :
        return word.rsplit(word[-1])
    elif not word[0].isalpha :
        return word.lsplit(word[0])
    else :
        return word
#main body
#enter the filename and form its handle
file_name = input("Enter the filename: ")
try :
    fhandle = open(file_name, mode = 'r', encoding = "UTF-8")
except :
    print("BAD FILENAME!!")
    quit()
#start reading the file line by line
dict_words = dict()                                                     #create an empty dictionary
for line in fhandle :
    word_list = line.split()
    for word in word_list :
        stripped_word = word_stripper(word)                             #strip the word of bullshit
        dict_words[stripped_word] = dict_words.get(word, 0) + 1          #add word to dictionary and increment its count by 1 if it already exists
#end file reading
#generate list of (count, word) tuple using items() method
word_list = list()                                                      #initilaze word_list()
for word, count in dict_words.items() :
    word_list.append( (count, word) )
#sorting of word_list in reverse order
word_list = sorted(word_list, reverse = True)
#print the first 10 elements of this sorted list
for (count, word) in word_list :
    print(word, count)
#end program