name = "Malik"
age = 18
hobby = "fishing"
makanan = "Sop Kura-kura"

data = f"my name  = {name}, my age {age}, my hobby = {hobby}"
print(data)

print(""+10*"~"+f" saya adalah {name} "+10*"~"+"\n"+10*"~"+f" umur saya {age} "+10*"~"+"\n"+10*"~"+f" hobi saya {hobby} "+10*"~"+"")

print("\n"+15*"-"+"Batas"+15*"-")

print( f""" 
nama saya = {name}
    umur = {age}
        hobi = {hobby}
""")

print("\n"+15*"-"+"Batas"+15*"-")

print( f""" 
nama saya = {name:>5}
umur = {age:10}
hobi = {hobby:>15}
makanan = {makanan:>15}
""")

print("\n"+15*"-"+"Batas"+15*"-")

#Bilangan dengan ordo ribuan
num = 123213 * 122
print(f"{num:,}")

print("\n"+15*"-"+"Batas"+15*"-")

#bilangan desimal
num = 232123.42421
print(f"{num:.3f}")
print(f"{num:,.3f}")