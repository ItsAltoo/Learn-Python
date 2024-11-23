import datetime as time


date = int(input("masukkan Tanggal \t:"))
month = int(input("masukkan Bulan \t\t:"))
year = int(input("masukkan Tahun \t\t:"))

born = time.date(year,month,date)

print(f"{born:%A}")

today = time.date.today()

ageDay = today - born
ageYear = ageDay.days // 365

print(f"{born:%A}")
print(ageYear)

