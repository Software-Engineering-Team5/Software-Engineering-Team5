import json
import sys
sys.path.append('.')
from PyQt6.QtWidgets import *

from src.ui.data_manage_ui import Ui_DataManage
from src.module.data_processing import *

def save_words(words, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(words, file, ensure_ascii=False, indent=4)

def add_word(words, word, meaning):
    words[word] = meaning

def remove_word(words, word):
    if word in words:
        del words[word]
        
class DataManage(QMainWindow) :
    def __init__(self, filename) :
        super().__init__()
        self.ui = Ui_DataManage()
        self.ui.setupUi(self)
        self.filename = filename
        self.ui.pushButton.clicked.connect(self.button_add)
        self.ui.pushButton_2.clicked.connect(self.button_remove)
        
    def button_add(self) :
        words = json_to_dict('hackers_test')
        word = self.ui.lineEdit.text()
        meaning = self.ui.lineEdit_2.text()
        add_word(words, word, meaning)
        save_words(words, self.filename)
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        
    def button_remove(self) :
        words = json_to_dict('hackers_test')
        word = self.ui.lineEdit.text()
        remove_word(words, word)
        save_words(words, self.filename)
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()

if __name__ == "__main__" :

    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = DataManage() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec()

