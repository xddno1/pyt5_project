import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置一个textedit，并铺满剩余窗口
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        # 创建状态栏
        self.statusBar()
        # 创建一个QAction，设置快捷键，设置状态提示，绑定点击事件
        openFile = QAction(QIcon("../src/boximg.png"), "Open", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("Open new File")
        openFile.triggered.connect(self.showDialog)
        # 创建一个菜单栏，添加菜单，绑定QAction
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(openFile)
        # 窗体的一些设置
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("File dialog")
        self.setWindowIcon(QIcon("../src/boximg.png"))
        self.show()

    def showDialog(self):
        # 弹出文件选择器
        fname = QFileDialog.getOpenFileName(self, "Open file", "/home")
        # 如果选择了文件
        if fname[0]:
            # 打开第一个文件
            f = open(fname[0], "r")
            # with用于捕获异常，发生错误则退出程序
            with f:
                # 读取文件，将数据设置进textedit组件中
                data = f.read()
                self.textEdit.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())