import sys
sys.path.append('.')

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import pyqtSignal
from src.ui.test_select_ui import Ui_TestSelect
from src.window.mean_test import MeanTest
from src.window.eng_test import EngTest

class TestSelect(QMainWindow):
    testSignal = pyqtSignal(str)
    
    def __init__(self, user=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_TestSelect()
        self.ui.setupUi(self)
        self.user = user
        self.ui.meanButton.clicked.connect(self.mean_test)
        self.ui.engButton.clicked.connect(self.eng_test)

    def mean_test(self):
        self.mean_test_window = MeanTest(self.user)
        self.mean_test_window.meanTestResult.connect(self.update_signal)
        self.mean_test_window.show()
        self.close()
    
    def eng_test(self):
        self.eng_test_window = EngTest(self.user)
        self.eng_test_window.engTestResult.connect(self.update_signal)
        self.eng_test_window.show()
        self.close()
        
    def update_signal(self, result):
        self.testSignal.emit(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TestSelect()
    widget.show()
    sys.exit(app.exec())




