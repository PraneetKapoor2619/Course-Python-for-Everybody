file_name = input("Enter filename: ")
try :
    fhandle = open(file_name, 'r', encoding="utf8")
except :
    print('BAD FILENAME!!')
    quit()

words = list()
dict_of_words = dict()

for line in fhandle :
    words = line.split()
    for word in words :
        dict_of_words[word] = dict_of_words.get(word, 0) + 1

list_of_words = list()

for key, value in dict_of_words.items() :
    list_of_words.append((value, key))

sorted_word_list = sorted(list_of_words, reverse = True)

for occ, word in sorted_word_list[:10] :
    print(word, occ)