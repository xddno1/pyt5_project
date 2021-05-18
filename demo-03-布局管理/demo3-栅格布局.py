import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 使用类QGridLayout创建网格布局,并且绑定到窗口上
        grid = QGridLayout()
        self.setLayout(grid)

        names = ["Cls", "Bck", "", "Close",
                 "7", "8", "9", "/",
                 "4", "5", "6", "*",
                 "1", "2", "3", "-",
                 "0", ".", "=", "+"]

        # 生成二维矩阵5*4
        positions = [(i, j) for i in range(5) for j in range(4)]

        # zip(positions, names)为将 其打包成元组，例子:(positions[0], names[0])
        # for循环解析：遍历positions，将对应的names生成button的名字，并绑定到对应的栅格中
        for position, name in zip(positions, names):
            if name == "":
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
        # 一些窗口的设置
        self.move(300, 150)
        self.setWindowTitle("Calculator")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
