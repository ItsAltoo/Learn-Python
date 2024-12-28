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