import os
currentfilelist=os.listdir("MultiFiles")

targetfilelist = os.listdir("E:\PythonProjects")

localfilelist=os.listdir(os.getcwd())

print("files in the folder where is in current directory:")
print(currentfilelist)
print("files in the accurate folder:")
print(targetfilelist)
print("files in the current directory:")
print(localfilelist)