import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建Qlable对象，并且通过对象的move方法对改对象进行移动
        lb11 = QLabel("You", self)
        lb11.move(15, 10)

        lb12 = QLabel("are", self)
        lb12.move(35, 44)

        lb13 = QLabel("best", self)
        lb13.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Absolute")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())