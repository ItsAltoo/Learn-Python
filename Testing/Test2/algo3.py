class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    

st = Stack()
st.push('abc')
st.push('abc')
st.push('abc')
print(st.items)
print(st.peek())

print(int(5**0.5))

data = {"name":"yui","age":12}

print(data['name'])
print(data['age'])

print("~" * 20)

# Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        print(f"Outer loop {i}: {arr}")
        for j in range(0, n-i-1):
            print(f"Inner loop {j}: {arr}")
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([5, 1, 4, 2, 8]))

