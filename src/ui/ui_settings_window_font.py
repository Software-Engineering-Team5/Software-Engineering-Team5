# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window_font.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFrame, QLabel,
    QMainWindow, QPushButton, QRadioButton, QStatusBar, QVBoxLayout, QWidget)

class Ui_FontSettingsWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 90, 181, 71))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(230, 10, 20, 551))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.fontSizedefault = QRadioButton(self.centralwidget)
        self.fontSizedefault.setObjectName(u"fontSizedefault")
        self.fontSizedefault.setGeometry(QRect(360, 190, 91, 100))
        self.fontSizedefault.setMinimumSize(QSize(50, 100))
        font = QFont()
        font.setPointSize(26)
        self.fontSizedefault.setFont(font)
        self.fontSizedefault.setStyleSheet(u"")
        self.fontSizeIncrease = QRadioButton(self.centralwidget)
        self.fontSizeIncrease.setObjectName(u"fontSizeIncrease")
        self.fontSizeIncrease.setGeometry(QRect(570, 190, 131, 100))
        self.fontSizeIncrease.setMinimumSize(QSize(50, 100))
        font1 = QFont()
        font1.setPointSize(55)
        self.fontSizeIncrease.setFont(font1)
        self.fontSizeIncrease.setStyleSheet(u"")
        self.fontSizeSaveButton = QPushButton(self.centralwidget)
        self.fontSizeSaveButton.setObjectName(u"fontSizeSaveButton")
        self.fontSizeSaveButton.setGeometry(QRect(400, 480, 251, 51))
        font2 = QFont()
        font2.setPointSize(20)
        self.fontSizeSaveButton.setFont(font2)
        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(760, 10, 21, 32))
        self.menuButtonTheme = QCommandLinkButton(self.centralwidget)
        self.menuButtonTheme.setObjectName(u"menuButtonTheme")
        self.menuButtonTheme.setGeometry(QRect(30, 190, 168, 41))
        self.menuButtonTheme.setFont(font2)
        self.menuButtonFont = QCommandLinkButton(self.centralwidget)
        self.menuButtonFont.setObjectName(u"menuButtonFont")
        self.menuButtonFont.setGeometry(QRect(30, 240, 168, 41))
        self.menuButtonFont.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:48pt; font-weight:700;\">\uc124\uc815</span></p></body></html>", None))
        self.fontSizedefault.setText(QCoreApplication.translate("MainWindow", u"\uae30\ubcf8", None))
        self.fontSizeIncrease.setText(QCoreApplication.translate("MainWindow", u"\ud06c\uac8c", None))
        self.fontSizeSaveButton.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.menuButtonTheme.setText(QCoreApplication.translate("MainWindow", u"\ud14c\ub9c8 \ubcc0\uacbd", None))
        self.menuButtonFont.setText(QCoreApplication.translate("MainWindow", u"\uae00\uc528 \ud06c\uae30 \ubcc0\uacbd", None))
    # retranslateUi
