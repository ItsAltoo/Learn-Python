from rich import print

class Buku:
    
    def __init__(self,judul: str,pengarang:str,tahun_terbit:int):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        
    def deskripsi(self):
        """ Menampilkan Deskripsi """
        print(f""" 
[blue]Judul[/blue] : [red]{self.judul}[/red]
[blue]Pengarang[/blue] : [red]{self.pengarang}[/red]
[blue]Tahun terbit[/blue] : [red]{self.tahun_terbit}[/red] 
              """)
        
  
# inheritance 
class Mahasiswa(Buku):
    def __init__(self, judul, pengarang, tahun_terbit,nama_mahasiswa,nim):
        super().__init__(judul, pengarang,tahun_terbit)
        self.nama_mahasiswa = nama_mahasiswa
        self.nim = nim
        self.buku_dipinjam = []
    
    def pinjam_buku(self):
        self.buku_dipinjam.append(self.judul)
    
    def simpan_ke_file(self):
        with open('Testing/data_peminjaman.txt','a')as file:
             file.write(f""" 
Nama : {self.nama_mahasiswa}
NIM : {self.nim}
Buku Dipinjam : {self.buku_dipinjam}
""")

buku_pertama = Mahasiswa('life of pi','Yann Martel',2012,'Ten','1250')
buku_kedua = Mahasiswa('Rich dad poor dad','Robert kiyosaki',1997,'Ten','1250',)

buku_pertama.deskripsi()
buku_pertama.simpan_ke_file()

buku_kedua.deskripsi()
buku_kedua.simpan_ke_file()