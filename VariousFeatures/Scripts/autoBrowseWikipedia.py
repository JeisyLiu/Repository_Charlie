import subprocess as sp
import keyboard
import time
import pyautogui as pg

sp.call("D:\\applications\\firefox\\firefox.exe")
time.sleep(5)
keyboard.press_and_release('Ctrl + L')
time.sleep(1)
pg.typewrite("wikipedia.org")
keyboard.press_and_release('Enter')