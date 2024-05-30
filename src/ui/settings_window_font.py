# Form implementation generated from reading ui file 'settings_window_font.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SettingFont(object):
    def setupUi(self, SettingFont):
        SettingFont.setObjectName("SettingFont")
        SettingFont.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=SettingFont)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 90, 181, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(230, 10, 20, 551))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.fontSizedefault = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.fontSizedefault.setGeometry(QtCore.QRect(360, 190, 91, 100))
        self.fontSizedefault.setMinimumSize(QtCore.QSize(50, 100))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fontSizedefault.setFont(font)
        self.fontSizedefault.setStyleSheet("")
        self.fontSizedefault.setObjectName("fontSizedefault")
        self.fontSizeIncrease = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.fontSizeIncrease.setGeometry(QtCore.QRect(570, 190, 131, 100))
        self.fontSizeIncrease.setMinimumSize(QtCore.QSize(50, 100))
        font = QtGui.QFont()
        font.setPointSize(55)
        self.fontSizeIncrease.setFont(font)
        self.fontSizeIncrease.setStyleSheet("")
        self.fontSizeIncrease.setObjectName("fontSizeIncrease")
        self.fontSizeSaveButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.fontSizeSaveButton.setGeometry(QtCore.QRect(400, 480, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.fontSizeSaveButton.setFont(font)
        self.fontSizeSaveButton.setObjectName("fontSizeSaveButton")
        self.exitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(760, 10, 21, 32))
        self.exitButton.setObjectName("exitButton")
        self.menuButtonTheme = QtWidgets.QCommandLinkButton(parent=self.centralwidget)
        self.menuButtonTheme.setGeometry(QtCore.QRect(30, 190, 168, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.menuButtonTheme.setFont(font)
        self.menuButtonTheme.setObjectName("menuButtonTheme")
        self.menuButtonFont = QtWidgets.QCommandLinkButton(parent=self.centralwidget)
        self.menuButtonFont.setGeometry(QtCore.QRect(30, 240, 168, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.menuButtonFont.setFont(font)
        self.menuButtonFont.setObjectName("menuButtonFont")
        SettingFont.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=SettingFont)
        self.statusbar.setObjectName("statusbar")
        SettingFont.setStatusBar(self.statusbar)

        self.retranslateUi(SettingFont)
        QtCore.QMetaObject.connectSlotsByName(SettingFont)

    def retranslateUi(self, SettingFont):
        _translate = QtCore.QCoreApplication.translate
        SettingFont.setWindowTitle(_translate("SettingFont", "MainWindow"))
        self.label.setText(_translate("SettingFont", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:700;\">설정</span></p></body></html>"))
        self.fontSizedefault.setText(_translate("SettingFont", "기본"))
        self.fontSizeIncrease.setText(_translate("SettingFont", "크게"))
        self.fontSizeSaveButton.setText(_translate("SettingFont", "저장"))
        self.exitButton.setText(_translate("SettingFont", "X"))
        self.menuButtonTheme.setText(_translate("SettingFont", "테마 변경"))
        self.menuButtonFont.setText(_translate("SettingFont", "글씨 크기 변경"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingFont = QtWidgets.QMainWindow()
    ui = Ui_SettingFont()
    ui.setupUi(SettingFont)
    SettingFont.show()
    sys.exit(app.exec())
