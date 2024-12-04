try:
    with open('db/py18/data.txt','r') as file:
        print(file.read())
except:
    print("file tidak ditemukan,sedang membuat file baru...")
    with open('db/py18/data.txt','w',encoding='utf-8') as file:
        file.write("anjayz")
print("terima kasih")

from numbers import Number

def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise " input harus angka"
    return a+b

print(tambah(5,2)) # <- input tidak bisa bernilai string karena isintance-nya Number

print(20*'~')

angka = 0

# try:
#     hasil = 10/angka
# except Exception as error_message:
#     print(error_message)
    

try:
    hasil = 10/angka
except ZeroDivisionError as error_message:
    print(error_message)


# Loop list

list_num = [2,10,5,9,6,3,4,20]
list_str = ['Yui','Yuki','Gonhi']
data_list = list_num + list_str

[print(f'data = {i}')for i in list_num]
print(20*'~')
[print(f'data = {i}')for i in data_list]
print(20*'~')
angka_kuadrat = [i**2 for i in list_num]
print(angka_kuadrat)
print(20*'~')



from library.operasiMtk import Operator 

num1 = int(input('masukkan angka pertama :'))
num2 = int(input('masukkan angka kedua :'))

operator = Operator(num1,num2)

print(f"Hasil Pertambahan\t :{operator.tambah():,}")
print(f"Hasil Pengurangan\t :{operator.kurang():,}")
print(f"Hasil Perkalian\t\t :{operator.kali():,}")
print(f"Hasil Pembagian\t\t :{operator.bagi():,}")