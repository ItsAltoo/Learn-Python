import pyautogui
import time

def auto_interact():
    try:
        # Delay untuk mempersiapkan perangkat
        print("Memulai interaksi otomatis dalam 3 detik...")
        time.sleep(3)
        
        # 1. Gerakkan mouse ke posisi tertentu
        print("Menggerakkan mouse ke posisi (100, 200)...")
        pyautogui.moveTo(100, 200, duration=1)  # Pindah ke koordinat (100, 200) dalam 1 detik

        # 2. Klik di posisi tersebut
        print("Melakukan klik di posisi (100, 200)...")
        pyautogui.click()

        # 3. Mengetik teks
        print("Mengetik teks: 'Hello, world!'")
        pyautogui.typewrite("Hello, world!", interval=0.1)  # Mengetik dengan jeda 0.1 detik per karakter

        # 4. Menekan tombol Enter
        print("Menekan tombol ENTER...")
        pyautogui.press('enter')

        # 5. Mengambil screenshot layar
        print("Mengambil screenshot layar...")
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        print("Screenshot disimpan sebagai 'screenshot.png'.")

        print("Interaksi otomatis selesai!")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Jalankan fungsi
auto_interact()
