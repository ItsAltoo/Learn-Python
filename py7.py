def kubus (a) :
    count =  a * a * a
    print(count)

kubus(8)

def volume_balok(p,l,t,kode_balok = "TBxx"):
    volume = p * l * t
    print("volume balok dari balok %s adalah %d" % (kode_balok,volume))
volume_balok(12,7,3,)

def hitung(n):
    print(n)
    if n < 10:
        hitung(n + 1)
        
        
hitung(1)
