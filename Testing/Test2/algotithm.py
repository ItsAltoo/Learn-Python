# fibonacci

num1 = 0
num2 = 1

print(num1)
print(num2)
for i in range(10):
    newnum = num1 + num2
    print(newnum)
    num1 = num2
    num2 = newnum
    
print(20*'- ')

def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

print(F(19))
    
print(20*'- ')

#DSA Array
my_array = [6,6,3,8,5,7]
nilai_awal = my_array[0]

for i in my_array:
    if i < nilai_awal:
        nilai_awal = i
        
print(nilai_awal)