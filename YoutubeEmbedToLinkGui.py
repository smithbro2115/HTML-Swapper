# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Josh\PycharmProjects\youtube_embed_to_link\YoutubeEmbedToLinkGui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.edited = QtWidgets.QTextEdit(self.centralwidget)
        self.edited.setObjectName("edited")
        self.gridLayout.addWidget(self.edited, 0, 1, 1, 1)
        self.copyButton = QtWidgets.QPushButton(self.centralwidget)
        self.copyButton.setObjectName("copyButton")
        self.gridLayout.addWidget(self.copyButton, 1, 1, 1, 1)
        self.original = QtWidgets.QTextEdit(self.centralwidget)
        self.original.setObjectName("original")
        self.gridLayout.addWidget(self.original, 0, 0, 1, 1)
        self.deleteAfterCopied = QtWidgets.QCheckBox(self.centralwidget)
        self.deleteAfterCopied.setObjectName("deleteAfterCopied")
        self.gridLayout.addWidget(self.deleteAfterCopied, 2, 0, 1, 1)
        self.copyPasted = QtWidgets.QCheckBox(self.centralwidget)
        self.copyPasted.setObjectName("copyPasted")
        self.gridLayout.addWidget(self.copyPasted, 1, 0, 1, 1)
        self.copiedLabel = QtWidgets.QLabel(self.centralwidget)
        self.copiedLabel.setEnabled(True)
        self.copiedLabel.setStyleSheet("color: rgba(0, 255, 0, 255);")
        self.copiedLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.copiedLabel.setObjectName("copiedLabel")
        self.gridLayout.addWidget(self.copiedLabel, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 21))
        self.menubar.setObjectName("menubar")
        self.menuedti = QtWidgets.QMenu(self.menubar)
        self.menuedti.setObjectName("menuedti")
        MainWindow.setMenuBar(self.menubar)
        self.actionCopyEdited = QtWidgets.QAction(MainWindow)
        self.actionCopyEdited.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionCopyEdited.setObjectName("actionCopyEdited")
        self.menuedti.addAction(self.actionCopyEdited)
        self.menubar.addAction(self.menuedti.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.copyButton.setText(_translate("MainWindow", "Copy"))
        self.deleteAfterCopied.setText(_translate("MainWindow", "Delete original version after copied"))
        self.copyPasted.setText(_translate("MainWindow", "Copy edited version after pasting original"))
        self.copiedLabel.setText(_translate("MainWindow", "Copied"))
        self.menuedti.setTitle(_translate("MainWindow", "Edit"))
        self.actionCopyEdited.setText(_translate("MainWindow", "Copy Edited"))
        self.actionCopyEdited.setShortcut(_translate("MainWindow", "Ctrl+Shift+C"))

