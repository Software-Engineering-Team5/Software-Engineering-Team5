# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        if not HomeWindow.objectName():
            HomeWindow.setObjectName(u"HomeWindow")
        HomeWindow.resize(1000, 600)
        HomeWindow.setStyleSheet(u"background-color: white;")
        self.centralwidget = QWidget(HomeWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(140, 160, 4, 4))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 30, 374, 140))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.horizontalLayoutWidget)
        self.title.setObjectName(u"title")

        self.horizontalLayout.addWidget(self.title)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 230, 341, 271))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gameButton = QPushButton(self.gridLayoutWidget)
        self.gameButton.setObjectName(u"gameButton")
        self.gameButton.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.gameButton.setFont(font)

        self.gridLayout.addWidget(self.gameButton, 1, 0, 1, 1)

        self.testButton = QPushButton(self.gridLayoutWidget)
        self.testButton.setObjectName(u"testButton")
        self.testButton.setMinimumSize(QSize(336, 70))
        self.testButton.setMaximumSize(QSize(230, 70))
        self.testButton.setFont(font)

        self.gridLayout.addWidget(self.testButton, 0, 0, 1, 1)

        self.vocaButton = QPushButton(self.gridLayoutWidget)
        self.vocaButton.setObjectName(u"vocaButton")
        self.vocaButton.setMinimumSize(QSize(0, 70))
        self.vocaButton.setFont(font)

        self.gridLayout.addWidget(self.vocaButton, 2, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(784, 396, 111, 41))
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(760, 430, 161, 101))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.timeAttackLabel = QLabel(self.gridLayoutWidget_2)
        self.timeAttackLabel.setObjectName(u"timeAttackLabel")

        self.gridLayout_2.addWidget(self.timeAttackLabel, 0, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.perfectStreakkLabel = QLabel(self.gridLayoutWidget_2)
        self.perfectStreakkLabel.setObjectName(u"perfectStreakkLabel")

        self.gridLayout_2.addWidget(self.perfectStreakkLabel, 1, 1, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(760, 230, 161, 161))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lowLevelScoreLabel = QLabel(self.gridLayoutWidget_3)
        self.lowLevelScoreLabel.setObjectName(u"lowLevelScoreLabel")

        self.gridLayout_4.addWidget(self.lowLevelScoreLabel, 2, 1, 1, 1)

        self.middleLevelScoreLabel = QLabel(self.gridLayoutWidget_3)
        self.middleLevelScoreLabel.setObjectName(u"middleLevelScoreLabel")

        self.gridLayout_4.addWidget(self.middleLevelScoreLabel, 1, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 1, 0, 1, 1)

        self.highLevelScoreLabel = QLabel(self.gridLayoutWidget_3)
        self.highLevelScoreLabel.setObjectName(u"highLevelScoreLabel")

        self.gridLayout_4.addWidget(self.highLevelScoreLabel, 0, 1, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 2, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(780, 200, 121, 31))
        self.label_15.setFont(font1)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(31, 149, 232, 61))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.attendanceInfo = QLabel(self.verticalLayoutWidget)
        self.attendanceInfo.setObjectName(u"attendanceInfo")
        self.attendanceInfo.setMinimumSize(QSize(230, 0))
        self.attendanceInfo.setMaximumSize(QSize(230, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        self.attendanceInfo.setFont(font2)

        self.verticalLayout.addWidget(self.attendanceInfo, 0, Qt.AlignHCenter)

        self.settingsButton = QPushButton(self.centralwidget)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setGeometry(QRect(20, 510, 71, 51))
        self.settingsButton.setFont(font1)
        self.settingsButton.setAutoFillBackground(False)
        self.settingsButton.setStyleSheet(u"background-image:url(\"gear.png\");\n"
"background-color: transparent;\n"
"font-size: 20px;\n"
"background-repeat: none;\n"
"font-weight: bold;")
        icon = QIcon(QIcon.fromTheme(u"emblem-system"))
        self.settingsButton.setIcon(icon)
        self.attendanceInfo_2 = QLabel(self.centralwidget)
        self.attendanceInfo_2.setObjectName(u"attendanceInfo_2")
        self.attendanceInfo_2.setGeometry(QRect(650, 47, 300, 30))
        self.attendanceInfo_2.setMinimumSize(QSize(300, 30))
        self.attendanceInfo_2.setMaximumSize(QSize(300, 30))
        font3 = QFont()
        font3.setPointSize(18)
        self.attendanceInfo_2.setFont(font3)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(710, 80, 250, 3))
        self.line.setMinimumSize(QSize(250, 0))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.wordLabel = QLabel(self.centralwidget)
        self.wordLabel.setObjectName(u"wordLabel")
        self.wordLabel.setGeometry(QRect(650, 90, 300, 50))
        self.wordLabel.setMinimumSize(QSize(300, 50))
        self.wordLabel.setMaximumSize(QSize(300, 50))
        font4 = QFont()
        font4.setPointSize(25)
        self.wordLabel.setFont(font4)
        self.wordLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.meaningLabel = QLabel(self.centralwidget)
        self.meaningLabel.setObjectName(u"meaningLabel")
        self.meaningLabel.setGeometry(QRect(650, 130, 300, 30))
        self.meaningLabel.setMinimumSize(QSize(300, 30))
        self.meaningLabel.setMaximumSize(QSize(300, 30))
        self.meaningLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(710, 170, 250, 3))
        self.line_2.setMinimumSize(QSize(250, 0))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        HomeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(HomeWindow)
        self.statusbar.setObjectName(u"statusbar")
        HomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HomeWindow)

        QMetaObject.connectSlotsByName(HomeWindow)
    # setupUi

    def retranslateUi(self, HomeWindow):
        HomeWindow.setWindowTitle(QCoreApplication.translate("HomeWindow", u"LoginWindow", None))
        self.title.setText(QCoreApplication.translate("HomeWindow", u"<html><head/><body><p><span style=\" font-size:72pt; font-weight:700; color:#000000;\">SE </span><span style=\" font-size:48pt; font-weight:700; color:#000000;\">voca</span></p></body></html>", None))
        self.gameButton.setText(QCoreApplication.translate("HomeWindow", u"\uac8c\uc784", None))
        self.testButton.setText(QCoreApplication.translate("HomeWindow", u"\ud14c\uc2a4\ud2b8", None))
        self.vocaButton.setText(QCoreApplication.translate("HomeWindow", u"\ub2e8\uc5b4\uc7a5", None))
        self.label_2.setText(QCoreApplication.translate("HomeWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">\ub098\uc758 \uac8c\uc784 \uae30\ub85d</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("HomeWindow", u"\ub3c4\uc7a5 \uae68\uae30:", None))
        self.timeAttackLabel.setText("")
        self.label_3.setText(QCoreApplication.translate("HomeWindow", u"\ud0c0\uc784 \uc5b4\ud0dd:", None))
        self.perfectStreakkLabel.setText("")
        self.lowLevelScoreLabel.setText("")
        self.middleLevelScoreLabel.setText("")
        self.label_12.setText(QCoreApplication.translate("HomeWindow", u"\uc911\uae09:", None))
        self.highLevelScoreLabel.setText("")
        self.label_16.setText(QCoreApplication.translate("HomeWindow", u"\ud558\uae09:", None))
        self.label_5.setText(QCoreApplication.translate("HomeWindow", u"\uc0c1\uae09:", None))
        self.label_15.setText(QCoreApplication.translate("HomeWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">\ub098\uc758 \ud14c\uc2a4\ud2b8 \uae30\ub85d</span></p></body></html>", None))
        self.attendanceInfo.setText(QCoreApplication.translate("HomeWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-style:italic; color:#626262;\">\ud604\uc7ac </span><span style=\" font-size:18pt; font-weight:700; font-style:italic; color:#397eff;\">n</span><span style=\" font-size:18pt; font-style:italic; color:#626262;\">\uc77c \uc9f8 \ucd9c\uc11d \uc911!</span></p></body></html>", None))
        self.settingsButton.setText(QCoreApplication.translate("HomeWindow", u"\uc124\uc815", None))
        self.attendanceInfo_2.setText(QCoreApplication.translate("HomeWindow", u"<html><head/><body><p align=\"right\">\uae5c\uc9dd \ub2e8\uc5b4!</p></body></html>", None))
        self.wordLabel.setText(QCoreApplication.translate("HomeWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:24pt; font-weight:700;\">breathtaking</span></p></body></html>", None))
        self.meaningLabel.setText(QCoreApplication.translate("HomeWindow", u"<html><head/><body><p align=\"right\">\uc228\uc774 \ub9c9\ud788\ub294[\uba4e\ub294 \ub4ef\ud55c]</p></body></html>", None))
    # retranslateUi

