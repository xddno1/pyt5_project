import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QApplication)
from PyQt5.QtGui import QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 声明一个颜色对象作为类属性，
        self.col = QColor(0, 0, 0)
        # 生成一个button，通过setCheckable()方法得到ToggleButton，绝对定位，绑定函数
        redb = QPushButton("Red", self)
        redb.setCheckable(True)
        redb.move(10, 10)
        redb.clicked[bool].connect(self.setColor)
        # 重复
        greenb = QPushButton("Green", self)
        greenb.setCheckable(True)
        greenb.move(10, 60)
        greenb.clicked[bool].connect(self.setColor)
        # 重复
        blueb = QPushButton("Blue", self)
        blueb.setCheckable(True)
        blueb.move(10, 110)
        blueb.clicked[bool].connect(self.setColor)
        # 生成一个QFrame，设置区域，设置背景颜色
        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" % self.col.name())
        # 设置窗体的一些属性
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("Toggle buttton")
        self.show()

    def setColor(self, pressed):
        # 调用sender()方法来获取信号源
        source = self.sender()
        # 通过传入的布尔值来设置通道的值
        if pressed:
            val = 255
        else:
            val = 0
        # 判断来源的文本内容，改变通道的值
        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        # 将改变的值再一次添加到背景颜色中
        self.square.setStyleSheet("QFrame { background-color: %s }" % self.col.name())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())