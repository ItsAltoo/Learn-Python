# Encapsulasi #

class Hero:
    
    def __init__(self,name,health,power):
        self.__name = name
        self.__health = health
        self.__power =  power
        
    # getter
    def getName(self):
        return  self.__name
    
    def getHealth(self):
        return self.__health
    
    # setter
    def attacked(self,attacked):
        self.__health -= attacked
        
    



# awal dari game
lancelot = Hero("Lancelot",185,20)

# game berjalan
# print(lancelot.__name) <- contoh dari Encapsulasi
print(lancelot.getName())


print(lancelot.getHealth())
lancelot.attacked(25)
print(lancelot.getHealth())


print(20*'_-')



# Staticmethod dan Classmethod #


class Data:
    
    # private class variable
    __angka = 0
    
    def __init__(self,nama):
        self.__nama = nama
        Data.__angka += 1
    
    # method ini hanya berlaku untuk objek
    def getAngka1(self):
        return Data.__angka
    
    # method ini tidak berlaku untuk objek tapi belaku untuk class
    def getAngka2():
        return Data.__angka
    
    
    # method static (decorator) nempel ke objek dan class
    @staticmethod
    def getAngka3():
        return Data.__angka
    
    
    @classmethod
    def getAngka4(cls):
        return cls.__angka
    
    
yuki = Data('Yuki')

yui = Data('Yui')

print(f"Memanggil dengan Objek : {yuki.getAngka1()}")
print(f"Memanggil dengan class : {Data.getAngka2()}")

print(5*'~')
yuta = Data('Yuta')

print(f"Memanggil dengan Objek : {yuki.getAngka3()}")
print(f"Memanggil dengan class : {Data.getAngka3()}")

print(5*'~')

print(f"Memanggil dengan Objek : {yuki.getAngka4()}")
print(f"Memanggil dengan class : {Data.getAngka4()}")