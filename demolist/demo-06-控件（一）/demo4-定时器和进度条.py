import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar, QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建水平进度条，设置范围
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        # 创建button，绝对定位，绑定函数
        self.btn = QPushButton("Start", self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)
        # 通过定时器(timer)对象来激活进度条
        self.timer = QBasicTimer()
        self.step = 0
        # 窗体的一些设置
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("QProssBar")
        self.show()

    # QObject及其子类都有一个timerEvent()事件处理器。我们要重新实现这个事件处理器来响应定时器事件
    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText("Finished")
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        print(self.timer)
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText("Start")
        else:
            self.timer.start(100, self)
            self.btn.setText("Stop")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
