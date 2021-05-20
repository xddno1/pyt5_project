import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个水平滑动条，设置为无法通过tab获取焦点，设置区域，绑定方法
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)
        # 创建了一个QLabel控件并为它设置了一个初始音量图像，限定大小
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("./src/boximg.png"))
        self.label.setGeometry(160, 40, 80, 30)
        # 窗体的一些设置
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("QSlider")
        self.show()

    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(QPixmap("./src/boximg.png"))
        elif value <= 30:
            self.label.setPixmap(QPixmap("./src/turingLogo.jpg"))
        elif value < 80:
            self.label.setPixmap(QPixmap("./src/boximg.png"))
        else:
            self.label.setPixmap(QPixmap("./src/turingLogo.jpg"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
