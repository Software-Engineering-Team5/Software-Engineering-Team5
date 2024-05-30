import sys
sys.path.append('.')

from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from src.ui.home import Ui_HomeWindow
from src.window.test_select_window import TestSelectWindow
from src.window.game_select_window import GameSelectWindow
from src.module.user_model import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self)
        self.ui.testButton.clicked.connect(self.test_window)
        self.ui.gameButton.clicked.connect(self.game_window)
        # self.ui.vocaButton.clicked.connect(self.voca_window)

    def test_window(self):
        self.test_window = TestSelectWindow()
        self.test_window.show()

    def game_window(self):
        self.game_window = GameSelectWindow()
        self.game_window.show()

    # def voca_window(self):
    #     self.game_window = SignUpWindow()
    #     self.game_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())