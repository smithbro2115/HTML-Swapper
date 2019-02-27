from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import GUI, CustomWidgets, TextColor
from Converter import converter
import pyperclip


# TODO Add progress bar or circle for converter
# TODO Run stress tests
# TODO Maybe add a text color change when modified


class Gui(GUI.Ui_MainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.copied_label_animation = None
        self.fade_effect = None
        self.fade_animation = None
        self.unfade_effect = None
        self.unfade_animation = None
        self.all_html_tags = ['!DOCTYPE html', '!-- --', 'a', 'abbr', 'address', 'area', 'article', 'aside', 'audio',
                              'b', 'base', 'bdi', 'bdo', 'blockquote', 'body', 'br', 'button', 'canvas', 'caption',
                              'cite', 'code', 'col', 'colgroup', 'data', 'datalist', 'dd', 'del', 'details', 'dfn',
                              'dialog', 'div', 'dl', 'dt', 'em', 'embed', 'fieldset', 'figure', 'footer', 'form',
                              'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hgroup', 'hr', 'html', 'i',
                              'iframe', 'img', 'input', 'ins', 'kbd', 'keygen', 'label', 'legend', 'li', 'link',
                              'main', 'map', 'mark', 'menu', 'menuitem', 'meta', 'meter', 'nav', 'noscript', 'object',
                              'ol', 'optgroup', 'option', 'output', 'p', 'param', 'pre', 'progress', 'q', 'rb', 'rt',
                              'rp', 'rtc', 'ruby', 's', 'samp', 'script', 'section', 'select', 'small', 'source',
                              'span', 'strong', 'style', 'sub', 'summary', 'sup', 'table', 'tbody', 'td', 'template',
                              'textarea', 'tfoot', 'th', 'thead', 'time', 'title', 'tr', 'track', 'u', 'ul', 'var',
                              'video', 'wbr']
        self.tag_to_replace_complete_model = QtCore.QStringListModel()
        self.tag_to_replace_completer = QtWidgets.QCompleter()
        self.thread_pool = QtCore.QThreadPool()
        self.window = None
        self.add_rule_dialog = None
        self.current_converter = None

    def setup_ui_additional(self, window):
        self.window = window
        self.rulesList = CustomWidgets.RulesListWidget()
        self.outputArea = CustomWidgets.OutputScrollArea()
        self.rulesList.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.rulesList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.rulesList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.rulesList.setObjectName("rulesList")
        self.gridLayout_2.addWidget(self.rulesList, 7, 1, 1, 3)
        self.outputArea.setObjectName("outputArea")
        self.gridLayout_2.addWidget(self.outputArea, 10, 1, 1, 3)
        self.addGroupButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeGroupButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addGroupButton.sizePolicy().hasHeightForWidth())
        self.addGroupButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.addGroupButton.setFont(font)
        self.addGroupButton.setIconSize(QtCore.QSize(2, 2))
        self.addGroupButton.setAutoDefault(False)
        self.addGroupButton.setDefault(False)
        self.addGroupButton.setFlat(False)
        self.addGroupButton.setObjectName("addGroupButton")
        self.gridLayout_2.addWidget(self.addGroupButton, 13, 1, 1, 2)
        self.removeGroupButton.setFont(font)
        self.removeGroupButton.setIconSize(QtCore.QSize(2, 2))
        self.removeGroupButton.setAutoDefault(False)
        self.removeGroupButton.setDefault(False)
        self.removeGroupButton.setFlat(False)
        self.removeGroupButton.setObjectName("addGroupButton")
        self.gridLayout_2.addWidget(self.removeGroupButton, 13, 3, 1, 1)
        self.removeRuleButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeRuleButton.setObjectName("removeRuleButton")
        self.gridLayout_2.addWidget(self.removeRuleButton, 8, 3, 1, 1)
        self.editRuleButton = QtWidgets.QPushButton(self.centralwidget)
        self.editRuleButton.setObjectName("editRuleButton")
        self.gridLayout_2.addWidget(self.editRuleButton, 8, 2, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 12, 1, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 9, 1, 1, 1)
        self.addRuleButton = QtWidgets.QPushButton(self.centralwidget)
        self.addRuleButton.setObjectName("addRuleButton")
        self.gridLayout_2.addWidget(self.addRuleButton, 8, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 1, 1, 1)
        _translate = QtCore.QCoreApplication.translate
        self.removeGroupButton.setText(_translate("MainWindow", "Remove"))
        self.removeRuleButton.setText(_translate("MainWindow", "Remove"))
        self.editRuleButton.setText(_translate("MainWindow", "Edit"))
        self.label_3.setText(_translate("MainWindow", "Rules:"))
        self.label_4.setText(_translate("MainWindow", "Output:"))
        self.addGroupButton.setText(_translate("MainWindow", "Add Group"))
        self.addRuleButton.setText(_translate("MainWindow", "Add"))
        self.edited.setReadOnly(True)
        self.thread_pool.setMaxThreadCount(1)
        self.original.textChanged.connect(self.original_text_changed)
        self.original.verticalScrollBar().valueChanged.connect(lambda x: self.text_slider_change(x, self.edited))
        self.edited.verticalScrollBar().valueChanged.connect(lambda x: self.text_slider_change(x, self.original))
        self.copyButton.clicked.connect(self.copy_edited)
        self.actionCopyEdited.triggered.connect(self.copy_edited)
        self.copyPasted.clicked.connect(self.copy_pasted_changed)
        self.copy_pasted_changed()
        self.copied_label_animation = self.fade_in_and_out()
        self.copiedLabel.hide()
        self.rulesList.signals.removed_group.connect(self.remove_group_from_all_lists)
        self.addRuleButton.clicked.connect(self.rulesList.add_rule_button_clicked)
        self.removeRuleButton.clicked.connect(self.rulesList.remove_item_from_list_widget)
        self.editRuleButton.clicked.connect(self.rulesList.edit_rule_button_clicked)
        self.removeGroupButton.clicked.connect(self.rulesList.remove_item_from_list_widget)
        self.addGroupButton.clicked.connect(self.add_group_to_all_lists)
        self.outputArea.signals.changed.connect(self.convert_local)
        self.convertCheckBox.stateChanged.connect(self.convert_local)
        self.rulesList.local_signals.changed_rules.connect(self.send_rules_to_outputs)
        self.add_group_to_all_lists()

    def add_group_to_all_lists(self):
        self.outputArea.add_group()
        self.rulesList.add_group()

    def remove_group_from_all_lists(self, number):
        list_widgets = [self.rulesList, self.outputArea]
        for list_widget in list_widgets:
            list_widget.remove_group_item(number)
            list_widget.rename_group_list_items()
        self.send_rules_to_outputs()

    def text_slider_change(self, event, scroll_to_track):
        scroll_to_track.verticalScrollBar().setValue(event)

    def convert_local(self):
        if self.convertCheckBox.isChecked():
            if self.outputArea.valid:
                try:
                    if self.current_converter.running:
                        self.current_converter.cancel = True
                except AttributeError:
                    pass
                self.current_converter = converter.Converter(self.original.toPlainText(),
                                                             self.get_list_of_groups_with_tags_and_rules(),
                                                             self.outputArea.get_dict_of_group_outputs())
                self.current_converter.signals.finished.connect(lambda x: self.edited.setPlainText(x))
                self.thread_pool.start(self.current_converter)
                # TextColor.change_color_of_list_of_ranges(indexes, self.edited, color='#20C520')6
                if self.copyPasted.isChecked():
                    self.copy_edited()
                if self.deleteAfterCopied.isChecked() and self.deleteAfterCopied.isEnabled():
                    self.original.clear()

    def get_list_of_groups_with_tags_and_rules(self):
        groups = []
        for group_item in self.rulesList.get_list_of_groups():
            g_int = group_item.id
            group = self.rulesList.get_list_of_rules_from_group(g_int)
            groups.append(group)
        return groups

    def original_text_changed(self):
        if self.original.toPlainText() != '':
            self.convert_local()
        else:
            self.edited.clear()

    def send_rules_to_outputs(self):
        self.outputArea.send_rules_to_outputs(self.get_list_of_groups_with_tags_and_rules())

    def copy_pasted_changed(self):
        if self.copyPasted.isChecked():
            self.deleteAfterCopied.setDisabled(False)
        else:
            self.deleteAfterCopied.setDisabled(True)

    def copy_edited(self):
        pyperclip.copy(self.edited.toPlainText())
        self.edited.setFocus()
        self.edited.selectAll()
        self.copiedLabel.show()
        self.copied_label_animation.start()

    def fade_in_and_out(self):
        animations = QtCore.QSequentialAnimationGroup()
        animations.addAnimation(self.unfade(self.copiedLabel))
        animations.addPause(250)
        animations.addAnimation(self.fade())
        return animations

    def fade(self):
        self.fade_animation = QtCore.QPropertyAnimation(self.unfade_effect, b"opacity")
        self.fade_animation.setDuration(250)
        self.fade_animation.setStartValue(1)
        self.fade_animation.setEndValue(0)
        return self.fade_animation

    def unfade(self, widget):
        self.unfade_effect = QtWidgets.QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.unfade_effect)
        self.unfade_animation = QtCore.QPropertyAnimation(self.unfade_effect, b"opacity")
        self.unfade_animation.setDuration(250)
        self.unfade_animation.setStartValue(.1)
        self.unfade_animation.setEndValue(1)
        return self.unfade_animation


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.settings = QtCore.QSettings('Brinkman', 'App')
        try:
            self.restoreGeometry(self.settings.value('geometry'))
            self.restoreState(self.settings.value('windowState', ''))
        except TypeError:
            pass

    def closeEvent(self, event):
        self.settings.setValue('geometry', self.saveGeometry())
        self.settings.setValue('windowState', self.saveState())
        QtWidgets.QMainWindow.closeEvent(self, event)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Gui()
    MainWindow = MainWindow()
    ui.setupUi(MainWindow)
    ui.setup_ui_additional(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
