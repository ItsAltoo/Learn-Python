isiBelanjaan = []

while True:
    print("~~~~~~~~~~~Pilih Belanjaan Anda~~~~~~~~~~~~")
    print("1.Keyboard           5.Mouse Pad")
    print("2.Monitor            6.Ram")
    print("3.Mouse              7.Cek Belanjaan")
    print("4.Laptop             8.Keluar")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    pilih = input("Pilih Pilihan anda 1-8 :")
    
    if pilih == "1":
        pilih = "Keyboard"
        isiBelanjaan.append(pilih)
        print("=======================================================")
        print(f"Anda Telah Memilih : '{pilih}' ")
        
    elif pilih == "2":
        pilih = "Monitor"
        isiBelanjaan.append(pilih)
        print("=======================================================")
        print(f"Anda Telah Memilih : '{pilih}' ")
        
    elif pilih == "3":
        pilih = "Mouse"
        isiBelanjaan.append(pilih)
        print("=======================================================")
        print(f"Anda Telah Memilih : '{pilih}' ")
        
    elif pilih == "4":
        pilih = "Laptop"
        isiBelanjaan.append(pilih)
        print("=======================================================")
        print(f"Anda Telah Memilih : '{pilih}' ")
        
    elif pilih == "5":
        pilih = "Mouse Pad"
        isiBelanjaan.append(pilih)
        print("=======================================================")
        print(f"Anda Telah Memilih : '{pilih}' ")
        
    elif pilih == "6":
        pilih = "Ram"
        isiBelanjaan.append(pilih)
        print("=======================================================")
        print(f"Anda Telah Memilih : '{pilih}' ")
        
    elif pilih == "7":
        loop = True
        while loop:
            print("\n==================Daftar Belanjaan====================")
            for i,memilih in enumerate(isiBelanjaan,1):
                print(f"{i}. {memilih}")
            print("=======================================================")
            
            print("Ketik 'y/n' untuk keluar atau tidak")
            exit = input("Exit? :")
            
            if exit == "y":
                break
            elif exit == "n":
                print("=======================================================")
                print("Exit dibatalkan, ketik y/n untuk memilih exit")
            else:
                print("=======================================================")
                print("Masukkan input yang benar")
                
    elif pilih == "8":
        print("=================Terima Kasih Telah Mencoba=================")
        break
    else: 
        print("=======================================================")
        print("Tolong masukkan pilihan 1-8")
