import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 水平布局，创建QPixmap
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("./src/turingLogo.jpg")
        # 创建label，设置label的值为qixmap
        lb1 = QLabel(self)
        lb1.setPixmap(pixmap)
        # 将label放入水平布局，再将水平布局放入窗口
        hbox.addWidget(lb1)
        self.setLayout(hbox)
        # 窗口的一些设置
        self.move(300, 200)
        self.setWindowTitle("Red Tank")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
