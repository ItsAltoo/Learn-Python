# Private Variable #

class Name:
    
    # class variabel
    jumlah = 0
    __privateJumlah = 0
    
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
        # variable instance private
        self.__private = "private"
        # variable instance protected
        self._protected = ' protected'
        
ahmed = Name("ahmed",123)


print(ahmed.__dict__)
# print(Name.__dict__)
# print(Name.__privateJumlah)
print(ahmed._protected)