# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window_theme.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFrame, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_ThemeSettingsWindow(object):
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
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(300, 90, 451, 100))
        self.radioButton.setMinimumSize(QSize(50, 100))
        font = QFont()
        font.setPointSize(40)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet(u"border : 1px solid white;")
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(300, 210, 451, 100))
        self.radioButton_2.setMinimumSize(QSize(50, 100))
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet(u"border : 1px solid black;")
        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(300, 330, 451, 100))
        self.radioButton_3.setMinimumSize(QSize(50, 100))
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet(u"border : 1px solid green;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(400, 480, 251, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.pushButton.setFont(font1)
        self.exitButton = QPushButton(self.centralwidget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(760, 10, 21, 32))
        self.menuButtonTheme = QCommandLinkButton(self.centralwidget)
        self.menuButtonTheme.setObjectName(u"menuButtonTheme")
        self.menuButtonTheme.setGeometry(QRect(30, 190, 168, 41))
        self.menuButtonTheme.setFont(font1)
        self.menuButtonFont = QCommandLinkButton(self.centralwidget)
        self.menuButtonFont.setObjectName(u"menuButtonFont")
        self.menuButtonFont.setGeometry(QRect(30, 240, 168, 41))
        self.menuButtonFont.setFont(font1)
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
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"light", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"dark", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"plant", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.exitButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.menuButtonTheme.setText(QCoreApplication.translate("MainWindow", u"\ud14c\ub9c8 \ubcc0\uacbd", None))
        self.menuButtonFont.setText(QCoreApplication.translate("MainWindow", u"\uae00\uc528 \ud06c\uae30 \ubcc0\uacbd", None))
    # retranslateUi

