# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Programming\HTML-Swapper\RuleWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 24)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ruleTypeDropdown = QtWidgets.QComboBox(Form)
        self.ruleTypeDropdown.setObjectName("ruleTypeDropdown")
        self.horizontalLayout_2.addWidget(self.ruleTypeDropdown)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.conditionLineEdit = QtWidgets.QLineEdit(Form)
        self.conditionLineEdit.setObjectName("conditionLineEdit")
        self.horizontalLayout_2.addWidget(self.conditionLineEdit)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(2, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

