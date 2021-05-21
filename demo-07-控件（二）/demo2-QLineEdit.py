import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个label，创建一个QLineEdit
        self.lb1 = QLabel(self)
        qle = QLineEdit(self)
        # qle绝对定位，label绝对定位
        qle.move(60, 100)
        self.lb1.move(60, 40)
        # QLineEdit绑定到label的值里面
        qle.textChanged[str].connect(self.onChanged)
        # 一些窗体的设置
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("QLineEdit")
        self.show()

    def onChanged(self, text):
        # 将QLineEdit的值在label中展示，并且动态改变label的大小
        self.lb1.setText(text)
        self.lb1.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())