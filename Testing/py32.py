import os 
os.system('cls')

# override method
class Buku:
    def __init__(self,nama:str,tahun:int):
        self.nama = nama
        self.tahun = tahun
        
        
    def showInfo(self):
        print('judul Buku : {}, Tahun Terbit : {}'.format(self.nama,self.tahun))
        

class BukuAljabar(Buku):
    def __init__(self, nama, tahun):
        super().__init__(nama,tahun)
        
    def showInfo(self):
        print('Judul Buku : {}, \nTahun Terbit : {}'.format(self.nama,self.tahun))
        
class BukuFisika(Buku):
    def __init__(self, nama, tahun):
        super().__init__(nama,tahun)
        

aljabar = BukuAljabar('aljabar',2019)
fisika = BukuFisika('fisika',2018)

aljabar.showInfo()
fisika.showInfo()

# override method adalah method yang diwarisi dari class induk, kemudian diubah isinya di class anak 
# dengan cara mendefinisikan method yang sama dengan class induk di class anak 
# seperti menimpa method yang ada di class induk

print('=====================================')

# multiple inheritance
class Buku:
    def __init__(self,nama:str,tahun:int):
        self.nama = nama
        self.tahun = tahun
        
        
    def showInfo(self):
        print('judul Buku : {}, Tahun Terbit : {}'.format(self.nama,self.tahun))
        

class BukuAljabar(Buku):
    def __init__(self, nama, tahun):
        super().__init__(nama,tahun)
        
    def showInfo(self):
        print('Judul Buku : {}, \nTahun Terbit : {}'.format(self.nama,self.tahun))
        
class BukuFisika(Buku):
    def __init__(self, nama, tahun):
        super().__init__(nama,tahun)
        
class BukuKimia(Buku):
    def __init__(self, nama, tahun):
        super().__init__(nama,tahun)
        

class BukuPelajaran(BukuAljabar,BukuFisika,BukuKimia):
    def __init__(self, nama, tahun):
        BukuAljabar.__init__(self,nama,tahun)
        BukuFisika.__init__(self,nama,tahun)
        BukuKimia.__init__(self,nama,tahun)
        
    def showInfo(self):
        print('Judul Buku : {}, \nTahun Terbit : {}'.format(self.nama,self.tahun))
    
pelajaran = BukuPelajaran('pelajaran',2017)
pelajaran.showInfo()


print('=====================================')


# method resolution order (MRO) adalah urutan pengecekan class yang diwarisi oleh class anak 
# urutan pengecekan class adalah dari kiri ke kanan 

class A:
    def show(self):
        print('ini adalah class A')
        
class B:
    def show(self):
        print('ini adalah class B')
        
class C(A,B):
    pass
    # def show(self):
    #     print('ini adalah class C')
    # jika method show di class C diaktifkan maka method show di class C yang akan dijalankan 

obj = C()
obj.show()

print('=====================================')

