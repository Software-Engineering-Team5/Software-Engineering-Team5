import random
import sys
sys.path.append('.')

from src.module.data_processing import json_to_dict
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QFont, QFontDatabase
from src.ui.main_ui import Ui_Main
from src.window.test_select import TestSelect
from src.window.game_select import GameSelect
from src.window.basic_study import BasicStudy
from src.window.settings_window_theme import SettingThema
from src.module.user_model import *

class Main(QMainWindow):
    def __init__(self, user=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_Main()
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
        self.test_window = TestSelect(self.user)
        self.test_window.testSignal.connect(self.update_test_score)
        self.test_window.show()
        
    def update_test_score(self, result):
        self.ui.middleLevelScoreLabel.setText(result)
        
    def show_game_window(self):
        self.game_window = GameSelect(self.user)
        self.game_window.timeAttackSignal.connect(self.update_time_attack_score)
        self.game_window.perfectStreakSignal.connect(self.update_perfect_streak_score)
        self.game_window.show()
        
    def update_time_attack_score(self, result):
        self.ui.timeAttackLabel.setText(result)
        
    def update_perfect_streak_score(self, result):
        self.ui.perfectStreakkLabel.setText(result)

    def show_voca_window(self):
        self.voca_window = BasicStudy()
        self.voca_window.show()
    
    def show_setting_window(self):
        self.thema_window = SettingThema()
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

    main_window = Main()
    main_window.show()
    sys.exit(app.exec())
