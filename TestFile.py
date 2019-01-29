import CustomWidgets
from PyQt5 import QtCore, QtWidgets, QtGui
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    custom_widget = CustomWidgets.RuleWidgetLocal()
    custom_widget.show()
    sys.exit(app.exec_())
