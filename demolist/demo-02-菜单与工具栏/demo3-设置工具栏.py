import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建QAction对象
        exitAction = QAction(QIcon("../../src/boximg.png"), "Exit", self)
        # 设置快捷键
        exitAction.setShortcut("Ctrl+Q")
        # 发出triggered信号。这个信号连接到了QApplication的quit()方法。从而使程序停止。
        exitAction.triggered.connect(qApp.quit)

        # 创建工具栏并绑定QAction对象
        toolbar = self.addToolBar("Exit")
        toolbar.addAction(exitAction)

        # 一些窗口的设置
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Toolbar")
        self.setWindowIcon(QIcon("SmartMedicineKit.png"))
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())