from __future__ import unicode_literals
import youtube_dl
from os import chdir,listdir
from subprocess import call

def mp3Download(urlList,path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        chdir(path)
        try:
            ydl.download(urlList)
        except youtube_dl.utils.DownloadError:
            pass
        
        controlList = list()

        for url in urlList:
            info_dict = ydl.extract_info(url, download=False)
            #video_url = info_dict.get("url", None)
            video_id = info_dict.get("id", None)
            video_title = info_dict.get('title', None)
            filename = str(video_title)+"-"+str(video_id)+".mp3"
            if filename in listdir(path):
                call("notify-send --urgency=normal --expire-time=120 'Youtube Download' '{} named video downloaded and converted mp3 file type.Procces is completed'".format(video_title),shell = True)
                controlList.append(1)
            else:
                call("notify-send --urgency=critical --expire-time=120 'Youtube Download' '{} named video downloading process is not completed successfully.Duty Crashed...'".format(video_title),shell = True)
                controlList.append(0)
        
        if not(0 in controlList):

            call("python /home/wasptheslimy/Desktop/youtube_Downloader/alertCodes.py 'Process is Completed.' 'Video List Download and Convert process is successfully completed' 1",shell = True)
        else:
            #DownList = list()
            #ErrorList = list()    
            #for controlVar,url in zip(controlList,urlList):

            call("python /home/wasptheslimy/Desktop/youtube_Downloader/alertCodes.py 'Process is inCompleted.' 'Video List Download and Convert process is not successfully completed.Some Videos Crashed,Not All.Maybe All I dunno .' 0",shell = True)



