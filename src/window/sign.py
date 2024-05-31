import sys
sys.path.append('.')

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from src.ui.login_ui import Ui_Login
from src.ui.signup_ui import Ui_SignUp
from src.window.main import Main
from src.window.data_managing import DataManage
from src.module.user_model import *

class Login(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.loginFunction)
        self.ui.signUpButton.clicked.connect(self.signUpFunction)
        
    def loginFunction(self):
        id = self.ui.id.text()
        pw = self.ui.password.text()
        user_manager = UserManager()
        
        if not user_manager.does_exists(id):
            QMessageBox.warning(self, '로그인 실패', 'id가 존재하지 않습니다. ')
            return
        
        if User.hash_password(pw) != user_manager.get(id)["password"]:
            QMessageBox.warning(self, '로그인 실패', '비밀번호가 틀렸습니다. ')
            return
        user_manager.update(id)
        user_manager.update_attendance(id)
        user_manager.save_users()
        QMessageBox.information(self, '로그인 성공', '로그인 성공')
        
        if user_manager.get(id)['is admin']:
            self.data_manage_window = DataManage()
            self.data_manage_window.show()
            self.close()
        else:
            self.main_window = Main(user_manager.get(id))
            self.main_window.show()
            self.close()
        
    def signUpFunction(self):
        self.sign_up_window = SignUp()
        self.sign_up_window.show()
        self.close()

class SignUp(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SignUp()
        self.ui.setupUi(self)
        self.ui.signupButton.clicked.connect(self.signupFunction)
        self.ui.loginButton.clicked.connect(self.loginFunction)

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
        
        self.loginFunction()
        
    def loginFunction(self):
        self.login_window = Login()
        self.login_window.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Login()
    widget.show()
    sys.exit(app.exec())
