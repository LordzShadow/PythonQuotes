#!/usr/bin/env python3
from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide2.QtGui import QFont, QGuiApplication
from PySide2.QtCore import Qt, QPoint
import sys
# from random import randint
# import requests
# from bs4 import BeautifulSoup
import praw

class NewWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setParent(None)

        self.label = QLabel(text="1111")
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(15)
        self.label.setFont(self.font)
        self.label.setStyleSheet("color: #EBE75C")
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFixedWidth(1000)

        self.h = 0
        self.w = 0

        self.chars = 250

        self.quotes = []
        # self.page = randint(1, 10)
        # print(self.page)
        # self.url = "http://quotes.toscrape.com/page/{}/".format(self.page)
        # self.response = requests.get(self.url)
        # self.soup = BeautifulSoup(self.response.text, "html.parser")

        self.subreddit = self.connectReddit()
        self.quotes = [quote.title for quote in self.subreddit.hot(limit=25)]
        self.i = 1

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.flags = QtWidgets
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnBottomHint | Qt.WindowCloseButtonHint | Qt.Tool)
        self.setLayout(self.layout)

        self.m_nMouseClick_X_Coordinate = None
        self.m_nMouseClick_Y_Coordinate = None
        self.oldPos = self.pos()

        self.uus = self.quotes[0]
        self.label.setText(self.uus)
        self.startTimer(1000 * 60 * 60)
        #self.startTimer(5000)

    # def choose(self):
    #     for quote in self.soup.find_all("span", {"class": "text"}):
    #         if quote.text in self.quotes:
    #             pass
    #         else:
    #             if len(quote.text) > self.chars:
    #                 self.quotes.append(quote.text)
    #                 return self.choose()
    #             self.quotes.append(quote.text)
    #             author = quote.parent.findChild("small", {"class": "author"})
    #             self.author = author.text
    #             return quote.text
    #
    #     print(10000)
    #     if self.page == 10:
    #         self.page = 1
    #     else:
    #         self.page += 1
    #     self.url = "http://quotes.toscrape.com/page/{}/".format(str(self.page))
    #     self.response = requests.get(self.url)
    #     self.soup = BeautifulSoup(self.response.text, "html.parser")
    #     return self.choose()

    def timerEvent(self, event):
        #self.uus = self.choose()
        #self.label.setText(self.uus + "\n - " + self.author)
        quote = self.quotes[self.i]
        self.label.setText(quote)
        self.i += 1
        if self.i == 25:
            self.i = 0
        self.label.ensurePolished()
        self.setFixedSize(self.sizeHint())
        self.change_size()
        return

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)

        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def connectReddit(self):
        with open("secrets.data", "r") as file:
            lines = file.readlines()
            self.reddit = praw.Reddit(client_id=lines[0].strip(),
                                      client_secret=lines[1].strip(),
                                      password=lines[2].strip(),
                                      user_agent=lines[3].strip(),
                                      username=lines[4].strip())
            return self.reddit.subreddit("quotes")

    def change_size(self):
        self.move(QPoint(self.w / 2 - self.width()/2, self.h - self.height()-10))
        print(self.label.height())
        print(self.y())


w = 0
h = 0
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    screen_size = QGuiApplication.primaryScreen().availableGeometry()
    widget = NewWidget()
    widget.w, widget.h = screen_size.width(), screen_size.height()
    print(widget.h)
    widget.resize(200, 100)
    widget.show()
    widget.move(widget.w/2-widget.minimumWidth()/2, widget.h-widget.height())
    widget.setWindowTitle("Motivational quotes")

    sys.exit(app.exec_())
