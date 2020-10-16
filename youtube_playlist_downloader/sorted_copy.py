from shutil import copyfile 
import os

def inFolder(path,target): # Sıkıntı : Klasör İçindeki her şeyi koyalıyor.Bunu Çöz
    dir_check = 0 
    file_check = 0 
    for i in sorted(os.listdir(path)): 
        if os.path.isdir(path+i): 
            try: 
                os.mkdir(target+i) 
                print("[MKDIR] {} created .".format(target+i))
            except FileExistsError: 
                pass 
                 
            inFolder(path+i+"/",target+i+"/") 
        elif os.path.isfile(path+i):
            if os.path.isfile(target+i):
                continue
            else:
                print("[COPY] {} -> {}".format(path+i,target+i))
                copyfile(path+i,target+i) 
        else: 
            raise Exception("Unknown situation...") 

if __name__ == "__main__":
    path = "/home/brad/Music/"
    target = "/run/media/dolores/A422-E6CD/"
    inFolder(path,target)