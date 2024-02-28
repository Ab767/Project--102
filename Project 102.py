import os

import shutil
source = "/Users/aarushbathula/Downloads/abc"
destination = "/Users/aarushbathula/Desktop"
files = os.listdir(source)
print(files)
for i in files:
    name,ext = os.path.splitext(i)
    if ext == "":
        continue
    if ext in[".zip",".docx",".pdf",".doc"]:
        path1 = source + "/" + i
        path2 = destination + "/" + "Document_files"
        path3 = destination + "/" + "Document_files" + "/" + i

        if os.path.exists(path2):
            print("folder already exist and moving the files")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Creating the folder and moving the files")
            shutil.move(path1,path2)
