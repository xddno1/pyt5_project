import sys
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton,
                             QSizePolicy, QLabel, QFontDialog, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 生成button，绝对定位，，绑定事件
        btn = QPushButton("Dialog", self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20, 20)
        btn.clicked.connect(self.showDialog)
        # 生成QLabel，绝对定位
        self.lb1 = QLabel("Studying makes me happy.", self)
        self.lb1.move(130, 20)
        # 生成垂直布局盒子，并将button和label添加到垂直盒子中
        vbox = QVBoxLayout()
        vbox.addWidget(btn)
        vbox.addWidget(self.lb1)
        # 将盒子与窗口绑定，并且设置一些窗口的参数
        self.setLayout(vbox)
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle("Font dialog")
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            # 如果有效，设置字体
            self.lb1.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())