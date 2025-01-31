# Menambah kontak baru (Nama & Nomor Telepon).
# Melihat semua kontak yang tersimpan.
# Mencari kontak berdasarkan nama.
# Menghapus kontak tertentu.
# Keluar dari program.

data_kontak = []

def get_kontak():
    nama = input("Masukkan Nama Anda :")
    nomor = int(input('Masukkan Nomor Anda :'))
    kontak = {'nama':nama , 'nomor':nomor}
    data_kontak.append(kontak)
    print(f'Kontak {nama} telah ditambahkan!')
    
def check_kontak():
    if not data_kontak:
        print('Data tidak ditemukan !')
    else:
        for i,kontak in enumerate(data_kontak,+1):
            print(f'{i}.Nama : {kontak['nama']}, Nomor : {kontak['nomor']}')
            
def find_kontak():
    cari = input('Cari nama kontak :')
    for kontak in data_kontak:
        if kontak['nama'].lower() == cari.lower():
            print(f'Nama : {kontak['nama']} , Nomor : {kontak['nomor']}')
            
    print('Nama tidak di temukan')
    
    
def del_kontak():
    cari = input('Cari nama yang ingin di hapus :')
    for kontak in data_kontak:
        if kontak['nama'].lower() == cari.lower():
            print(f'Kontak {kontak['nama']} telah dihapus !')
            data_kontak.remove(kontak)
            return
    print('Kontak tidak di temukan !')
    
if __name__ == '__main__':
    while True:
        print(""" Buat Kontak Anda
1.Tambah Kontak
2.Cek Kontak
3.Cari Kontak
4.Hapus Kontak
5.Exit
              """)
        inpt = input('Pilih Opsi :')
        
        if inpt == '1':
            get_kontak()
        elif inpt == '2':
            check_kontak()
        elif inpt == '3':
            find_kontak()
        elif inpt == '4':
            del_kontak()
        elif inpt == '5':
            break
        else:
            print('Tolong Pilih Salah Satu Opsi Di atas !')