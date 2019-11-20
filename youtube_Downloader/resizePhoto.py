
#AUTHOR IS NOT ME "WASP"
# UNNOUN AUTHOR?
from PIL import Image
 
def resize_image(input_image_path,
                 output_image_path,
                 size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size 
    resized_image = original_image.resize(size)
    width, height = resized_image.size
    #resized_image.show()
    resized_image.save(output_image_path)
 
if __name__ == '__main__':

    from sys import argv,exit

    try:
        inputPath,outputPath,width,height= argv[1],argv[2],int(argv[3]),int(argv[4])
        size = (width,height)
    except IndexError:
        print("[ERROR] There is undefined arguments exists.You must fill it.")
        exit()



    resize_image(input_image_path=inputPath,
                 output_image_path=outputPath,
                 size=size)#Size must be like (300,128) Blah Blah Blah