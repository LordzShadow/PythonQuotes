#!/usr/bin/env python3
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide2.QtGui import QPalette, QColor, QFont
from PySide2.QtCore import Qt, QPoint, QTimer
import sys
from random import choice


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


        self.quotes = ["Believe in yourself!",
                       "Have faith in your abilities!",
                       "If you can dream it, you can do it.",
                       "Press forward, do not stop, do not linger in your journey, but strive for the mark you set before you.",
                       "Aim for the moon. If you miss, you may hit a star.",
                       "Don't watch the clock; do what it does. Keep going.",
                       "We aim above the mark to hit the mark.",
                       "Change your life today, don't gamble on the future.",
                       "You just can't beat the person who never gives up.",
                       "Never give up.",
                       "Opportunities don't happen, you create them.",
                       "If you're going through hell, keep going.",
                       "No masterpiece was ever created by a lazy artist.",
                       "Do one thing every day that scares you.",
                       "The starting point of all achievements is desire.",
                       "It's better to fail in originality than succeed in imitation.",
                       "Failure is the condiment that gives success it's flavor."]

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.flags = QtWidgets
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnBottomHint|Qt.WindowCloseButtonHint)
        self.setLayout(self.layout)

        self.m_nMouseClick_X_Coordinate = None
        self.m_nMouseClick_Y_Coordinate = None
        self.oldPos = self.pos()

        self.valik = choice(self.quotes)
        self.label.setText(self.valik)
        self.startTimer(180000)

    def timerEvent(self, event):
        self.uus = choice(self.quotes)
        if self.uus == self.valik:
            self.timerEvent(event)
        else:
            self.valik = self.uus
            self.label.setText(self.valik)
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
    widget.setWindowTitle("Motivational quotes")

    sys.exit(app.exec_())

