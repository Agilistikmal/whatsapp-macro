import pyautogui
import time

if __name__ == "__main__":
    # User input
    text = input(":: Masukkan teks => ")
    count = int(input(":: Masukkan jumlah pengiriman => "))
    time_delay = float(input(":: Masukkan delay (detik) => "))
    with_count = input(":: Tampilkan jumlah pengiriman? Contoh: Halo 1, Halo 2, ... (y/n) => ")
    is_with_count = True if with_count.lower() == 'y' else False

    loc_file_sticker_input = pyautogui.locateOnScreen('data/file_sticker_input.png')

    for i in range(count):
        # Move to text input
        pyautogui.moveTo(loc_file_sticker_input)
        pyautogui.moveRel(100, 0)
        pyautogui.click()

        # Send text
        pyautogui.typewrite(text, interval=0.05)

        if is_with_count:
            pyautogui.typewrite(f" {i+1}")

        pyautogui.press('enter')

        time.sleep(time_delay)

    print(":: Selesai")
    
