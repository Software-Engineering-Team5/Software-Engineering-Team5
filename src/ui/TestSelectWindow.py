# Form implementation generated from reading ui file 'TestSelectWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TestSelectWindow(object):
    def setupUi(self, TestSelectWindow):
        TestSelectWindow.setObjectName("TestSelectWindow")
        TestSelectWindow.resize(1000, 600)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=TestSelectWindow)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 240, 841, 261))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.meanButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.meanButton.setMinimumSize(QtCore.QSize(300, 70))
        self.meanButton.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.meanButton.setFont(font)
        self.meanButton.setObjectName("meanButton")
        self.horizontalLayout.addWidget(self.meanButton)
        self.engButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.engButton.setMinimumSize(QtCore.QSize(300, 70))
        self.engButton.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.engButton.setFont(font)
        self.engButton.setObjectName("engButton")
        self.horizontalLayout.addWidget(self.engButton)
        self.label = QtWidgets.QLabel(parent=TestSelectWindow)
        self.label.setGeometry(QtCore.QRect(304, 167, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(TestSelectWindow)
        QtCore.QMetaObject.connectSlotsByName(TestSelectWindow)

    def retranslateUi(self, TestSelectWindow):
        _translate = QtCore.QCoreApplication.translate
        TestSelectWindow.setWindowTitle(_translate("TestSelectWindow", "Dialog"))
        self.meanButton.setText(_translate("TestSelectWindow", "뜻 맞추기"))
        self.engButton.setText(_translate("TestSelectWindow", "단어 맞추기"))
        self.label.setText(_translate("TestSelectWindow", "테스트할 항목을 선택하세요."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TestSelectWindow = QtWidgets.QDialog()
    ui = Ui_TestSelectWindow()
    ui.setupUi(TestSelectWindow)
    TestSelectWindow.show()
    sys.exit(app.exec())
