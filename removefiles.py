import time
import os
import shutil

path = input("Enter file path")
days = int(input("How old do you want a folder to be to get deleted"))
seconds = time.time()-int((days)*24*60*60)
def getctime(): 
    ctime = os.stat(path).st_ctime
    return ctime

def removePath(path):
    os.remove(path)

def doesPathExist():
      os.path.exists(path)
if doesPathExist == "true":
    for root_folder, folder,files in os.walk(path):
        if seconds>= getctime(root_folder):
            removePath(path)
        else:
            print("Path not found")

          




    





    

