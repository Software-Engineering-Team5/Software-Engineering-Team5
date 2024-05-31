class ThemeManager:
    @staticmethod
    def apply_theme(app, theme_file):
        try:
            with open(theme_file, "r") as file:
                stylesheet = file.read()
                app.setStyleSheet(stylesheet)  # QApplication 객체에 스타일 시트 적용
                print("Theme applied:", theme_file)  # 디버깅 출력
        except FileNotFoundError:
            print(f"Theme file {theme_file} not found.")
