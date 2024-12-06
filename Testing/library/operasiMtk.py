from numbers import Number

class Operator:
    def __init__(self,a,b):
        if not isinstance(a,Number) or not isinstance(b,Number):
            raise "inpt harus angka"
        self.num1 = a
        self.num2 = b

    def tambah(self)-> int:
        """ Ini adalah Operator Pertambahan """
        return self.num1 + self.num2
    
    def kurang(self)->int:
        """ Ini adalah Operator Pengurangan """
        return self.num1 - self.num2
    
    def kali(self)-> int:
        """ Ini adalah Operator Perkalian """
        return self.num1 * self.num2
    
    def bagi(self):
        """ Ini adalah Operator Pembagian """
        return self.num1 / self.num2


# operator_tambah = Operator(2,2) # <- param tersebut mengarah ke def __init__,tidak ke tambah
# operator_kurang = Operator(2,2)


# # print(Operator.tambah(2,2)) <- jika di lakukan seperti ini akan menyebabkan error
# print(operator_tambah.tambah())
# print(operator_kurang.kurang())