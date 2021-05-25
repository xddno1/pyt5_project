import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个数字显示组件和一个滑动条组件
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)
        # 使用垂直盒子布局，并将两个组件一次添加进盒子中
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
        # 将盒子与窗口绑定
        self.setLayout(vbox)
        # 两个组件之间的绑定
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Signal & slott")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())