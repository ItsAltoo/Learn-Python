import numpy as np

a = np.array([[7,4,2,0,4],[1,2,4,5,5]])
b = np.array([[7,4,2,0,4],[1,2,4,5,5]])
c = np.array([4,3,1,5,1])

count = a + b

print(count)
print(15*' - ')

matriksA = np.ones([5,4])

print(matriksA)
print(15*'-')
print(matriksA + 2)
print(15*'-')
print(f"jumlah array : {a.ndim}")
print(f"ukuran array :{a.shape}")
print(f"jumlah isi array atau jumlah elemen :{a.size}")
print(f"type : {a.dtype}")

print(15*'-')

zerosA = np.zeros(2)
print(zerosA)
onesA = np.ones(2)
print(onesA)
empytA = np.empty(3)
print(empytA)
arrageA = np.arange(4)
print(arrageA)
arrageB = np.arange(0,20,5)
print(arrageB)