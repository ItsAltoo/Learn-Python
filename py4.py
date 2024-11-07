buah = {"apel","mangga","jambu","kiwi",21,False}

print(f"buah = {len(buah)}")
print("Jumlah = %d" % len(buah))
print(buah)


for i in buah:
    print(i)

buah.add("iya")
print(buah)


buah.clear()
print(buah)

x = {4,5,2}
y = {8,3,5}
z = y.difference(x)
print(z)
