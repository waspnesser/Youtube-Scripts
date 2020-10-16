#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import PIL
from PIL import Image
#ALERT CODE SCHEME
# AUTHOR -- WASP

class Alert(QWidget):
    def __init__(self,size,label,message,messageType):
        super().__init__()
        #self.backgroundRole(QPalette.Base)
        self.setWindowTitle("ProgressNotifier")
        self.setAutoFillBackground(True)
        palette = self.palette()
        #palette.setColor(self.backgroundRole(), Qt.blue)
        color = QColor(107,111,125)
        palette.setColor(self.backgroundRole(), color)
        self.setPalette(palette)
        self.label = label
        self.message = message
        self.size = size
        self.messageType = messageType
        self.setGeometry(size[0]/2-200,size[1]/2-100,300,100)#For symetry obssesiopn...But it is not symetric ,still...
        self.initUI()

    def initUI(self):
        self.MainVerticalLayout = QVBoxLayout()

        self.HeaderHorizontalLayout = QHBoxLayout()

        self.labelPlace =  QLabel()
        if self.messageType:
            self.labelPlace.setPixmap(QPixmap("/home/wasptheslimy/Desktop/youtube_Downloader/Icons/doneAdjusted.png"))
        else:
            self.labelPlace.setPixmap(QPixmap("/home/wasptheslimy/Desktop/youtube_Downloader/Icons/WarningAdjusted.png"))

        self.labelPlaceText = QLabel(self.label)
        cssCodeLabelText = """
        font-family: 'Times New Roman', Times, serif;
        font-size:18px;
        background-color: #324e4a;
        color : #fad764;
        padding-top : 4px;
        padding-bottom : 4px;
        padding-left:64px;
        padding-right:64px;
        border-style: solid;
        border-width: medium;
        """
        cssCodeMessage = """
        font-family: 'Times New Roman', Times, serif;
        font-size:12px;
        background-color: #2e654f;
        color :#e09bff;
        padding-top : 8px;
        padding-bottom : 8px;
        padding-left:12px;
        padding-right:12px;
        border-style: solid;
        border-width: 4px;
        border-color : #540d4d;

        """

        self.labelPlaceText.setStyleSheet(cssCodeLabelText)

        self.messagePlace = QLabel(self.message)
        self.messagePlace.setStyleSheet(cssCodeMessage)
        self.HeaderHorizontalLayout.addWidget(self.labelPlace)
        self.HeaderHorizontalLayout.addWidget(self.labelPlaceText)
        self.HeaderHorizontalLayout.addStretch()

        self.MainVerticalLayout.addLayout(self.HeaderHorizontalLayout)
        self.MainVerticalLayout.addStretch()
        self.MainVerticalLayout.addWidget(self.messagePlace)

        self.setLayout(self.MainVerticalLayout)
        





if __name__ == '__main__':

    import sys

    try: 
        label,message,messageType = sys.argv[1],sys.argv[2],int(sys.argv[3])
    except IndexError:
        print("[ERROR] Message and Label is not specified...")
        sys.exit()

    app = QApplication(sys.argv)

    screen = app.primaryScreen()
    size = screen.size()
    width = size.width()
    height = size.height()
    size = (width,height)

    obj = Alert(size,label,message,messageType)
    obj.show()
    sys.exit(app.exec_())
    