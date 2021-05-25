import sys
from PyQt5.QtWidgets import (QWidget, QCalendarWidget, QLabel, QApplication)
from PyQt5.QtCore import QDate


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个日历，画格子，绝对定位，绑定点击事件
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)
        # 创建标签，设置初始值，绝对定位
        self.lb1 = QLabel(self)
        date = cal.selectedDate()
        self.lb1.setText(date.toString())
        self.lb1.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Calender")
        self.show()

    def showDate(self, date):
        # 日历点击之后，lb改变
        self.lb1.setText(date.toString())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())