import sys
sys.path.append('.')
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QSettings

from src.ui.settings_window_theme import Ui_SettingThema  # 수정


class SettingThema(QMainWindow):
    def __init__(self):
        super().__init__()

        # 테마 설정 페이지 UI
        self.theme_settings_ui = Ui_SettingThema()
        self.theme_settings_ui.setupUi(self)

        # QSettings 초기화
        self.settings = QSettings("MyCompany", "MyApp")

        # 메뉴 버튼 클릭 이벤트
        self.theme_settings_ui.menuButtonTheme.clicked.connect(self.showThemeSettingsPage)

        # 저장 버튼 눌렀을 때
        self.theme_settings_ui.pushButton.clicked.connect(self.apply_theme)

        # 초기화
        self.initUI()

    def initUI(self):
        self.load_last_theme()  # 저장된 테마 로드
        self.showThemeSettingsPage()  # 기본값으로 테마 설정 페이지를 보여줌

    def showThemeSettingsPage(self):
        self.theme_settings_ui.centralwidget.show()
        self.setCentralWidget(self.theme_settings_ui.centralwidget)

    def apply_theme(self):
        if self.theme_settings_ui.radioButton.isChecked():
            theme_file = "src/module/light_theme.qss"
        elif self.theme_settings_ui.radioButton_2.isChecked():
            theme_file = "src/module/dark_theme.qss"
        elif self.theme_settings_ui.radioButton_3.isChecked():
            theme_file = "src/module/plant_theme.qss"
        else:
            theme_file = "src/module/light_theme.qss"  # Default theme

        self.load_theme(theme_file)
        self.settings.setValue("theme", theme_file)

    def load_last_theme(self):
        theme_file = self.settings.value("theme", "light_theme.qss")
        self.load_theme(theme_file)

    def load_theme(self, theme_file):
        try:
            with open(theme_file, "r") as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Theme file {theme_file} not found.")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    main_window = SettingThema()
    main_window.show()

    sys.exit(app.exec())
