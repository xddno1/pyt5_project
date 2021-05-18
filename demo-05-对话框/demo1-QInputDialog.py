import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个button，并通过绝对布局定位，点击事件绑定showDialog方法
        self.btn = QPushButton("Dialog", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        # 创建一个QLineEdit控件，并通过绝对定位布局
        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle("Input dialog")
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name:")
        if ok:
            # 如果点击确定，修改le的内容
            self.le.setText(str(text))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())