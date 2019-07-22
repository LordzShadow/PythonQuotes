#!/usr/bin/env python3
from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QPoint
import sys
from random import randint
import requests
from bs4 import BeautifulSoup


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

        self.chars = 250

        self.quotes = []
        self.page = randint(1, 10)
        print(self.page)
        self.url = "http://quotes.toscrape.com/page/{}/".format(self.page)
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, "html.parser")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.flags = QtWidgets
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnBottomHint | Qt.WindowCloseButtonHint)
        self.setLayout(self.layout)

        self.m_nMouseClick_X_Coordinate = None
        self.m_nMouseClick_Y_Coordinate = None
        self.oldPos = self.pos()

        self.author = ""
        self.uus = self.choose()
        self.label.setText(self.uus + "\n - " + self.author)
        #self.startTimer(1000 * 60 * 60)
        self.startTimer(5000)

    def choose(self):
        for quote in self.soup.find_all("span", {"class": "text"}):
            if quote.text in self.quotes:
                pass
            else:
                if len(quote.text) > self.chars:
                    self.quotes.append(quote.text)
                    return self.choose()
                self.quotes.append(quote.text)
                author = quote.parent.findChild("small", {"class": "author"})
                self.author = author.text
                return quote.text

        print(10000)
        if self.page == 10:
            self.page = 1
        else:
            self.page += 1
        self.url = "http://quotes.toscrape.com/page/{}/".format(str(self.page))
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        return self.choose()

    def timerEvent(self, event):
        self.uus = self.choose()
        self.label.setText(self.uus + "\n - " + self.author)
        return

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)

        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = NewWidget()
    widget.resize(200, 100)
    widget.show()
    widget.move(0, widget.maximumHeight())
    widget.setWindowTitle("Motivational quotes")

    sys.exit(app.exec_())

