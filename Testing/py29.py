import os 
os.system('cls')

# Getter & Setter

class Character :
    
    def __init__(self,name,darah,power):
        self.nama = name
        self.__darah = darah
        self.__power = power
        #self.__info = 'name : {} , Darah : {}'.format(self.nama,self.__darah)
    
    @property # <- decorator @property
    def informasi(self):
        return 'name : {} , Darah : {}'.format(self.nama,self.__darah)
    
    @property
    def power(self):
        pass
    
    @power.getter
    def power(self):
        return self.__power
    
    @power.setter
    def power(self,inpt):
        self.__power = inpt
    
    @power.deleter
    def power(self):
        print('delete power !')
        self.__power = None
    
    
    
    
    
    
    
yuki = Character('yuki',100,20)

# print(yuki.informasi()) 
print(yuki.informasi)   # <- mengubah method menjadi atribut
yuki.nama = 'yui'
print(yuki.informasi)

print('\n',13*' </line> ','\n')

print(yuki.power)
yuki.power = 80
print(yuki.power)
print(yuki.__dict__)

del yuki.power

print(yuki.__dict__)

data = [12,3,412,532,12]

count = sum(data) / len(data)
print(count)