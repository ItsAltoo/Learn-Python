import os
os.system('cls')


class DataMhs:
    def __init__(self,matkul : str,sks:int,waktu:int):
        self.matkul = matkul
        self.sks = sks
        self.waktu = waktu

class Jadwal(DataMhs):
    def __init__(self, matkul, sks, waktu):
        super().__init__(matkul, sks, waktu)
    
    def addData(self):
        with open('./dataJadwal,txt','a')as file:
            file.write(f"Matkul : {self.matkul} , SKS : {self.sks} , Waktu : {self.waktu} menit \n")
    
    def showData(self):
        try:
            with open('./dataJadwal,txt','r')as file:
                print(file.read())
        except:
            print('File tidak di temukan')


while True:
    matkul = input("Masukkan Matkul : ")
    sks = input("Masukkan SKS : ")
    waktu = input("Masukkan Waktu : ")

    dataMatkul = Jadwal(matkul,sks,waktu)

    dataMatkul.addData()
    dataMatkul.showData()
