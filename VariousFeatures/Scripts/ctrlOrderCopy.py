import os
import keyboard
import pyautogui
import threading
import time

resetmark = False
ctrlbuffer = ['a', 'a', 'a', 'a']

def shutter():
    global resetmark
    resetmark = True
    global ctrlbuffer
    ctrlbuffer = ['a', 'a', 'a', 'a']
    print('a thread finished')

def changer(x, i):
    global ctrlbuffer
    ctrlbuffer[i] = x

def matching(x):
    if ''.join(ctrlbuffer) == x:
        print("detected, saving")
        keyboard.press_and_release("ctrl + c")
        
        time.sleep(1)

timer = threading.Timer(2, shutter)

timer.start()

while True:
    if keyboard.is_pressed('c'):
        changer('c', 0)
        time.sleep(.2)
        print('c')
        print("".join(ctrlbuffer))

    if keyboard.is_pressed('t'):
        changer('t', 1)
        time.sleep(.2)
        print('t')
        print("".join(ctrlbuffer))

    if keyboard.is_pressed('r'):
        changer('r', 2)
        time.sleep(.2)
        print('r')
        print("".join(ctrlbuffer))

    if keyboard.is_pressed('l'):
        changer('l', 3)
        time.sleep(.2)
        print('t')
        print("".join(ctrlbuffer))

    matching('ctrl')

    if resetmark:
        othertime = threading.Timer(2, shutter)
        othertime.start()
        resetmark = False
