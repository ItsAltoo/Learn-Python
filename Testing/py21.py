# __main__ adalah top level code environment

# __name__ == "__main__" akan terjadi jika ada di program utama

## __name__ pada file program utama
print(f"nilai __name__ pada py21.py = {__name__}")

## __name__ pada file program eksternal
import library.py10

## contoh penggunaan __main__

# deklarasi
def tambah (a:int,b: int)-> int:
    return a + b



# fungsi utama
if __name__ == "__main__":
    angka1 = 4
    angka2 = 12
    hasil = tambah(angka1,angka2)
    print(f"hasil tambah : {hasil}")