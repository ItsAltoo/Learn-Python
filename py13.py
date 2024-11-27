data = 'my name is Malik,Nim 1250,True,False,aAWs'
dictionary = {
    'name' : 'malik',
    'age' : 18,
    'hobby' : 'awda'
}


print('new line \r awds \n asdwk\r\n')

print('total karakter', len(data))
print(r'data[0:41:3]')
print(f'{data[0:41:3]}')
print(data[0:-32])

asci = ord('w')
print(asci)
char = 92
print(chr(char))
print(data.count('i'))
txt = 'awdksadaw'
print(txt.islower())
txt = "AWDASDWA"
print(txt.isupper())
txt = 'wqeqdsdq'
print(txt.isalpha())
txt = '12381sdawed12'
print(txt.isalnum())
txt = '12312423'
print(txt.isdigit())
newData = ' '
print(newData.isspace())
txt = 'Awod Aodwkas Wad'
print(txt.istitle())

list = ['appel','mangga','jeruk']

combine = ' dan '.join(list)
print(combine)

combine = 'appelwasdjerukwasdmanggaaa'
print(combine.split('wasd'))


kanan  = 'kanan'.rjust(10,'=')
print("'"+kanan+"'")

kiri  = 'kiri'.ljust(10)
print("'"+kiri+"'")

tengah  = 'tengah'.center(20,'~')
print("'"+tengah+"'")

tengah  = 'tengah'.strip('~')
print("'"+tengah+"'")

kiri  = 'kiri'.strip()
print("'"+kiri+"'")

dataTeman = {
    "nama" : 'malik',
    "age" : 18,
    'hobby': 'code',
    'location' : 'unknown'
}

for i in dataTeman:
    print(i)
    
print(20*'~')
print(dataTeman.keys())
for key in dataTeman.keys():
    print(dataTeman.get(key))

print(20*'~')
for value in dataTeman.values():
    print(value)

print(20*'~')
print(dataTeman.items())
for item in dataTeman.items():
    print(item)
    
print(20*'~')
for key,value in dataTeman.items():
    print(f"key = {key},value = {value}")