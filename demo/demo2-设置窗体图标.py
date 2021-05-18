import sys
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets


class Icon(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Icon")
        # 下面的代码用于设置窗体图标
        self.setWindowIcon(QIcon("../src/boximg.png"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    icon = Icon()
    icon.show()
    sys.exit(app.exec_())
