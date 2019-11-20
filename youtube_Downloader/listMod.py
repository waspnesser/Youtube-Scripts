import sys
from itertools import cycle
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets

from MainMp3Motor import mp3Download


class ListDownload(QtWidgets.QWidget):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()

    def __init__(self, path):
        super().__init__()
        self.path = path
        self.setWindowTitle("List Download Mod")
        self.initUI()

    def initUI(self):
        VerticalLayout = QtWidgets.QVBoxLayout(self)

        SeasonOfWitch = QtWidgets.QLabel("Enter the URLs : ")

        self.URLs = QtWidgets.QTextEdit()
        self.URLs.setText("""enter the addresses in the here .a row for each url.
        Delete this message before entering the URLs.""")

        horizontalControlLayout = QtWidgets.QHBoxLayout()
        download = QtWidgets.QPushButton("Download")
        download.clicked.connect(self.videoDownload)

        Cancel = QtWidgets.QPushButton("Cancel")
        Cancel.clicked.connect(self.close)
        horizontalControlLayout.addWidget(download)
        horizontalControlLayout.addWidget(Cancel)

        VerticalLayout.addWidget(SeasonOfWitch)
        VerticalLayout.addWidget(self.URLs)
        VerticalLayout.addLayout(horizontalControlLayout)

        self.started.connect(self.messageAnimation)

    def videoDownload(self):
        lines = self.URLs.toPlainText().split("\n")
        urls = []
        for line in lines:
            if 'www.youtube.com' in line.split("/") and (line.startswith("https://") or line.startswith("http://")):
                urls.append(line)
        if urls:
            Thread(target=self.downloadFunc, args=(urls,), name="download", daemon=True).start()

    def downloadFunc(self, urls):
        self.started.emit()
        mp3Download(urls, self.path)
        self.finished.emit()
        

    def messageAnimation(self):
        self.URLs.clear()
        text = "Downloading ...."
        timer = QtCore.QTimer(self, interval=50)
        it = cycle(text+"\n")
        timer.timeout.connect(lambda: self.appendLetter(next(it)))
        timer.start()
        self.finished.connect(timer.stop)
        self.finished.connect(self.URLs.clear)

    def appendLetter(self, letter):
        if letter == "\n":
            self.URLs.clear()
        else:
            self.URLs.moveCursor(QtGui.QTextCursor.End)
            self.URLs.insertPlainText(letter)
            self.URLs.moveCursor(QtGui.QTextCursor.End)


