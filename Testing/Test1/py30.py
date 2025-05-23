import os 
os.system('cls')

class Mhs:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim
        
class Data(Mhs):
    def __init__(self,nama,nim,time):
        Mhs.__init__(self,nama,nim)
        self.time = time
        
    @property
    def info(self):
        return "nama : {} , nim : {} , time : {}".format(self.nama,self.nim,self.time)
    
yuki = Data('malik',2342,12)
print(yuki.info)
print(yuki.__dict__)

# object.__dict__ = untuk mengetahui semua atribut yang ada di dalam object

# decorator @property = untuk mengubah method menjadi seperti atribut

# __init__ = untuk menginisialisasi object

# super() = untuk mengakses method dari parent class

# super().__init__() = untuk mengakses method __init__ dari parent class

# super().__init__(self,nama,nim) = untuk mengakses method __init__ dari parent class dengan parameter nama dan nim

# tuple
tuple = (1,2,3,4,5)
print(tuple[0])
print(tuple[1])
# tuple[0] = 2 
# tuple[0] = 2 # error karena tuple tidak bisa diubah

print(15*' </> ')

class Car:
    def __init__(self,name,brand,year):
        self.name = name
        self.brand = brand
        self.year = year
        
    def info(self):
        """ method info """
        return f"Name : {self.name} , Brand : {self.brand} , Year : {self.year}"
    

    def info2(self,*args):
        """ *args """
        return f""" 
    Car 1 :
    Name : {self.name} , Brand : {self.brand} , Year : {self.year}
    Car 2 :
    Name : {args[0].name} , Brand : {args[0].brand} , Year : {args[0].year}
    Car 3 :
    Name : {args[1].name} , Brand : {args[1].brand} , Year : {args[1].year}"""
    # apakah parameter di info2 bisa menggunakan *args atau **kwargs ?
    # bisa menggunakan *args atau **kwargs jika parameter yang diinputkan adalah object
    # contohnya : info2(self,*args) atau info2(self,**kwargs)
    #bagaimana cara mengakses atribut dari object yang diinputkan ? 
    # menggunakan object.atribut 
    
    def info3(self,**kwargs):
        """ **kwargs """
        return f""" 
    Car 1 :
    Name : {self.name} , Brand : {self.brand} , Year : {self.year}
    Car 2 :
    Name : {kwargs['name1']} , Brand : {kwargs['brand1']} , Year : {kwargs['year1']}
    Car 3 :
    Name : {kwargs['name2']} , Brand : {kwargs['brand2']} , Year : {kwargs['year2']}"""
    

toyota = Car('avanza','toyota',2019)
bmw = Car('x5','BMW',2019)
lambo = Car('aventador','Lamborghini',2019)


print(toyota.info())
print(bmw.info())
print(toyota.info2(bmw,lambo))
print(bmw.info2(toyota,lambo))
print(15*' </> ')
print(toyota.info3(name1 = 'aventador',brand1 = 'Lamborghini',year1 = 2019,name2 = 'x5',brand2 = 'BMW',year2 = 2019))
print(lambo.info3(name1 = 'avanza',brand1 = 'toyota',year1 = 2019,name2 = 'x5',brand2 = 'BMW',year2 = 2019))


print(15*' </> ')


