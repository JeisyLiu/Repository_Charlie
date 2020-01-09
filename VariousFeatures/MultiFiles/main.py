import Alpha
import container.Bravo

Alpha.os.mkdir("new")

with container.Bravo.mss.mss() as sct:
    filename = sct.shot(mon=-1, output='fullscreen.png')
    print(filename)