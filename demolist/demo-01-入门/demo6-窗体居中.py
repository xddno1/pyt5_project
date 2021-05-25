import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置大小
        self.resize(250, 150)
        # 调用自定义的居中函数
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        # 得到一个指定了主窗体形状的矩形。
        qr = self.frameGeometry()
        # QtGui.QDesktopWidget提供了关于用户桌面的信息，包括屏幕尺寸。
        cp = QDesktopWidget().availableGeometry().center()
        # 指出显示器的屏幕分辨率并根据分辨率找出屏幕的中心点。
        qr.moveCenter(cp)
        # 将窗体的左上角移动到矩形qr的左上角，窗体与矩形重合，从而将窗体置于屏幕中心。
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
