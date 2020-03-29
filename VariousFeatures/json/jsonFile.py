import testb
import platform
import os
import time
import bs4
import json

#apples = '{"title":"merci", "length":30, "path":"E://echo"}'
file = open("tmp.txt", 'r')
apples = file.read()
butter = {"username":"danke", "weight":10, "mark":.38}
x = json.dumps(butter)
y = json.loads(apples)
print("apples is ", apples)
print(y["title"])
print(x)

'''print("system info", platform.uname())
#time.sleep(2)
print("runned time", os.times())'''