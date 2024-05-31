import json
import random
import sys
sys.path.append('.')

from PyQt6.QtWidgets import *
from src.ui.basic_study_ui import Ui_BasicStudy
import random

#화면을 띄우는데 사용되는 Class 선언
class BasicStudy(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_BasicStudy()
        self.ui.setupUi(self)

        # 단어 리스트 초기화
        self.words = []
        self.i=0
        
        # JSON 파일에서 단어를 불러옵니다.
        self.load_word_file()
        random.shuffle(self.words)
        self.current_word = None
        
        if self.words:
            self.i=self.i+1
            self.current_word = self.words[self.i]
            self.ui.label_eng.setText(f"{self.current_word['word']}")
            self.ui.label_kor.setText(f"{self.current_word['meaning']}")

        else:
            QMessageBox.critical(self, "에러", "단어장 파일을 로드해주세요.")

        self.ui.pushButton_before.clicked.connect(self.button_before)
        self.ui.pushButton_after.clicked.connect(self.button_after)
        self.ui.pushButton_main.clicked.connect(self.button_main)
        
    def load_word_file(self):
        # 파일 선택 대화 상자를 열어서 JSON 파일을 선택합니다.
        filename, _ = QFileDialog.getOpenFileName(self, "단어장 파일 선택", "", "JSON Files (*.json)")

        if filename:
            # 선택한 파일을 열어서 단어를 로드합니다.
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.words = [{"word": word, "meaning": meaning} for word, meaning in data.items()]

    def button_before(self) :
        if self.i!=0:
            self.i=self.i-1
            self.current_word = self.words[self.i]
            self.ui.label_eng.setText(f"{self.current_word['word']}")
            self.ui.label_kor.setText(f"{self.current_word['meaning']}")
    def button_after(self) :
        if self.words:
            self.i=self.i+1
            self.current_word = self.words[self.i]
            self.ui.label_eng.setText(f"{self.current_word['word']}")
            self.ui.label_kor.setText(f"{self.current_word['meaning']}")

        else:
            QMessageBox.critical(self, "에러", "단어장 파일을 로드해주세요.")
            
    def button_main(self):
        self.close()
    
if __name__ == "__main__" :

    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = BasicStudy() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec()

