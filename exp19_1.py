class PartyAnimal :
    x = 0
    
    def party(self, num) :
        self.x = self.x + num
        print("So far", self.x)

an = PartyAnimal()
an.party(2)
an.party(2)
an.party(2)
print(type(an))
print(dir(an))