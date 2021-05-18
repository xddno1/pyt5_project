import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QColorDialog, QApplication)
from PyQt5.QtGui import QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 默认颜色为黑色
        col = QColor(0, 0, 0)
        # 创建一个button，绝对定位，绑定事件
        self.btn = QPushButton("Dialog", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        # 创建一个QFrame，设置背景颜色的样式，设置大小
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle("Color dialog")
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            # 如果颜色颜色有效，则修改样式
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())