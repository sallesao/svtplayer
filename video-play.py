"""Small test for playing video with Qt."""

import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


def main():
    app = QApplication(sys.argv)

    # Create media player, read media URL from first command line argument
    player = QMediaPlayer()
    media = QMediaContent(QUrl(sys.argv[1]))
    player.setMedia(media)

    # Create and set video output widget
    video = QVideoWidget()
    player.setVideoOutput(video)

    video.show()
    player.play()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
