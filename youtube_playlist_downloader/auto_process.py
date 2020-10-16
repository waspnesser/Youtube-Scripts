from sorted_copy import inFolder
from YOUTUBE import playlist_download
from set_image import set_image
from urllib.request import urlretrieve
import os


download_image = lambda url,output:urlretrieve(url,output)

raw = "/home/brad/Music/"
path_up = input("Where download :Music/")
if path_up[-1] != "/":
	path_up += "/"
path = raw+path_up

if not os.path.isdir(path):
	raise Exception("Invalid Path -> {} ".format(path) )

url = input("Playlist URL : ")
info = playlist_download(url,path = path)
folder_name = "{}-{}".format(info["title"],info["uploader"])# Sondaki boşluğa dikkat
folder_path = path + folder_name + "/"
response = input("Would  you like to put image for playlist cover in to the downloaded folder (y/n) : "  )
if response == "y":
	t_img = input("Local or URL ?(local -> 0;URL -> 1) :  ")
	if t_img == "1":
		flag  = 0
		while not flag:
			img_url = input("Image url : ")
			ext = input("Would you enter extension of image (by short .???) : ")
			if ext[0] != ".":
				ext ="."+ext
			img_path  = folder_path + "cover"+ext
			try:
				download_image(img_url,img_path)
			except Exception as err:
				print(err," ==> Please try again...")
				continue

			set_image(img_path,folder_path)
			flag = 1
	else:
		img_name = input("Please put your local image to \n {}\n folder. If you putted image to specified path\n Please write image name: ".format(folder_path) )
		img_path = folder_path+img_name
		if os.path.isfile(img_path):
			set_image(img_path,folder_path)
		else:
			raise Exception("Image not found!")

mp3Path = "/run/media/dolores/A422-E6CD/"
#Bundan sonrası sıkıntılı
if os.path.ismount(mp3Path):

	send_Response = input("Would you like to update mp3 player (y/n) : ")
	if send_Response == "y":
		print("SOURCE : ",raw,"\nTARGET : ",mp3Path)
		inFolder(raw,mp3Path)

	

else:
	pass
