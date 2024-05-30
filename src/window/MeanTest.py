import sys
import json
import random
import os
from src.ui.MeanTest import Ui_MainWindow
from PyQt6 import uic
from PyQt6.QtWidgets import *

class MeanTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 단어 리스트 초기화
        self.words = []

        # JSON 파일에서 단어를 불러옵니다.
        self.load_word_file()

        self.current_word = None
        self.correct_count = 0
        self.total_attempts = 0
        self.max_attempts = 20
        self.results = []

        # UI 요소를 가져옵니다.
        self.question_text = self.findChild(QPlainTextEdit, 'plainTextEdit')
        self.answer_input = self.findChild(QLineEdit, 'lineEdit')
        self.submit_button = self.findChild(QPushButton, 'pushButton')

        # 버튼 클릭 시 check_answer 함수 호출
        self.submit_button.clicked.connect(self.check_answer)

        # Enter 키를 누르면 check_answer 함수 호출
        self.answer_input.returnPressed.connect(self.check_answer)

        # 첫 번째 문제를 표시
        self.next_word()

    def load_word_file(self):
        # 파일 선택 대화 상자를 열어서 JSON 파일을 선택합니다.
        filename, _ = QFileDialog.getOpenFileName(self, "단어장 파일 선택", "", "JSON Files (*.json)")

        if filename:
            # 선택한 파일을 열어서 단어를 로드합니다.
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.words = [{"word": word, "meaning": meaning} for word, meaning in data.items()]

    def next_word(self):
        if self.words:
            if self.total_attempts < self.max_attempts:
                self.current_word = random.choice(self.words)
                self.question_text.setPlainText(f"{self.current_word['word']}")
                self.answer_input.clear()
            else:
                self.show_result()
        else:
            QMessageBox.critical(self, "에러", "단어장 파일을 로드해주세요.")

    def check_answer(self):
        if self.words:
            answer = self.answer_input.text().strip()
            self.total_attempts += 1

            is_correct = answer == self.current_word['meaning']
            if is_correct:
                self.correct_count += 1

            self.results.append({
                "question": self.current_word['word'],
                "correct_answer": self.current_word['meaning'],
                "your_answer": answer,
                "result": "O" if is_correct else "X"
            })

            self.next_word()

    def show_result(self):
        if self.words:
            dialog = QDialog(self)
            dialog.setWindowTitle('결과')

            layout = QVBoxLayout(dialog)

            result_label = QLabel(f"시험 종료! 총 맞춘 개수: {self.correct_count}/{self.max_attempts}")
            layout.addWidget(result_label)

            # Create a table widget
            table = QTableWidget()
            table.setRowCount(len(self.results))
            table.setColumnCount(4)
            table.setHorizontalHeaderLabels(['문제', '정답', '당신의 답', '결과'])

            for row, item in enumerate(self.results):
                question_item = QTableWidgetItem(item['question'])
                correct_answer_item = QTableWidgetItem(item['correct_answer'])
                your_answer_item = QTableWidgetItem(item['your_answer'])
                result_item = QTableWidgetItem(item['result'])

                table.setItem(row, 0, question_item)
                table.setItem(row, 1, correct_answer_item)
                table.setItem(row, 2, your_answer_item)
                table.setItem(row, 3, result_item)

            table.resizeColumnsToContents()

            scroll = QScrollArea()
            scroll.setWidget(table)
            scroll.setWidgetResizable(True)
            scroll.setFixedHeight(300)
            scroll.setFixedWidth(500)

            layout.addWidget(scroll)

            close_button = QPushButton("닫기")
            close_button.clicked.connect(QApplication.instance().quit)
            layout.addWidget(close_button)

            dialog.setLayout(layout)
            dialog.exec()

            # Reset the game state
            self.correct_count = 0
            self.total_attempts = 0
            self.results.clear()
            self.next_word()
        else:
            QMessageBox.critical(self, "에러", "단어장 파일을 로드해주세요.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = MeanTest()
    game.show()
    sys.exit(app.exec())