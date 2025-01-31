# Tugas: Membuat Program Manajemen Buku
# Deskripsi: Buatlah program sederhana untuk mengelola koleksi buku di perpustakaan. Program ini harus memiliki fitur untuk:

# 1. Menambah buku ke dalam koleksi.
# 2. Menampilkan semua buku yang ada di koleksi.
# 3. Mencari buku berdasarkan judul.
import os
os.system('cls')


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Menambahkan buku ke koleksi"""
        self.books.append(book)

    def show_books(self):
        """Menampilkan semua buku di koleksi"""
        if not self.books:
            print("Koleksi buku kosong!")
        else:
            print("Daftar Koleksi Buku:")
            for index, book in enumerate(self.books, start=1):
                print(f"{index}. Judul: {book.title}, Penulis: {book.author}, Tahun: {book.year}")

    def search_book(self, title):
        """Mencari buku berdasarkan judul"""
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if not found_books:
            print(f"Buku dengan judul '{title}' tidak ditemukan.")
        else:
            print(f"Buku ditemukan:")
            for book in found_books:
                print(f"Judul: {book.title}, Penulis: {book.author}, Tahun: {book.year}")


# Menu interaktif untuk pengguna
library = Library()




def main():
    while True:
        print("\n1. Tambah Buku")
        print("2. Lihat Koleksi Buku")
        print("3. Cari Buku")
        print("4. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            # Input untuk menambahkan buku
            title = input("Masukkan judul buku: ")
            author = input("Masukkan penulis buku: ")
            year = input("Masukkan tahun terbit: ")
            book = Book(title, author, year)
            library.add_book(book)
            print("Buku berhasil ditambahkan!")

        elif pilihan == "2":
            # Menampilkan semua koleksi buku
            library.show_books()

        elif pilihan == "3":
            # Mencari buku berdasarkan judul
            title = input("Masukkan judul buku yang dicari: ")
            library.search_book(title)

        elif pilihan == "4":
            # Keluar dari program
            print("Keluar dari program...")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

        






if __name__ == '__main__':

    main()