from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap,QGradient

from MainMp3Motor import mp3Download
from newPath import PathPage
from listMod import ListDownload

from sys import exit

class YTD(QWidget):
    def __init__(self,path = "home/wasptheslimy/Music/YoutubeDownloads/"):
        super().__init__()
        self.setStyleSheet("background-color:  #697268")
        self.path = path
        self.resize(480,140)
        self.initUI()
        self.setWindowTitle("Youtbe Downloader")
    def initUI(self):
        

        self.verticalLinkLayout = QVBoxLayout()


        self.headerHorizantalLayout = QHBoxLayout()

        self.headerHorizantalLayout.addStretch()
        
        cssTitle = """
        font-family: 'Aguero Serif';
        font-size:48px;
        background-color: 	#4e5340;
        color :#fffcf4;
        padding-top : 8px;
        padding-bottom : 8px;
        padding-left:12px;
        padding-right:12px;
        border-style: solid;
        border-width: 4px;
        border-color : #22181c;
        """
        cssIcon = """
        background-color:#fffcf4;
        padding = 1px;
        border-style: solid;
        border-width: 4px;
        border-color : 	#4e5340;
        border-radius:25px;
        """

        self.YoutubeIcon = QLabel()
        self.YoutubeIcon.setPixmap(QPixmap("/home/wasptheslimy/Desktop/youtube_Downloader/Icons/youtubeAdjusted.png"))
        self.YoutubeTitle = QLabel()
        self.YoutubeIcon.setStyleSheet(cssIcon)
        self.YoutubeTitle.setStyleSheet(cssTitle)
        self.YoutubeTitle.setText("Youtube Downloader")
        self.headerHorizantalLayout.addWidget(self.YoutubeIcon)
        self.headerHorizantalLayout.addWidget(self.YoutubeTitle)
        #self.headerHorizantalLayout.

        self.headerHorizantalLayout.addStretch()


        self.verticalLinkLayout.addLayout(self.headerHorizantalLayout)

        cssLinkLabel = """
        background-color:#240b36;
        color: 	#f2dc5d;
        border-style: solid;
        border-width: 1px;
        border-color :#697268;
        border-radius: 5px;
        font-family:'Immani Demo';
        padding:5px;
        """

        cssVideoLink = """
        background-color:#f6e8ea;
        color:#22181c;
        border-style: solid;
        border-width: 2px;
        border-color :#697268;
        """

        self.LinkLayout = QHBoxLayout()

        self.LinkLabel = QLabel()
        self.LinkLabel.setText("Youtube Link : ")
        self.videoLink = QLineEdit("Enter the youtube link")
        self.LinkLayout.addWidget(self.LinkLabel)
        self.LinkLayout.addWidget(self.videoLink)
        self.verticalLinkLayout.addLayout(self.LinkLayout)
        self.verticalLinkLayout.addStretch()

        self.LinkLabel.setStyleSheet(cssLinkLabel)
        self.videoLink.setStyleSheet(cssVideoLink)

        self.path = self.getPath()
        

        cssPathLabel = """
        background-color:#f6e8ea;
        color:#22181c;
        border-style: solid;
        border-width: 2px;
        border-radius:1px;
        border-color :#5a0001;
        font-family:'Times New Roman', Times, serif;
        font-size:14px;
        """
        self.PathLabel = QLabel()
        self.PathLabel.setStyleSheet(cssPathLabel)
        self.Pathscheme = "Current Download PATH : {}"
    
        self.PathLabel.setText(self.Pathscheme.format(self.path))



        self.horizontalOptionLayout = QHBoxLayout()
        self.newPath = QPushButton("Enter New Path")
        self.newPath.setStyleSheet("background-color:#aac0aa;color:#405858;font-family:'Times New Roman', Times, serif;")
        self.newPath.clicked.connect(self.newPathFunction)
        self.listmod = QPushButton("List Download Mod")
        self.listmod.setStyleSheet("background-color:#aac0aa;color:#405858;font-family:'Times New Roman', Times, serif;")

        self.listmod.clicked.connect(self.listmodFunction)
        self.horizontalOptionLayout.addWidget(self.newPath)
        self.horizontalOptionLayout.addWidget(self.listmod)
        self.horizontalOptionLayout.addStretch()

        #QFileDialog./home/wasptheslimy/Desktop/

        self.horizontalControlLayout = QHBoxLayout()
        self.Download = QPushButton("Download")
        self.Download.setStyleSheet("background-color:#aac0aa;color:#202840;font-family:'Times New Roman', Times, serif;")
        self.Download.clicked.connect(self.DownFunc)

        self.Cancel = QPushButton("Cancel")
        self.Cancel.setStyleSheet("background-color:#aac0aa;color:#202840;font-family:'Times New Roman', Times, serif;")
        self.Cancel.clicked.connect(self.cancelFunc)
        self.horizontalControlLayout.addWidget(self.Download)
        self.horizontalControlLayout.addWidget(self.Cancel)

        self.verticalLinkLayout.addWidget(self.PathLabel)
        self.verticalLinkLayout.addLayout(self.horizontalOptionLayout)
        self.verticalLinkLayout.addStretch()
        self.verticalLinkLayout.addLayout(self.horizontalControlLayout)

        self.setLayout(self.verticalLinkLayout)

    def newPathFunction(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.pathUpdate)
        self.timer.start(1000)    

        self.popWindow = PathPage()
        #self.popWindow.setGeometry(548, 346, 303, 140)
        self.popWindow.show()

    def pathUpdate(self):
        if self.path != self.getPath():
            self.path = self.getPath()
            self.PathLabel.setText(self.Pathscheme.format(self.path))
            self.timer.disconnect()
        else:
            pass

    def getPath(self):
        with open("path.txt","r") as pathFile:
            self.path = pathFile.readlines()[-1][:-1]
        
        return self.path


    def cancelFunc(self):
        self.close()



    def DownFunc(self):
        url = self.videoLink.text()
        if 'www.youtube.com' in url.split("/"):
            mp3Download([url],self.path)
        else:
            print("[ERROR] Invalid URL")
            exit()
    
    def listmodFunction(self):
        self.popWindow = ListDownload(self.path)
        self.popWindow.show()        


    


