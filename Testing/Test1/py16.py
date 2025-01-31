from os import system
system("cls")

def tambah(*args):
    """ *args """
    inpt = 0
    for i in args:
        inpt += i
        
    return inpt

print(f"hasil tambah = {tambah(12,23,2,1)}")



def kali(*angka):
    """ *args """
    inpt = 1
    for i in angka:
        inpt += i
        
    return inpt

print(f"hasil Kali = {kali(12,23,2,1)}")


# **kwargs

def bagi(**kwargs):
    """ **kwargs """
    angka_pertama = kwargs['angka1']
    angka_kedua = kwargs['angka2']
    angka_ketiga = kwargs['angka3']
    
    bagi = angka_pertama / angka_kedua / angka_ketiga
    print(bagi)

bagi(angka1 = 20,angka2 = 5,angka3 = 1)

def bagi(**inputan: int)-> int:
    """ **kwargs """
    angka_pertama = inputan['angka1']
    angka_kedua = inputan['angka2']
    angka_ketiga = inputan['angka3']
    
    bagi = angka_pertama / angka_kedua / angka_ketiga
    print(bagi)

bagi(angka1 = 50,angka2 = 5,angka3 = 2)


# fungsi *args dan **kwargs

def  math(*angka,**operasi):
    output = 0
    if operasi['operator'] == "tambah":
        for i in angka:
            output += i
    elif operasi['operator'] == 'kali':
        output = 1
        for i in angka:
            output *= i
    else:
        print("Operasi Gagal")
    return output

opTambah = f"Hasil Dari Pertambahan = {math(1,23,4,5,operator = "tambah")}"

opKali = f"Hasil Dari Perkalian = {math(1,23,4,5,operator = "kali")}"


# path = "db/py16/db.txt"
# with open(path,'a') as file:
#     file.write(f"{opTambah}\n{opKali}\n\n")

# with open(path,'r')as file:
#     print(file.read())
