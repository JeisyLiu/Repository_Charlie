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


# change file name extensions in the dir and sub dir
def replaceExtension(root_dir):
    files = os.listdir(root_dir)

    for i in files:
        if (i.__contains__('.java')):
            tar_filename = i.replace('.java', '.cs')
            
            print (tar_filename)
            os.rename(root_dir +'//' + i, root_dir + '//' + tar_filename)
            continue
        if not (i.__contains__('.')):
            sub_dir = root_dir + "//" + i
            replaceExtension(sub_dir)
            pass


tar_path = 'E://Project//Q1_SDK//Code//q1-sdk-win-3.0//LogicLayer//Q1SDK-Client//Q1SDK-Client//pay'

replaceExtension(tar_path)
