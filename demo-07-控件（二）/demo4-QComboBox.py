import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个label
        self.lb1 = QLabel("Ubuntu", self)
        # 创建一个QComboBox，并且添加选项
        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")
        # 将QComboBox和label绝对定位
        combo.move(50, 50)
        self.lb1.move(50, 150)
        # 绑定QComboBox的选择事件
        combo.activated[str].connect(self.onActivated)
        # 一些窗口的设置
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("QComboBox")
        self.show()

    # 如果选中改变文字和label的大小
    def onActivated(self, text):
        self.lb1.setText(text)
        self.lb1.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())