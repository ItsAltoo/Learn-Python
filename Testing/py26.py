# Tugas: Membuat Program Manajemen Buku
# Deskripsi: Buatlah program sederhana untuk mengelola koleksi buku di perpustakaan. Program ini harus memiliki fitur untuk:

# 1. Menambah buku ke dalam koleksi.
# 2. Menampilkan semua buku yang ada di koleksi.
# 3. Mencari buku berdasarkan judul.
import os
os.system('cls')


class Buku:
    
    def  __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
        

class Library(Buku):
    
    def __init__(self,title,author,year):
        super().__init__(title,author,year)
        self.books = []
        
    def add_book(self):
        self.books.append(f"Judul : '{self.title}' ,Author : '{self.author}' , Tahun terbit : '{self.year}'")
    
    def show_books(self):
        print(self.books)
            
            

def main():
    print(f""" 
1. Tambah Buku
2. Lihat Koleksi Buku
3. Cari Buku
4. Keluar
          """)
    opsi = input('Pilih Opsi :')
    
    if opsi == '1':
        title = input('Masukkan judul buku :')
        author = input('Masukkan author buku :')
        year = input('Masukkan tahun terbit buku :')
        buku = Library(title,author,year)
        buku.add_book()
        print('Buku berhasil di tambahkan!')
        
    elif opsi == '2':
        






if __name__ == '__main__':
    pass