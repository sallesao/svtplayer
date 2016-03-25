#!/usr/bin/python3

import sys

from PyQt5.QtCore import QUrl, pyqtSignal
from PyQt5.QtWidgets import QApplication, QPushButton, QStackedWidget

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


class ClickableVideoWidget(QVideoWidget):

    clicked = pyqtSignal()

    def __init__(self):
        super().__init__()

    def mouseReleaseEvent(self, _):
        self.clicked.emit()


app = QApplication(sys.argv)

# create stacked layout
w = QStackedWidget()

# add buttons
btn1 = QPushButton("PLAY")
player = QMediaPlayer()
media = QMediaContent(QUrl(sys.argv[1]))
player.setMedia(media)

# Create and set video output widget
video = ClickableVideoWidget()
player.setVideoOutput(video)

# add to stacked layout
print("Added widget", w.addWidget(btn1))
print("Added widget", w.addWidget(video))

def play_video():
    w.setCurrentIndex(1)
    player.play()

def pause_video():
    player.pause()
    w.setCurrentIndex(0)

# connect signals to stack change layout slot
btn1.clicked.connect(play_video)
video.clicked.connect(pause_video)

w.show()

sys.exit(app.exec_())
