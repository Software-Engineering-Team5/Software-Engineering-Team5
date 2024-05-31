# theme_manager.py

class ThemeManager:
    @staticmethod
    def apply_theme(app, theme_file):
        try:
            with open(theme_file, "r") as file:
                app.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Theme file {theme_file} not found.")
