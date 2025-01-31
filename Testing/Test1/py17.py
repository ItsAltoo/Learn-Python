
# Sort dengan lambda
listw = ["Otong","Ucup","Dudung"]

listw.sort(key=lambda inpt : len(inpt))
print(listw)


# Filter dengan lambda
num = [1,2,3,4,5,5,2,5,7,5,9,7,6,4,6]

new_num = list(filter(lambda x:x<7,num))
print(new_num)

# Bilangan Genap dengan lambda
even_num = list(filter(lambda x:(x % 2 == 0),num))
print(even_num)

# BIlangan Ganjil dengan lambda
odd_num = list(filter(lambda x : (x % 2 != 0),num))
print(odd_num)

# anonymous function

# anonymous function dengan currying 
def pangkat(n):
    return lambda angaka : angaka ** n

pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")
print(f"pangkat 2 = {pangkat(2)(5)}")


pangkat5 = pangkat(5)
print(f"pangkat 5 = {pangkat5(5)}")
print(f"pangkat 5 = {pangkat(5)(5)}")



print(25*'~')



## Global dan Local Scope

name = 'Yuki' # <- ini adalah variable global

# akses variable global dalam fungsi
def function():
    print(f'Hallo my name is {name}')
    
function()

# akses varibale global dalam loop

for i in range(1,5+1):
    print(f'loop {i} - {name}')


# Percabangan
if True:
    print(name)
    


## Variable local scope

def fungsi():
    nama = 'Yui' # <- variable local scope 

fungsi()
# print(nama) <- tidak bisa di gunakan

# Contoh 1: penggunaan akses variable
def sayHello():
    print(f'Hello {nick}')
    
nick = 'Luan'
sayHello()
# nick = 'Luan' <- Error jika diletakkan di bawah panggilan fungsi

# Contoh 2: Merubah variable global
angka = 2
nama = 'Ichi'

def change_num(num,new_nama):
    global angka,nama
    angka = num
    nama = new_nama

print(angka,nama)
change_num(20,"Hogo")
print(angka,nama)

# Contoh 3:
angka = 0

for i in range(0,5):
    angka += i
    lkw = 12312
    
print(angka)
print(lkw)

if True:
    angka = 10
    lkw = 10

print(angka)
print(lkw)



# Contoh sederhana untuk menangkap exception
from math import nan


inpt = int(input("masukkan angka :"))
output = nan

try:
    output = 10/inpt
except:
    print("Program Error")
    
print(output)


# Contoh di aplikasi

while True:
    agka = int(input('Masukkan Angka Pembagi :'))
    try:
        hasil = 10/agka
        print(f"hasil {hasil}")
        done = input('lanjut? y/n :')
        if done == 'n' or done == "N":
            break
    except:
        print('pembagi nol,silahkan masukkan input lagi..')
        
print('terima kasih')