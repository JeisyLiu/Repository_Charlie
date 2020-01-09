import os
tempfile=open("temp","w+")
print("temp file is created, plz check out ur folder")
tempfile.close()
input("press any key to delete")
os.remove("temp")
print("deleted successfully")