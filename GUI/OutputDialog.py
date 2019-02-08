# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Josh\PycharmProjects\HTML-Swapper\GUI\OutputDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OutputDialog(object):
    def setupUi(self, OutputDialog):
        OutputDialog.setObjectName("OutputDialog")
        OutputDialog.resize(424, 109)
        self.gridLayout = QtWidgets.QGridLayout(OutputDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(OutputDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(OutputDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 40))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 404, 38))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.scrollWidget.setMaximumSize(QtCore.QSize(16777215, 40))
        self.scrollWidget.setObjectName("scrollWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout.addWidget(self.scrollWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(OutputDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(OutputDialog)
        self.buttonBox.accepted.connect(OutputDialog.accept)
        self.buttonBox.rejected.connect(OutputDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OutputDialog)

    def retranslateUi(self, OutputDialog):
        _translate = QtCore.QCoreApplication.translate
        OutputDialog.setWindowTitle(_translate("OutputDialog", "Output"))
        self.label.setText(_translate("OutputDialog", "TextLabel"))

