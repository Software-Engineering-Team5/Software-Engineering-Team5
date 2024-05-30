import sys
sys.path.append('.')

import json
from src.module.user_model import DB_PATH, User, UserManager
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
from src.ui.signup_ui import Ui_SignUpWindow

class SignUpWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SignUpWindow()
        self.ui.setupUi(self)
        self.ui.signupButton.clicked.connect(self.signupFunction)

    def signupFunction(self):
        id = self.ui.id.text()
        pw = self.ui.password.text()
        user_manager = UserManager()
        
        if not id or not pw:
            QMessageBox.warning(self, '아이디와 비밀번호를 입력하세요. ', '아이디와 비밀번호를 입력하세요. ')
            return
        if user_manager.does_exists(id):
            QMessageBox.warning(self, '이미 존재하는 아이디입니다', '이미 존재하는 아이디입니다')
            return
        user_manager.create(id, pw)
        user_manager.save_users()
        
        QMessageBox.information(self, '회원가입 성공', '회원가입 성공')
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = SignUpWindow()
    widget.show()
    sys.exit(app.exec())
