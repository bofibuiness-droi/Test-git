import shutil
import os


with open("core/text.txt", "w") as file:
    file.write("hello,python!\n")
    file.write("file handling is easy with python")
print("file written successfully")

source = 'core/text.txt'
destiantion = 'core/text'

shutil.move(source, destiantion)

keep = input("do you want to keep this text file: (y/n)")
if keep == "y":
    os.remove("core/text/text.txt")
    print("file as been deleted!")
else:
    print("okay:)")