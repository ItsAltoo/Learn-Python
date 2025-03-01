print('-'*8)

# Print the increasing pattern
for i in range(1, 6):
    print('* ' * i)
    if i == 5:
        # Print the decreasing pattern
        for j in range(4, 0, -1):
            print('* ' * j)


print('-'*8)
# Bubble sort algorithm 

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Sorted array:", my_array)

print('-'*8)

for i in range(1,10):
    if i % 2 != 0:
        print(i)
        
print('-'*8)

def luas_persegi(sisi):
    return sisi **2

print(luas_persegi(5))

print('-'*8)

# num = int(input('Masukkan Angka :'))

# if num < 0 :
#     print(f"Bilangan negatif {num}")
# elif num > 0:
#     print(f"Bilangan Positif {num}")
# else:
#     print("Bilangan Nol")
    
print('-'*8)

myList = [1,2,3,4,5]
total = 0

for i in myList:
    total += i
    
print(total)

print('-'*8)

name = input('Input Name :')
tukar = ''

for i in name:
    tukar = i + tukar
    
print(tukar)