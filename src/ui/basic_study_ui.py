from PyQt6.QtCore import QCoreApplication, QRect, Qt, QMetaObject
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFrame

class Ui_BasicStudy(object):
    def setupUi(self, BasicStudy):
        if not BasicStudy.objectName():
            BasicStudy.setObjectName("BasicStudy")
        BasicStudy.resize(1000, 600)
        self.pushButton_before = QPushButton(BasicStudy)
        self.pushButton_before.setObjectName("pushButton_before")
        self.pushButton_before.setGeometry(QRect(40, 250, 100, 70))
        font = QFont()
        font.setPointSize(16)
        self.pushButton_before.setFont(font)
        self.pushButton_after = QPushButton(BasicStudy)
        self.pushButton_after.setObjectName("pushButton_after")
        self.pushButton_after.setGeometry(QRect(860, 250, 100, 70))
        self.pushButton_after.setFont(font)
        self.pushButton_main = QPushButton(BasicStudy)
        self.pushButton_main.setObjectName("pushButton_main")
        self.pushButton_main.setGeometry(QRect(400, 540, 200, 41))
        self.label_eng = QLabel(BasicStudy)
        self.label_eng.setObjectName("label_eng")
        self.label_eng.setGeometry(QRect(320, 221, 251, 51))
        self.label_eng.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 수정된 부분
        self.label_eng.setStyleSheet("color: black;")  # 기본 색상으로 설정
        self.label_kor = QLabel(BasicStudy)
        self.label_kor.setObjectName("label_kor")
        self.label_kor.setGeometry(QRect(350, 230, 300, 100))
        self.label_kor.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 수정된 부분
        self.line = QFrame(BasicStudy)
        self.line.setObjectName("line")
        self.line.setGeometry(QRect(140, 20, 20, 550))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(BasicStudy)
        self.line_2.setObjectName("line_2")
        self.line_2.setGeometry(QRect(840, 20, 20, 550))
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(BasicStudy)
        QMetaObject.connectSlotsByName(BasicStudy)

    def retranslateUi(self, BasicStudy):
        BasicStudy.setWindowTitle(QCoreApplication.translate("BasicStudy", "Form", None))
        self.pushButton_before.setText(QCoreApplication.translate("BasicStudy", "이전", None))
        self.pushButton_after.setText(QCoreApplication.translate("BasicStudy", "다음", None))
        self.pushButton_main.setText(QCoreApplication.translate("BasicStudy", "홈으로", None))
        self.label_eng.setText("")
        self.label_kor.setText("")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    BasicStudy = QWidget()
    ui = Ui_BasicStudy()
    ui.setupUi(BasicStudy)
    BasicStudy.show()
    sys.exit(app.exec())
