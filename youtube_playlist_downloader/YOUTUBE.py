import youtube_dl
import time

def playlist_download(url,path = "~/Music/"):
    start = time.time()
    outtmpl = path + "%(playlist_title)s-%(playlist_uploader)s/%(playlist_index)s %(title)s-%(uploader)s.%(ext)s"
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
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(url,download = True)# Title and Uploader is important

    end = time.time()
    print("Playlist Download Process Completed in {} second.".format(end-start))
    return info

if __name__ == "__main__":
    url = input("Enter url : ")
    info = playlist_download(url)



