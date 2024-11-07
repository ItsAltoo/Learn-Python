num1 = int(input(f"masukkan angka untuk alas anda :"))
num2 = int(input(f"masukkan angka untuk tinggi anda :"))


def segt (a,t):
    count = 1/2 * a * t
    print(count)
    
segt(num1,num2)



def data_akun() :
    return {"rofil": "12345", "rangga": "t503"}

def cek_akun(username, passowrd) :
    if username in data_akun() and password in data_akun().values():
        return True;
    return False;
    
    
username = input("Masukan username Anda? ")
password = input("Masukan password Anda? ")

if(cek_akun(username, password) == True) :
    print("Selamat Datang %s" % username)
else:
    print("Username dan Password Salah")

def garis(panjang, simbol) :
    print(simbol * panjang)
    
def tampilkan_menu_makanan():
    garis(26, "-")
    print("1. Nasi Ayam Rp. 10.000")
    print("2. Bakso Rp. 12.000")
    print("3. Es Teh Rp. 4.000")
    print("4. Sate Madura Rp. 25.000")
    print("0. Exit ")
    garis(26, "-")

pesanan = ""

while pesanan != "0":
    tampilkan_menu_makanan()
    pesanan = input("Masukan Kode Pesanan? ")
    garis(26, "-")

hello = lambda : "Hello World"
print(hello())

cek_bilangan_genap = lambda angka : angka <= 5
print(cek_bilangan_genap(2))

angka_ajaib = [1, 2, 3, 4, 5, 6, 7, 8]

print(list(map(lambda angka : (angka * 2),
angka_ajaib)))
print(list(filter(lambda angka : angka <= 5,
angka_ajaib)))

def garis(panjang = 10, style = "-") :
    print(style * panjang)
    
garis(50, "=")
print("Daftar Pesanan Anda")
garis(50, "*")
print(" 1. Ayam Potong Rp. 15.000,00")
print(" 2. Ayam Goreng Pedas Rp. 12.000,00")
garis(50,"-")
print("Total :Rp. 27.000,00")
garis(50,"=")
garis(15, "*")
garis()

nn = "=================================================="

print(len(nn))