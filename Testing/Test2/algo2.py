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