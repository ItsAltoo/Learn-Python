class Mahasiswa:
    #class variable / variable statis
    jumlah = 0
    
    def __init__(self,firstName: str,lastName: str,nim: int):
        # instance variable
        self.nama_depan = firstName # self pada konstruktor sama saja seperti variable saat memanggil classnya
        self.nama_akhir = lastName
        self.nim = nim 
        Mahasiswa.jumlah += 1
        print('Hallo Nama saya ' + self.nama_depan)
        
mhs = Mahasiswa('Yui','Shiro',12312) # variable mhs bsa dibilang adalah self pada konstruktor
print(Mahasiswa.jumlah)
mhs = Mahasiswa('Yuki','Brine',1122312)
print(Mahasiswa.jumlah)
mhs = Mahasiswa('Yami','Kuro',102312)
print(Mahasiswa.jumlah)




class Hero:
    # class variable
    jumlah_hero = 0
    
    def  __init__(self,inptName,inptHelth,inptAtck,inptArmor):
        # instance variable
        self.name = inptName
        self.darah = inptHelth
        self.attack = inptAtck
        self.armor = inptArmor
        Hero.jumlah_hero += 1
    
    # void function / method tanpa return
    def who(self):
        print(f'Hi {self.name}')
        
    # method dengan argument
    def darahUp(self,up):
        self.darah += up
        
    # method dengan return
    def getDarah(self):
        return self.darah
    

hero1 = Hero('Mamot',120,20,50)
hero2 = Hero('kiku',122,32,41)

