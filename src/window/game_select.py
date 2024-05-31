import sys
sys.path.append('.')

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import pyqtSignal
from src.ui.game_select_ui import Ui_GameSelect
from src.window.perfect_streak import PerfectStreak
from src.window.time_attack import TimeAttack

class GameSelect(QMainWindow):
    timeAttackSignal = pyqtSignal(str)
    perfectStreakSignal = pyqtSignal(str)
    
    def __init__(self, user=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_GameSelect()
        self.ui.setupUi(self)
        self.user = user
        self.ui.timeAttackButton.clicked.connect(self.time_attack)
        self.ui.perfectStreakButton.clicked.connect(self.perfect_streak)

    def time_attack(self):
        self.time_attack_window = TimeAttack(self.user)
        self.time_attack_window.timeAttackSignal.connect(self.update_time_attack_signal)
        self.time_attack_window.show()
    
    def perfect_streak(self):
        self.perfect_streak_window = PerfectStreak(self.user)
        self.perfect_streak_window.perfectStreakSignal.connect(self.update_perfect_streak_signal)
        self.perfect_streak_window.show()
        
    def update_time_attack_signal(self, result):
        self.timeAttackSignal.emit(result)
        
    def update_perfect_streak_signal(self, result):
        self.perfectStreakSignal.emit(result)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = GameSelect()
    widget.show()
    sys.exit(app.exec())




