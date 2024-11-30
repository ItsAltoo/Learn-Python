import os

class DataMahasiswa:
    def __init__(self, file_name="data_mahasiswa.txt"):
        self.file_name = file_name

    def simpan_data(self, nama, nim):
        mode = "a" if os.path.exists(self.file_name) else "w"
        with open(self.file_name, mode) as file:
            file.write(f"{nama},{nim}\n")
        print("Data berhasil disimpan ke dalam data_mahasiswa.txt.")

    def baca_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                data = file.readlines()
            if len(data) > 0:
                print("Daftar Data Mahasiswa:")
                for line in data:
                    nama, nim = line.strip().split(",")
                    print(f"Nama Lengkap: {nama}, NIM: {nim}")
            else:
                print("File kosong.")
        else:
            print("File tidak ditemukan.")


class Kehadiran:
    def __init__(self, file_name="kehadiran.txt"):
        self.file_name = file_name

    def simpan_kehadiran(self, nama, status):
        mode = "a" if os.path.exists(self.file_name) else "w"
        with open(self.file_name, mode) as file:
            file.write(f"{nama} {status}\n")
        print("Data kehadiran berhasil disimpan.")

    def tampilkan_kehadiran(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                data = file.readlines()
            if len(data) > 0:
                print("Daftar Kehadiran:")
                for line in data:
                    print(line.strip())
            else:
                print("File kosong.")
        else:
            print("File tidak ditemukan.")

    def tambah_kehadiran(self, nama, status):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                data = file.readlines()
                for line in data:
                    if line.startswith(nama):
                        print("Nama sudah ada di daftar.")
                        return
        self.simpan_kehadiran(nama, status)


class FileManager:
    def hapus_file(self, file_name):
        if os.path.exists(file_name):
            konfirmasi = input(f"Apakah Anda yakin ingin menghapus file {file_name}? (y/n): ").lower()
            if konfirmasi == "y":
                os.remove(file_name)
                print(f"File {file_name} berhasil dihapus.")
            else:
                print("Penghapusan file dibatalkan.")
        else:
            print("File tidak ditemukan.")


class ProgramMenu:
    def __init__(self):
        self.data_mahasiswa = DataMahasiswa()
        self.kehadiran = Kehadiran()
        self.file_manager = FileManager()

    def tampilkan_menu(self):
        while True:
            print("\n=== Menu Program ===")
            print("1. Simpan Data Mahasiswa")
            print("2. Baca Data Mahasiswa")
            print("3. Simpan Kehadiran")
            print("4. Tambah Kehadiran")
            print("5. Tampilkan Kehadiran")
            print("6. Hapus File")
            print("0. Keluar")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                nama = input("Masukkan Nama Lengkap: ")
                nim = input("Masukkan NIM: ")
                self.data_mahasiswa.simpan_data(nama, nim)
            elif pilihan == "2":
                self.data_mahasiswa.baca_data()
            elif pilihan == "3":
                nama = input("Masukkan Nama Mahasiswa: ")
                status = input("Masukkan Status Kehadiran (Hadir/Tidak Hadir): ")
                self.kehadiran.simpan_kehadiran(nama, status)
            elif pilihan == "4":
                nama = input("Masukkan Nama Mahasiswa: ")
                status = input("Masukkan Status Kehadiran (Hadir/Tidak Hadir): ")
                self.kehadiran.tambah_kehadiran(nama, status)
            elif pilihan == "5":
                self.kehadiran.tampilkan_kehadiran()
            elif pilihan == "6":
                file_name = input("Masukkan nama file yang ingin dihapus: ")
                self.file_manager.hapus_file(file_name)
            elif pilihan == "0":
                print("Program selesai. Sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    menu = ProgramMenu()
    menu.tampilkan_menu()
