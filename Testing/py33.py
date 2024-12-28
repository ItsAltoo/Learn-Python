# Diamond problem

class A:
    def show(self):
        print('ini adalah class A')
        
class B(A):
    def show(self):
        print('ini adalah class B')
        
class C(A):
    def show(self):
        print('ini adalah class C')
        
class D(B,C):
    pass

d = D()
d.show()

# Jadi mengapa class B yang ditampilkan bukan class C? 
# Karena method resolution order (MRO) adalah urutan pengecekan class yang diwarisi oleh class anak urutan pengecekan class adalah dari kiri ke kanan dan class B lebih dulu dari class C 

print('=====================================')



# magic method

class Mhs:
    
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim
        # biasa digunakan untuk inisialisasi object 
        
    def __str__(self):
        return 'nama : {} , nim : {}'.format(self.nama,self.nim)
    # biasa digunakan untuk menampilkan object dan biasa digunakan untuk user
    
    def __repr__(self):
        return 'nama : {} , nim : {}'.format(self.nama,self.nim)
    # biasa digunakan untuk menampilkan object dan biasa digunakan untuk debugging 
    
    def __add__(self,objek):
        return self.nim + objek.nim
    # biasa digunakan untuk operasi matematika dan operasi lainnya
    
    def __len__(self):
        return len(self.nama)
    # biasa digunakan untuk menghitung panjang object dan biasa digunakan untuk operasi matematika
    
    # def __del__(self):
    #     print('object dihapus')
    # biasa digunakan untuk menghapus object dan biasa digunakan untuk operasi lainnya

mhs = Mhs('yuki',123)
mhs2 = Mhs('yui',321)
print(mhs)
print(mhs + mhs2)
print(mhs.__len__())
print(mhs.__repr__())
print(mhs.__str__())
# del mhs

print('=====================================')