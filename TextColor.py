from PyQt5 import QtGui, QtWidgets


def change_color_of_list_of_ranges(indexes, text_edit, color='green'):
    for i in indexes:
        change_color_of_range(i, text_edit, color)


def change_color_of_range(index_range, text_edit: QtWidgets.QTextEdit, color='green'):
    print(index_range)
    min_i = index_range[0]
    print(min_i)
    max_i = index_range[1]
    amount_of_chars = max_i - min_i
    cursor = QtGui.QTextCursor(text_edit.document())
    cursor.setPosition(min_i, QtGui.QTextCursor.MoveAnchor)
    cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, amount_of_chars)
    text = cursor.selectedText()
    cursor.insertHtml("<FONT color=white style=\"BACKGROUND-COLOR: " + color + "\">" + text + "</FONT>")
