from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QSettings
from PySide6.QtGui import QFont

from ui_settings_window_font import Ui_FontSettingsWindow  # 수정

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 폰트 크기 설정 페이지 UI
        self.font_settings_ui = Ui_FontSettingsWindow()
        self.font_settings_ui.setupUi(self)

        # QSettings 초기화
        self.settings = QSettings("MyCompany", "MyApp")

        # 라디오 버튼 클릭 시 이벤트 핸들러 설정
        self.font_settings_ui.fontSizedefault.clicked.connect(self.setDefaultFontSize)
        self.font_settings_ui.fontSizeIncrease.clicked.connect(self.setIncreaseFontSize)
        self.font_settings_ui.fontSizeSaveButton.clicked.connect(self.saveFontSize)

        # 초기화
        self.initUI()

    def initUI(self):
        self.applyFontSize()
        self.showFontSettingsPage()  # 기본값으로 폰트 설정 페이지를 보여줌

    def showFontSettingsPage(self):
        self.font_settings_ui.centralwidget.show()
        self.setCentralWidget(self.font_settings_ui.centralwidget)

    def setDefaultFontSize(self):
        self.currentFontSize = 12
        self.applyFontSize()

    def setIncreaseFontSize(self):
        self.currentFontSize = 22
        self.applyFontSize()

    def saveFontSize(self):
        self.settings.setValue("fontSize", self.currentFontSize)
        self.applyFontSize()

    def applyFontSize(self):
        savedFontSize = self.settings.value("fontSize", 12)
        self.currentFontSize = int(savedFontSize)

        font = QFont()
        font.setPointSize(self.currentFontSize)

        # 모든 UI 요소에 대해 폰트 크기 적용
        self.font_settings_ui.label.setFont(font)
        self.font_settings_ui.fontSizedefault.setFont(font)
        self.font_settings_ui.fontSizeIncrease.setFont(font)
        self.font_settings_ui.fontSizeSaveButton.setFont(font)
        self.font_settings_ui.exitButton.setFont(font)
        self.font_settings_ui.menuButtonTheme.setFont(font)
        self.font_settings_ui.menuButtonFont.setFont(font)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
