class Mhs:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim
        
class Data(Mhs):
    def __init__(self,nama,nim,time):
        Mhs.__init__(self,nama,nim)
        self.time = time
        
    @property
    def info(self):
        return "nama : {} , nim : {} , time : {}".format(self.nama,self.nim,self.time)
    
yuki = Data('malik',2342,12)
print(yuki.info)