import sys
sys.path.append('.')

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import pyqtSignal
from src.ui.level_select_ui import Ui_LevelSelect
from src.window.test_select import TestSelect

class LevelSelect(QMainWindow):
    resultSignal = pyqtSignal(str)
    
    def __init__(self, user=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_LevelSelect()
        self.ui.setupUi(self)
        self.user = user
        self.ui.easyButton.clicked.connect(self.easy)
        self.ui.normalButton.clicked.connect(self.normal)
        self.ui.hardButton.clicked.connect(self.hard)

    def easy(self):
        self.test_select_window = TestSelect('easy', self.user)
        self.test_select_window.testSignal.connect(self.update_signal)
        self.test_select_window.show()
        self.close()
    
    def normal(self):
        self.test_select_window = TestSelect('normal', self.user)
        self.test_select_window.testSignal.connect(self.update_signal)
        self.test_select_window.show()
        self.close()
        
    def hard(self):
        self.test_select_window = TestSelect('hard', self.user)
        self.test_select_window.testSignal.connect(self.update_signal)
        self.test_select_window.show()
        self.close()
        
    def update_signal(self, result):
        self.resultSignal.emit(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = LevelSelect()
    widget.show()
    sys.exit(app.exec())




