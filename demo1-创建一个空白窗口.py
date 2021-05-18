import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(800, 500)
widget.setWindowTitle('simple')
widget.show()
sys.exit(app.exec_())
