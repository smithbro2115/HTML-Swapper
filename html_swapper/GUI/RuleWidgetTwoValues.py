# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Programming\html_swapper\RuleWidgetTwoValues.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 24)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ruleTypeDropdown = QtWidgets.QComboBox(Form)
        self.ruleTypeDropdown.setObjectName("ruleTypeDropdown")
        self.horizontalLayout.addWidget(self.ruleTypeDropdown)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.attributeLineEdit = QtWidgets.QLineEdit(Form)
        self.attributeLineEdit.setObjectName("attributeLineEdit")
        self.horizontalLayout.addWidget(self.attributeLineEdit)
        self.attributeValueLineEdit = QtWidgets.QLineEdit(Form)
        self.attributeValueLineEdit.setObjectName("attributeValueLineEdit")
        self.horizontalLayout.addWidget(self.attributeValueLineEdit)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(2, 3)
        self.horizontalLayout.setStretch(3, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

