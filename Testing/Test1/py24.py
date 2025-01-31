# latihan UAS #

def mtk (a,b):
    return a + b

tambah = mtk(3,2)
print(tambah)

# angka1 = int(input('angka 1 :'))
# angka2 = int(input('angka 2 :'))

def kali(a,b):
    return a * b

# print(kali(angka1,angka2))

print('ab' + 'cd')



class Buku:
    angka1 = 2
    angka2 = 5
    
    def __init__(self,nama,nim):
        self.name = nama
        self.nim = nim
        
    def fullName (self):
        print(self.name,self.nim)
    
    def tambah(self):
        return self.angka1 + self.angka2


data = Buku('ouo',1250)
data.fullName()