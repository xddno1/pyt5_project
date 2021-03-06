import sys
from PyQt5.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication)


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        # 开启拖动监听
        self.setAcceptDrops(True)

    # 监听拖动事件，判断是否符合类型
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat("text/plain"):
            e.accept()
        else:
            e.ignore()

    # 监听拖拽放开事件
    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置一个输入行
        edit = QLineEdit("", self)
        # 设置为可拖拽的
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle("Simple drag & drop")
        self.setGeometry(300, 300, 300, 150)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())