import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建两个button
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        # QHBoxLayout与QVBoxLayout是水平与垂直放置控件的两个基本布局类

        # 可以理解为创建了一个水平布局的div块
        # hbox为水平布局类，添加了两个按钮
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 创建了垂直布局类，添加了刚刚创建的水平布局类
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 将vbox放在窗口上，并设置一些窗口的基础属性
        self.setLayout(vbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Buttons")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())