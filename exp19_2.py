class PartyAnimal(object) :
    x = 0
    
    def __init__(self) :
        print("I am constructed!! I am ALIVE!!!!")
        self.x = 69
    
    def party(self) :
        self.x = self.x + 1
        print('So far', self.x)
    
    def __del__(self) :
        print("I am destructed!! I AM DEAAAAAAAAAADDDD!!!!")

an = PartyAnimal()
an.party()
an.party()
an.party()
an = 42
print(" 'an' contains", an)