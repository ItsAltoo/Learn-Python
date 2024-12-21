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

# 