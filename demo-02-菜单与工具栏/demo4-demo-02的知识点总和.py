import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个编辑框
        textEdit = QTextEdit()
        # 设置为QMainWindow的中心控件。中心控件会占用QMainWindow的所有剩余空间
        self.setCentralWidget(textEdit)

        # 创建QAction对象 ，设置快捷键，设置状态提示，绑定关闭窗口事件
        exitAction = QAction(QIcon("../src/boximg.png"), "Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(self.close)

        # 创建状态栏
        self.statusBar()

        # 创建菜单栏，添加目录，并绑定QAction对象
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAction)

        # 创建工具栏，并绑定QAction对象
        toolbar = self.addToolBar("Exit")
        toolbar.addAction(exitAction)

        # 一些窗口的设置
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Main Window")
        self.setWindowIcon(QIcon("SmartMedicineKit.png"))
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())