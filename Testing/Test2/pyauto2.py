import pyautogui
import time

def auto_interact():
    print("Memulai interaksi otomatis dalam 3 detik...")
    time.sleep(3)
    
    # previousMouseX, previousMouseY = pyautogui.position()
    # coor = True
    # idle_count = 0
    # idle_limit = 5  # Batas iterasi sebelum dianggap berhenti

    # while coor:
    #     currentMouseX, currentMouseY = pyautogui.position()
        
    #     if (currentMouseX, currentMouseY) == (previousMouseX, previousMouseY):
    #         idle_count += 1
    #     else:
    #         idle_count = 0
        
    #     if idle_count >= idle_limit:
    #         print("Mouse berhenti bergerak. Menghentikan loop.")
    #         coor = False
    #     else:
    #         print(f"X : {currentMouseX}, Y : {currentMouseY}")
    #         previousMouseX, previousMouseY = currentMouseX, currentMouseY
        
    #     time.sleep(0.5)  # Tambahkan jeda untuk mengurangi beban CPU
    
    pyautogui.click()

    

auto_interact()