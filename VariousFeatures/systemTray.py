from pystray import MenuItem as item
import pystray
import pyautogui as pg
from PIL import Image

def action():
    pass

def msgBox():
    pg.alert(text='Tui',title='Tip', button='Copy that')

image = Image.open("MatplotlibGraphics/drawCircle.png")
menu = (item('name', action), item('Tip', msgBox))
icon = pystray.Icon("name", image, "CtrlReplacer", menu)
icon.run()