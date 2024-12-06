class  Object :
    nama = "malik"
    umur = 18
    hobi = "art"
    def example(param):
        return print('this function %s' % param.nama)
        
# print(Object.example())

newObject = Object()

print(newObject.example())
