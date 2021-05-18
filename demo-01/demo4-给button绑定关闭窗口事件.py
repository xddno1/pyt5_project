import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个按钮 并赋值，方便后面操作此按钮  第一个参数是按钮的标签，第二个参数是它的父控件
        qbtn = QPushButton("Quit", self)
        # 绑定点击事件
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # sizeHint()方法为控件返回一个推荐的尺寸
        qbtn.resize(qbtn.sizeHint())
        # 将其在窗体上移动
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Quit button")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
