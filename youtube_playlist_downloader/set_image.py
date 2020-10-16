
from mutagen.mp3 import MP3 
from mutagen.id3 import ID3, APIC, error 
import sys
import time
import os
get_ext = lambda  file_name : file_name.split(".")[-1]
def set_image(image:str,files:list): 
  start = time.time()
  for file in files:
     ext = get_ext(file)
     if ext != "mp3":
        continue
     else:

        audio = MP3(file, ID3=ID3) 
         
        # add ID3 tag if it doesn't exist 
        try: 
            audio.add_tags() 
        except error: 
            pass 
        audio.tags.add( 
            APIC( 
                encoding=3, # 3 is for utf-8 
                mime='image/{}'.format(get_ext(image)), # image/jpeg or image/png 
                type=3, # 3 is for the cover image 
                desc=u'Cover', 
                data=open(image,"rb").read() 
            ) 
        ) 
        audio.save()
        print("Image file {} has been embeeded to {} file.".format(image,file))
  
  end = time.time()
  print("Set Image Process Completed in {} second.".format(end-start))

if __name__ == "__main__":

  """
  argv[1] => image file
  argv[2:] => mp3 files
  """
  if len(sys.argv)>1:
    files = sys.argv[2:]
    image = sys.argv[1]
  else:
    image = input("Enter image file location : ")
    if not os.file.isFile(image):
      raise FileNotFoundError("Entered image file not found! ")
    else:
      files = list()
      FLAG = False

      while (not FLAG):
        ask_file = input("Enter mp3 file (Loop Termination Code : END000 )")
        if not os.file.isFile(ask_file):
          print("{} file does not exist.".format(ask_file))
          continue
      
        elif ask_file == "END000":
          print("Asking operation terminated.")
          FLAG = True

        else:
          files.append(ask_file)

  set_image(image,files)

