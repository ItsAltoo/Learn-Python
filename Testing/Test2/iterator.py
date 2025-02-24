data = (12,421,"Number", 3.14)

iterData = iter(data)

print(next(iterData))
print(next(iterData))
print(next(iterData))
print(next(iterData))

print('~'*8)

class Myiter:
    def __iter__(self):
        self.a = 1
        return self
        
    def __next__(self):
        if self.a <= 50:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

classIter = Myiter()
newIter = iter(classIter)



print(next(newIter))
print(next(newIter))
print(next(newIter))
print(next(newIter))
print(next(newIter))

print("~"*8)

for x in range(0,10):
    print(next(newIter))

print("~"*8)

for x in newIter:
    print(x)

print("~"*8)
