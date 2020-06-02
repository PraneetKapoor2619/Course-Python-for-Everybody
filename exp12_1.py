slist = ['1', '1', 0, 233, 'fool']
sdict = dict()
choice = 'y'
while choice != "N" and choice != "n" :
    skey = input("Enter the key: ")
    svalue = input("Enter the value: ")
    sdict[skey] = svalue
    choice = input("Press N or n if you wish to quit making the dictionary: ")
print(slist, sdict)