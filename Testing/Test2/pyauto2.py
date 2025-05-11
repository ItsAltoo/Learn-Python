import pyautogui
import time

def auto_interact():
    print("Memulai interaksi otomatis dalam 3 detik...")
    time.sleep(3)
    
    # mencari coordinasi cursor atau posisi cursor
    previousMouseX, previousMouseY = pyautogui.position()
    coor = True
    idle_count = 0
    idle_limit = 5  # Batas iterasi sebelum dianggap berhenti

    while coor:
        currentMouseX, currentMouseY = pyautogui.position()
        
        if (currentMouseX, currentMouseY) == (previousMouseX, previousMouseY):
            idle_count += 1
        else:
            idle_count = 0
        
        if idle_count >= idle_limit:
            print("Mouse berhenti bergerak. Menghentikan loop.")
            coor = False
        else:
            print(f"X : {currentMouseX}, Y : {currentMouseY}")
            previousMouseX, previousMouseY = currentMouseX, currentMouseY
        
        time.sleep(0.5)  # Tambahkan jeda untuk mengurangi beban CPU
    
    # Auto Copy-Paste
    for i in range(5):
        pyautogui.hotkey('ctrl','a')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl','c')
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl','v')
        print(f'copy ke :{i+1}')

    

auto_interact()