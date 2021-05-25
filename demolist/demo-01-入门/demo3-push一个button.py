import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 下面的代码无缘无故报错，注释就可运行
        # QToolTip.setFont("SansSerif", 10)
        # 设置按钮的提示
        self.setToolTip("This is a <b>QWidget</b> widget")
        # 创建一个按钮 并赋值，方便后面操作此按钮  第一个参数是按钮的标签，第二个参数是它的父控件
        btn = QPushButton("Button", self)
        # 设置按钮提示
        btn.setToolTip("This is a <b>QPushButon</b> widget")
        # sizeHint()方法为控件返回一个推荐的尺寸
        btn.resize(btn.sizeHint())
        # 将其在窗体上移动
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Tooltips")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())