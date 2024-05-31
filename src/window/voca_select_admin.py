import sys
sys.path.append('.')

from PyQt6.QtWidgets import QApplication, QMainWindow
from src.ui.voca_select_ui import Ui_VocaSelect
from src.window.data_managing import DataManage

class VocaSelectAdmin(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_VocaSelect()
        self.ui.setupUi(self)
        self.ui.hackersButton.clicked.connect(self.hackers)
        self.ui.wordMasterButton.clicked.connect(self.word_master)
        self.ui.amazingTalkerButton.clicked.connect(self.amzing_talker)

    def hackers(self):
        self.data_manage_window = DataManage('data/hackers_test/hackers_test_processed.json')
        self.data_manage_window.show()
    
    def word_master(self):
        self.data_manage_window = DataManage('data/word_master/word_master_processed.json')
        self.data_manage_window.show()
        
    def amzing_talker(self):
        self.data_manage_window = DataManage('data/amazing_talker/amazing_talker_processed.json')
        self.data_manage_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = VocaSelectAdmin()
    widget.show()
    sys.exit(app.exec())




