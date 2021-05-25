import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout,QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建label和edit
        title = QLabel("Title")
        author = QLabel("Author")
        review = QLabel("Review")
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
        # 创建栅格布局
        grid = QGridLayout()
        # 设置组件间距
        grid.setSpacing(10)
        # 将组件添加进栅格布局中
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 18, 1)
        # 将栅格布局类绑定到窗口中
        self.setLayout(grid)
        # 窗口的一些设置
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Review")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())