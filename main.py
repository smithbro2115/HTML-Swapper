from PyQt5 import QtCore, QtGui, QtWidgets
import YoutubeEmbedToLinkGui
import converter
import pyperclip
import TextColor
import CustomWidgets


class Gui(YoutubeEmbedToLinkGui.Ui_MainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.converter = converter.Converter()
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
        self.window = None
        self.add_rule_dialog = None

    def setup_ui_additional(self, window):
        self.window = window
        self.tagsToReplaceList = CustomWidgets.GroupListWidget()
        self.rulesList = CustomWidgets.GroupListWidget()
        self.outputList = CustomWidgets.GroupListWidget()
        self.rulesList.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.rulesList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.rulesList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.rulesList.setObjectName("rulesList")
        self.gridLayout_2.addWidget(self.rulesList, 7, 1, 1, 3)
        self.tagsToReplaceList.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.tagsToReplaceList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tagsToReplaceList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tagsToReplaceList.setObjectName("tagsToReplaceList")
        self.gridLayout_2.addWidget(self.tagsToReplaceList, 2, 1, 1, 3)
        self.outputList.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.outputList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.outputList.setObjectName("outputList")
        self.gridLayout_2.addWidget(self.outputList, 10, 1, 1, 3)
        self.addTagButton = QtWidgets.QPushButton(self.centralwidget)
        self.addTagButton.setObjectName("addTagButton")
        self.gridLayout_2.addWidget(self.addTagButton, 3, 1, 1, 1)
        self.addGroupButton = QtWidgets.QPushButton(self.centralwidget)
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
        self.gridLayout_2.addWidget(self.addGroupButton, 13, 1, 1, 3)
        self.removeTagButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeTagButton.setObjectName("removeTagButton")
        self.gridLayout_2.addWidget(self.removeTagButton, 3, 3, 1, 1)
        self.editTagButton = QtWidgets.QPushButton(self.centralwidget)
        self.editTagButton.setObjectName("editTagButton")
        self.gridLayout_2.addWidget(self.editTagButton, 3, 2, 1, 1)
        self.removeRuleButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeRuleButton.setObjectName("removeRuleButton")
        self.gridLayout_2.addWidget(self.removeRuleButton, 8, 3, 1, 1)
        self.editRuleButton = QtWidgets.QPushButton(self.centralwidget)
        self.editRuleButton.setObjectName("editRuleButton")
        self.gridLayout_2.addWidget(self.editRuleButton, 8, 2, 1, 1)
        self.editOutputButton = QtWidgets.QPushButton(self.centralwidget)
        self.editOutputButton.setObjectName("editOutputButton")
        self.gridLayout_2.addWidget(self.editOutputButton, 11, 2, 1, 1)
        self.removeOutputButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeOutputButton.setObjectName("removeOutputButton")
        self.gridLayout_2.addWidget(self.removeOutputButton, 11, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)
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
        self.addOutputButton = QtWidgets.QPushButton(self.centralwidget)
        self.addOutputButton.setObjectName("addOutputButton")
        self.gridLayout_2.addWidget(self.addOutputButton, 11, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 1, 1, 1)
        _translate = QtCore.QCoreApplication.translate
        self.editTagButton.setText(_translate("MainWindow", "Edit"))
        self.removeTagButton.setText(_translate("MainWindow", "Remove"))
        self.removeRuleButton.setText(_translate("MainWindow", "Remove"))
        self.editRuleButton.setText(_translate("MainWindow", "Edit"))
        self.removeOutputButton.setText(_translate("MainWindow", "Remove"))
        self.editOutputButton.setText(_translate("MainWindow", "Edit"))
        self.addOutputButton.setText(_translate("MainWindow", "Add"))
        self.label_3.setText(_translate("MainWindow", "Rules:"))
        self.label_4.setText(_translate("MainWindow", "Output:"))
        self.addTagButton.setText(_translate("MainWindow", "Add"))
        self.addGroupButton.setText(_translate("MainWindow", "Add Group"))
        self.addRuleButton.setText(_translate("MainWindow", "Add"))
        self.label_5.setText(_translate("MainWindow", "Tags To Replace:"))
        self.edited.setReadOnly(True)
        self.original.textChanged.connect(self.original_text_changed)
        self.original.verticalScrollBar().valueChanged.connect(lambda x: self.text_slider_change(x, self.edited))
        self.edited.verticalScrollBar().valueChanged.connect(lambda x: self.text_slider_change(x, self.original))
        self.copyButton.clicked.connect(self.copy_edited)
        self.actionCopyEdited.triggered.connect(self.copy_edited)
        self.copyPasted.clicked.connect(self.copy_pasted_changed)
        self.copy_pasted_changed()
        self.copied_label_animation = self.fade_in_and_out()
        self.copiedLabel.hide()
        # self.tagToReplaceLineEdit.setCompleter(self.tag_to_replace_completer)
        self.tag_to_replace_completer.setModel(self.tag_to_replace_complete_model)
        self.tag_to_replace_complete_model.setStringList(self.all_html_tags)
        self.addRuleButton.clicked.connect(self.add_rule_button_clicked)
        self.removeRuleButton.clicked.connect(lambda: self.remove_item_from_list_widget(self.rulesList))
        self.editRuleButton.clicked.connect(self.edit_rule_button_clicked)
        self.addTagButton.clicked.connect(self.add_tag_button_clicked)
        self.editTagButton.clicked.connect(self.edit_tag_button_clicked)
        self.removeTagButton.clicked.connect(lambda: self.remove_item_from_list_widget(self.tagsToReplaceList))
        self.addGroupButton.clicked.connect(self.add_group)
        self.add_group()

    def add_tag_button_clicked(self):
        list_item = CustomWidgets.TagToReplaceResult()
        self.tagsToReplaceList.addItem(list_item)
        index = self.tagsToReplaceList.row(list_item)
        self.tagsToReplaceList.editItem(self.tagsToReplaceList.item(index))

    def edit_tag_button_clicked(self):
        items = self.tagsToReplaceList.selectedItems()
        if len(items) == 1:
            self.tagsToReplaceList.editItem(items[0])

    def add_rule_button_clicked(self):
        self.add_rule_dialog = CustomWidgets.RuleDialogLocal()
        try:
            self.add_rule_dialog.signals.disconnect()
        except TypeError:
            pass
        self.add_rule_dialog.signals.result.connect(self.append_rule)
        self.add_rule_dialog.show()

    def append_rule(self, rule_dict):
        list_item = CustomWidgets.RuleResult(rule_dict['rule'].readable_string)
        list_item.rule = rule_dict['rule']
        list_item.rule_dialog = rule_dict['dialog']
        self.rulesList.addItem(list_item)

    def remove_item_from_list_widget(self, list_widget):
        for item in list_widget.selectedItems():
            if not isinstance(item, CustomWidgets.GroupResult):
                list_widget.takeItem(list_widget.row(item))
            else:
                self.remove_group_from_all_lists(item.id)

    def edit_rule_button_clicked(self):
        if len(self.rulesList.selectedItems()) == 1:
            item = self.rulesList.selectedItems()[0]
            self.add_rule_dialog = self.rulesList.item(self.rulesList.row(item)).rule_dialog
            self.add_rule_dialog.signals.disconnect()
            self.add_rule_dialog.signals.result.connect(self.edit_rule)
            self.add_rule_dialog.show()

    def edit_rule(self, rule_dict):
        self.remove_item_from_list_widget(self.rulesList)
        self.append_rule(rule_dict)

    def add_group(self):
        rule_list_item = CustomWidgets.GroupResult(len(self.get_list_of_groups(self.rulesList)) + 1)
        tags_list_item = CustomWidgets.GroupResult(len(self.get_list_of_groups(self.tagsToReplaceList)) + 1)
        out_list_item = CustomWidgets.GroupResult(len(self.get_list_of_groups(self.outputList)) + 1)
        self.rulesList.addItem(rule_list_item)
        self.tagsToReplaceList.addItem(tags_list_item)
        self.outputList.addItem(out_list_item)

    def remove_group_from_all_lists(self, number):
        list_widgets = [self.tagsToReplaceList, self.rulesList, self.outputList]
        for list_widget in list_widgets:
            self.remove_group(list_widget, number)

    def remove_group(self, list_widget, number):
        for index in range(0, list_widget.count()):
            list_item = list_widget.item(index)
            try:
                if list_item.id == number and list_item.id != 1:
                    list_widget.takeItem(index)
            except AttributeError:
                pass
        self.rename_group_list_items(self.get_list_of_groups(list_widget))

    @staticmethod
    def get_list_of_group_ids(list_widget):
        group_ids = []
        for index in range(0, list_widget.count()):
            list_item = list_widget.item(index)
            try:
                group_ids.append(list_item.id)
            except AttributeError:
                pass
        return group_ids

    @staticmethod
    def rename_group_list_items(items):
        for index in range(0, len(items)):
            correct_id = index + 1
            item = items[index]
            if item.id != correct_id:
                item.id = correct_id
                item.setText("Group " + str(correct_id))

    def get_list_of_rules(self):
        rules = []
        for index in range(0, self.rulesList.count()):
            rules.append(self.rulesList.item(index).rule)
        return rules

    def get_list_of_tags(self):
        tags = []
        for index in range(0, self.tagsToReplaceList.count()):
            tags.append(self.tagsToReplaceList.item(index).letters)
        return tags

    @staticmethod
    def get_list_of_groups(group_list):
        groups = []
        for index in range(0, group_list.count()):
            list_item = group_list.item(index)
            if isinstance(list_item, CustomWidgets.GroupResult):
                groups.append(list_item)
        return groups

    def text_slider_change(self, event, scroll_to_track):
        scroll_to_track.verticalScrollBar().setValue(event)

    def convert_local(self):
        edited, indexes = self.converter.convert(self.original.toPlainText(), self.get_list_of_tags(),
                                                 self.get_list_of_rules())
        self.edited.setPlainText(edited)
        TextColor.change_color_of_list_of_ranges(indexes, self.edited, color='#20C520')
        if self.copyPasted.isChecked():
            self.copy_edited()
        if self.deleteAfterCopied.isChecked() and self.deleteAfterCopied.isEnabled():
            self.original.clear()

    def original_text_changed(self):
        if self.original.toPlainText() != '':
            self.convert_local()
        else:
            self.edited.clear()

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
            print('fail')

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
