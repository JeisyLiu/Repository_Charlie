import mss
import os
with mss.mss() as sct:
    filename = sct.shot(mon=-1, output='fullscreen.png')
    print(filename)
