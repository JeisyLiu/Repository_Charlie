import os

apples=open("newfile.txt","w+")
os.makedirs("godknows")
for i in range(10):
    apples.write("This is line %d\r\n" % (i+1))
apples.close()