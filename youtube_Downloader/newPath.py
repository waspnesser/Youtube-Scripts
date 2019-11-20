from PyQt5.QtWidgets import *
from subprocess import call
import os


class PathPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Path")
        self.initUI()
    def initUI(self):
        self.VerticalLayout = QVBoxLayout()
        
        self.SeasonOfWitch = QLabel()
        self.SeasonOfWitch.setText("Enter the new Path : ")

        self.Path = QLineEdit()
        self.Path.setText("Path")

        self.horizontalControlLayout = QHBoxLayout()
        self.updateWidget = QPushButton("Update")
        self.updateWidget.clicked.connect(self.update)

        self.Cancel = QPushButton("Cancel")
        self.Cancel.clicked.connect(self.cancelFunc)
        self.horizontalControlLayout.addWidget(self.updateWidget)
        self.horizontalControlLayout.addWidget(self.Cancel)


        self.VerticalLayout.addWidget(self.SeasonOfWitch)
        self.VerticalLayout.addWidget(self.Path)
        self.VerticalLayout.addLayout(self.horizontalControlLayout)

        self.setLayout(self.VerticalLayout)

    def cancelFunc(self):
        self.close()
    
    def pathControl(self,path):
        currentPath = os.getcwd()
        try:
            os.chdir(path)#If that pass can this entered Path,it can be return
            os.chdir(currentPath)
            return True
            
        except FileNotFoundError:
        
            call("python /home/wasptheslimy/Desktop/youtube_Downloader/alertCodes.py '   ERROR   ' '[File Not Found Error] Enter a operable PATH.' 0",shell = True)

        except NotADirectoryError:
            
            call("python /home/wasptheslimy/Desktop/youtube_Downloader/alertCodes.py '   ERROR   ' '[Not a Directory Error] Enter a directory PATH not file.' 0",shell = True)

        except PermissionError:
            call("python /home/wasptheslimy/Desktop/youtube_Downloader/alertCodes.py '   ERROR   ' '[Permission Error] For this PATH you must change your authority.' 0",shell = True)
        
        return False



    def update(self):
        self.DownloadPath = self.Path.text()
        if self.pathControl(self.DownloadPath):

            with open("path.txt","a") as pathFile:
                pathFile.write(self.DownloadPath)
                pathFile.write("\n")
        
        self.close()
