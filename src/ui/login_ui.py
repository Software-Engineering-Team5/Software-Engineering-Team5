# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(1000, 600)
        self.centralwidget = QtWidgets.QWidget(parent=LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 140, 1001, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(140, 160, 4, 4))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(320, 220, 61, 31))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_2 = QtWidgets.QFrame(parent=self.verticalLayoutWidget_8)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 61, 31))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.frame_2)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(620, 220, 61, 70))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.loginButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_9)
        self.loginButton.setMinimumSize(QtCore.QSize(51, 0))
        self.loginButton.setMaximumSize(QtCore.QSize(20, 100))
        self.loginButton.setIconSize(QtCore.QSize(10, 30))
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout_10.addWidget(self.loginButton)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(320, 260, 61, 31))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_3 = QtWidgets.QFrame(parent=self.verticalLayoutWidget_10)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 61, 31))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_11.addWidget(self.frame_3)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(320, 310, 351, 41))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(320, 350, 351, 41))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_4 = QtWidgets.QFrame(parent=self.verticalLayoutWidget_5)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.signUpButton = QtWidgets.QPushButton(parent=self.frame_4)
        self.signUpButton.setGeometry(QtCore.QRect(109, 0, 131, 41))
        self.signUpButton.setObjectName("signUpButton")
        self.verticalLayout_6.addWidget(self.frame_4)
        self.password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password.setGeometry(QtCore.QRect(380, 260, 241, 31))
        self.password.setMaxLength(100)
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setObjectName("password")
        self.id = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.id.setGeometry(QtCore.QRect(380, 220, 241, 31))
        self.id.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.id.setObjectName("id")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "LoginWindow"))
        self.label.setText(_translate("LoginWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">로그인</span></p></body></html>"))
        self.label_2.setText(_translate("LoginWindow", "<html><head/><body><p align=\"center\">ID</p></body></html>"))
        self.loginButton.setText(_translate("LoginWindow", "로그인"))
        self.label_3.setText(_translate("LoginWindow", "<html><head/><body><p align=\"center\">PW</p></body></html>"))
        self.label_4.setText(_translate("LoginWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#777777;\">계정이 없으신가요?</span></p></body></html>"))
        self.signUpButton.setText(_translate("LoginWindow", "회원가입"))
        self.password.setPlaceholderText(_translate("LoginWindow", "비밀번호를 입력하세요."))
        self.id.setPlaceholderText(_translate("LoginWindow", "아이디를 입력하세요."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec())
