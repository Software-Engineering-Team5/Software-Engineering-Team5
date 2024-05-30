import sys
sys.path.append('.')

from PyQt6.QtWidgets import QApplication, QMainWindow
from src.ui.GameSelectWindow import Ui_GameSelectWindow
from src.window.perfect_streak import PerfectStreakGame
from src.window.time_attack import TimeAttackGame

class GameSelectWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GameSelectWindow()
        self.ui.setupUi(self)
        self.ui.timeAttackButton.clicked.connect(self.time_attack)
        self.ui.perfectStreakButton.clicked.connect(self.perfect_streak)

    def time_attack(self):
        self.test_window = TimeAttackGame()
        self.test_window.show()
    
    def perfect_streak(self):
        self.test_window = PerfectStreakGame()
        self.test_window.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = GameSelectWindow()
    widget.show()
    sys.exit(app.exec())




