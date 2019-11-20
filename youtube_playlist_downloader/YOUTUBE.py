import youtube_dl
import os 
outtmpl = "%(playlist_title)s-%(playlist_uploader)s /%(playlist_index)s %(title)s-%(uploader)s.%(ext)s"
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    },
        {'key': 'FFmpegMetadata'},
    ],
    'outtmpl' : outtmpl,
}

url = input("Enter url : ")

with youtube_dl.YoutubeDL(ydl_opts) as ydl:

    ydl.download([url]) 

