import sys
sys.path.append('.')

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from src.ui.TestSelectWindow import Ui_TestSelectWindow
from src.window.MeanTest import MeanTest
from src.window.EngTest import EngTest

class TestSelectWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TestSelectWindow()
        self.ui.setupUi(self)
        self.ui.meanButton.clicked.connect(self.mean_test)
        self.ui.engButton.clicked.connect(self.eng_test)

    def mean_test(self):
        self.mean_test_window = MeanTest()
        self.mean_test_window.show()
    
    def eng_test(self):
        self.eng_test_window = EngTest()
        self.eng_test_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = TestSelectWindow()
    widget.show()
    sys.exit(app.exec())




