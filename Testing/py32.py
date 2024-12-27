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