# global_settings.py

from PyQt6.QtCore import QSettings

class GlobalSettings:
    def __init__(self):
        self.settings = QSettings("MyCompany", "MyApp")

    def set_theme(self, theme_file):
        self.settings.setValue("theme", theme_file)

    def get_theme(self):
        return self.settings.value("theme", "src/module/light_theme.qss")
