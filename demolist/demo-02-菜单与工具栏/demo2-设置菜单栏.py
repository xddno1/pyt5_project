import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建QAction对象
        exitAction = QAction(QIcon("../../src/boximg.png"), "&退出", self)
        exitAction1 = QAction(QIcon("../../src/boximg.png"), "&啥也不是", self)
        # 设置快捷键属性
        exitAction.setShortcut("Ctrl+Q")
        # 设置状态栏
        exitAction1.setStatusTip("按了也没用")
        exitAction.setStatusTip("Exit application")
        # 发出triggered信号。这个信号连接到了QApplication的quit()方法。从而使程序停止。
        exitAction.triggered.connect(qApp.quit)
        # 开启状态栏
        self.statusBar()
        # 开启菜单栏，并赋值
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        # 在菜单栏添加QAction对象
        fileMenu.addAction(exitAction)
        fileMenu.addAction(exitAction1)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Menubar")
        self.setWindowIcon(QIcon("../../src/boximg.png"))
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
