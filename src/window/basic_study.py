import json
import random
import sys
sys.path.append('.')

from PyQt6.QtWidgets import *
from src.ui.basic_study_ui import Ui_BasicStudy
import random


class BasicStudy(QMainWindow):
    def __init__(self, filepath, parent=None):
        super().__init__(parent)
        self.ui = Ui_BasicStudy()
        self.ui.setupUi(self)
        self.path = filepath
        self.words = []
        self.i = 0
        
        self.load_word_file()
        random.shuffle(self.words)
        self.current_word = None
        
        if self.words:
            self.i += 1
            self.current_word = self.words[self.i]
            self.ui.label_eng.setText(self.current_word['word'])
            self.ui.label_kor.setText(self.current_word['meaning'])
        else:
            QMessageBox.critical(self, "에러", "단어장 파일을 로드해주세요.")

        self.ui.pushButton_before.clicked.connect(self.button_before)
        self.ui.pushButton_after.clicked.connect(self.button_after)
        self.ui.pushButton_main.clicked.connect(self.button_main)
        
    def load_word_file(self):
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
            self.words = [{"word": word, "meaning": meaning} for word, meaning in data.items()]
        
    def button_before(self):
        if self.i > 0:
            self.i -= 1
            self.current_word = self.words[self.i]
            self.ui.label_eng.setText(self.current_word['word'])
            self.ui.label_kor.setText(self.current_word['meaning'])
    
    def button_after(self):
        if self.words:
            self.i += 1
            self.current_word = self.words[self.i]
            self.ui.label_eng.setText(self.current_word['word'])
            self.ui.label_kor.setText(self.current_word['meaning'])
        else:
            QMessageBox.critical(self, "에러", "단어장 파일을 로드해주세요.")
            
    def button_main(self):
        self.close()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = BasicStudy("path_to_your_json_file.json")  # JSON 파일의 경로를 지정
    myWindow.show()
    sys.exit(app.exec())