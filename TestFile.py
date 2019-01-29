import CustomWidgets
from PyQt5 import QtCore, QtWidgets, QtGui
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    custom_widget = CustomWidgets.RuleDialogLocal()
    custom_widget.signals.result.connect(print)
    custom_widget.exec_()
    sys.exit(app.exec_())
