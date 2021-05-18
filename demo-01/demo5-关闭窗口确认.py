import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QPushButton
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("MEssage box")
        self.show()

    # 传入event
    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Message", "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        # 如果点击确定，同意这次操作，否则忽略
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
