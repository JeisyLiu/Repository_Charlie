from mss import mss
import mss.tools

with mss.mss() as sct:

    monitor = {"top": 160, "left": 160, "width": 1280, "height": 720}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

    sct_img = sct.grab(monitor)

    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)