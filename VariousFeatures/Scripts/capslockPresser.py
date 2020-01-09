import keyboard
import time
while True:
    while keyboard.is_pressed('capslock'):
        print('rero')
        time.sleep(2)
        keyboard.press_and_release('capslock')
        break