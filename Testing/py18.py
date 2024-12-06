try:
    with open('Testing/db/py18/data.txt','r') as file:
        print(file.read())
except:
    print("file tidak ditemukan,sedang membuat file baru...")
    with open('Testing/db/py18/data.txt','w',encoding='utf-8') as file:
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

# num1 = int(input('masukkan angka pertama :'))
# num2 = int(input('masukkan angka kedua :'))

# operator = Operator(num1,num2)

# print(f"Hasil Pertambahan\t :{operator.tambah():,.2f}")
# print(f"Hasil Pengurangan\t :{operator.kurang():,.2f}")
# print(f"Hasil Perkalian\t\t :{operator.kali():,.2f}")
# print(f"Hasil Pembagian\t\t :{operator.bagi():,.2f}")


print(20*'~')


import numpy as np

vektorA = np.array([1,2,3,4])

print(f"ini adalah matrik vektor a = {vektorA}")
print(f"ini adalah matrik vektor a x 2 = {vektorA *2 }")
print(f"ini adalah matrik vektor a akar pangkat 2 = {vektorA ** 2}")

matrixB = np.array([(18,13,12,11),(12,32,8,23),(34,10,3,6),(2,6,3,9)])
print(f"matriks B = {matrixB}")
print(f"Matriks B akar kuadrat 2 =\n {matrixB ** 2}")

zerosC = np.zeros((4,4))
print(f"Zeros C =\n {zerosC}")
print(f"Zeros C + 3 =\n {zerosC + 3}")

onesD = np.ones((4,4))
print(f"ones D =\n {onesD}")
print(f"ones D + 4 =\n {onesD + 2}")


matrixTime = matrixB + matrixB**2 + onesD

print(f"hasil perkalian matrix =\n {matrixTime}") #<- Ordo matriks harus sama