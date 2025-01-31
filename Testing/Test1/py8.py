""" 
Deskripsi Project: Pengecekan Kehadiran Siswa
Fitur:

Menambahkan nama siswa ke daftar hadir.
Mengecek apakah siswa sudah hadir atau belum.
Menampilkan daftar siswa unik yang hadir.
Menampilkan jumlah siswa yang hadir.
"""

def tampilkan_menu():
    print("\n=== Menu Kehadiran ===")
    print("1. Tambahkan nama siswa")
    print("2. Cek apakah siswa sudah hadir")
    print("3. Tampilkan daftar siswa unik")
    print("4. Tampilkan jumlah siswa yang hadir")
    print("5. Keluar")

def tambahSiswa(daftarSiswa):
    nama = input(f"Masukkan nama yang ingin di masukkan :")
    
    daftarSiswa.append(nama)
    print(f"{nama} telah di tambahkan ke daftar hadir")
    

def cekHadir(daftarSiswa):
    nama = input(f"Masukkan nama yang ingin di masukkan :")
    
    if nama in daftarSiswa:
        print(f"{nama} Telah Hadir")
    else:
        print(f"{nama} Belum Hadir")
        
def siswaUnik(daftarSiswa):
    siswa_unik = set(daftarSiswa)
    print("\nDaftar siswa unik yang hadir:")
    
    for siswa in siswa_unik:
        print(f"- {siswa}")
        
def jumlahSiswa(daftarSiswa):
    print(f"\nJumlah total siswa yang hadir adalah {len(daftarSiswa)}")
    
def main():
    daftarSiswa = []
    
    while True:
        tampilkan_menu()
        choose = input(f"pilih opsi dari 1-5 :")
        
        if choose == '1':
            tambahSiswa(daftarSiswa)
        elif choose == '2':
            cekHadir(daftarSiswa)
        elif choose == '3':
            siswaUnik(daftarSiswa)
        elif choose == '4':
            jumlahSiswa(daftarSiswa)
        elif choose == '5':
            print("terima kasih telah mencoba program ini :D")
            break
        else:
            print(f"Tolong masukkan opsi yang benar")
            
main()

