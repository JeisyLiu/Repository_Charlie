import pyautogui as pg
x,y=pg.size()
print("the size of screen (Pixel)",pg.size())
print("position of cursor",pg.position())
print("now move cursor to Windows Icon and Click")
pg.moveTo(2,1078)#the pos can't be 0 or maxsize
pg.click()
print("move cursor to center and press left button twice")
pg.click(x/2,y/2,button='right',clicks=1)

'''
detail in this site
https://pyautogui.readthedocs.io/en/latest/mouse.html
'''