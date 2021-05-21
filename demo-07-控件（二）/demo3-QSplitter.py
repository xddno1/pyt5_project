import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame, QSplitter, QStyleFactory, QApplication)
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建横向盒子
        hbox = QHBoxLayout(self)
        # 设置三个frame
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)
        # 创建一个横向QSplitter，将其中两个frame放入
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        # 创建一个纵向QSplitter，将横向QSplitter和剩下的frame放入
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        # 将纵向QSplitter放入横向布局中，并且将横向布局放入窗口中
        hbox.addWidget(splitter2)
        self.setLayout(hbox)
        # 一些窗口的设置
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("QSplitter")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
