import random
import sys
sys.path.append('.')

from src.module.data_processing import json_to_dict
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QFont, QFontDatabase
from src.ui.home import Ui_HomeWindow
from src.window.test_select_window import TestSelectWindow
from src.window.game_select_window import GameSelectWindow
from src.window.basic_study import BasicStudy
from src.window.settings_window_theme import SettingThemaWindow
from src.module.user_model import *

class MainWindow(QMainWindow):
    def __init__(self, user=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self)
        self.user = user
        self.ui.testButton.clicked.connect(self.show_test_window)
        self.ui.gameButton.clicked.connect(self.show_game_window)
        self.ui.vocaButton.clicked.connect(self.show_voca_window)
        self.ui.settingsButton.clicked.connect(self.show_setting_window)

        self.set_attendance()
        self.set_word()
        self.set_middle_level_score()
        self.set_time_attack_score()
        self.set_perfect_streak_score()
        
    def show_test_window(self):
        self.test_window = TestSelectWindow()
        self.test_window.show()

    def show_game_window(self):
        self.game_window = GameSelectWindow()
        self.game_window.show()

    def show_voca_window(self):
        self.voca_window = BasicStudy()
        self.voca_window.show()
        
        self.ui.middleLevelScoreLabel.setText(self.middle_level_score)
        self.ui.timeAttackLabel.setText(self.time_attack)
        self.ui.perfectStreakkLabel.setText(self.perfect_streak_score)
    
    def show_setting_window(self):
        self.thema_window = SettingThemaWindow()
        self.thema_window.show()
    
    def set_attendance(self):
        self.ui.attendanceInfo.setText('현재 {n}일 째 출석 중'.format(n=self.user['attendance']))
        
    def set_word(self):
        words = json_to_dict('hackers_test')
        items = list(words.items())
        word = random.choice(items)
        self.ui.wordLabel.setText(word[0])
        self.ui.meaningLabel.setText(word[1])

    def set_middle_level_score(self):
        self.ui.middleLevelScoreLabel.setText(str(self.user['test score']))
        
    def set_time_attack_score(self):
        self.ui.timeAttackLabel.setText(str(self.user['time attack score']))
        
    def set_perfect_streak_score(self):
        self.ui.perfectStreakkLabel.setText(str(self.user['perfect streak score']))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    font_path = 'src/fonts/AppleSDGothicNeo.ttf' # set font !!
    QFontDatabase.addApplicationFont(font_path)
    app.setFont(QFont("AppleSDGothicNeo"))

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
