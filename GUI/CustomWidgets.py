from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal
import re
from Converter import Rules
from GUI import AddRuleDialog, OutputWidget, OutputDialog
from inspect import signature
from Converter.Output import Output

html_tags = ['!DOCTYPE html', '!-- --', 'a', 'abbr', 'address', 'area', 'article', 'aside', 'audio',
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


class OutputDialogSigs(QtCore.QObject):
    accepted = pyqtSignal(list)
    button_pushed = pyqtSignal(str)
    valid = pyqtSignal(bool)


class OutputRuleButton(QtWidgets.QPushButton):
    def __init__(self):
        super(OutputRuleButton, self).__init__()
        self.rule = None

    def __eq__(self, other):
        if other == self.text():
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class OutputDialogLocal(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(OutputDialogLocal, self).__init__(parent)
        self.ui = OutputDialog.Ui_OutputDialog()
        self.ui.setupUi(self)
        self.rules = None
        self.ui.lineEdit.textChanged.connect(self.validate_format)
        self.button_texts = []
        self.buttons = []
        self.signals = OutputDialogSigs()
        self.ui.scrollArea.verticalScrollBar().setEnabled(False)
        self._valid = True
        self.used_rules = []
        self.valid = True
        self.default_rules = [Rules.AllAttributes(), Rules.AllContents(), Rules.AllOfTag(), Rules.TagType()]

    def accept(self):
        self.signals.accepted.emit([self.ui.lineEdit.text(), self.get_used_rules()])
        super(OutputDialogLocal, self).accept()

    @property
    def valid(self):
        return self._valid

    @valid.setter
    def valid(self, value):
        self._valid = value
        self.ui.buttonBox.buttons()[0].setEnabled(self._valid)
        if self._valid:
            self.ui.lineEdit.setGraphicsEffect(None)
        else:
            shadow = QtWidgets.QGraphicsDropShadowEffect()
            shadow.setColor(QtGui.QColor(255, 0, 0))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.ui.lineEdit.setGraphicsEffect(shadow)
        self.signals.valid.emit(self._valid)

    def open_window(self, rules):
        self.setup(rules)
        self.open()

    def setup(self, rules):
        self.rules = rules
        self.delete_all_buttons()
        self.add_all_variable_buttons()
        self.validate_format()

    def add_all_variable_buttons(self):
        self.delete_all_buttons()
        self.buttons = []
        self.button_texts = []
        try:
            list_of_rules = self.get_all_constant_rules() + self.default_rules
        except TypeError:
            list_of_rules = self.default_rules
        for button in self.make_a_list_buttons_for_all_rules(list_of_rules):
            if button.text() not in self.button_texts:
                self.buttons.append(button)
                self.button_texts.append(button.text())
                self.ui.scrollWidget.layout().addWidget(button)

    def add_button_to_scroll_area(self, button):
        self.ui.scrollWidget.layout().addWidget(button)

    def get_all_constant_rules(self):
        self.take_out_all_false_rules()
        try:
            if len(self.rules) > 1:
                return list(set(self.rules[0]).intersection(*self.rules[1:])) + self.default_rules
            else:
                return self.rules[0] + self.default_rules
        except TypeError:
            return None

    def make_a_list_buttons_for_all_rules(self, rules):
        buttons = []
        for rule in rules:
            buttons.append(self.make_button_of_rule(rule))
        return buttons

    def take_out_all_false_rules(self):
            for or_set in self.rules:
                try:
                    for rule in or_set:
                        if not rule.kwargs['does']:
                            or_set.remove(rule)
                except TypeError:
                    continue

    def rule_button_clicked(self, button):
        index = self.ui.lineEdit.cursorPosition()
        o = self.ui.lineEdit.text()
        e = o[:index] + button.text() + o[index:]
        self.ui.lineEdit.setText(e)

    def make_button_of_rule(self, rule):
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        button = OutputRuleButton()
        button.rule = rule
        button.setText("[" + rule.values_saved[0] + "]")
        button.setSizePolicy(size_policy)
        button.clicked.connect(lambda: self.rule_button_clicked(button))
        return button

    def issubset_of_available_rules(self, rules):
        for rule in rules:
            if rule not in self.buttons:
                return False
        return True

    def get_used_rules_text(self):
        return re.findall('\[.*?\]', self.ui.lineEdit.text())

    def get_used_rules(self):
        used = []
        used_text = self.get_used_rules_text()
        for button in self.buttons:
            if button in used_text:
                used.append(button.rule)
        return used

    def validate_format(self):
        self.valid = self.is_valid()

    def is_valid(self):
        self.used_rules = self.get_used_rules_text()
        # edited_text = re.sub("[\[].*?[\]]", "test", text)
        return self.issubset_of_available_rules(self.used_rules)

    def delete_all_buttons(self):
        for button in self.buttons:
            button.deleteLater()
        self.button_texts = []


class OutputWidgetLocal(QtWidgets.QWidget):
    def __init__(self, number, parent=None):
        super(OutputWidgetLocal, self).__init__(parent=parent)
        self.signals = OutputDialogSigs()
        self.ui = OutputWidget.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.setStyleSheet("background-color: #E1E1E1;")
        self.ui.groupLabel.setText('Group ' + str(number))
        self.rules = None
        self.output = Output('', alls=None, attributes=None, contents=None)
        self.used_rules = []
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.id = number
        self.ui.replaceWithLabel.setTextFormat(QtCore.Qt.PlainText)
        self.dialog = OutputDialogLocal()
        self.dialog.signals.accepted.connect(self.receive_dialog_message)
        self.dialog.signals.valid.connect(lambda x: self.set_valid(x))
        self.ui.pushButton.clicked.connect(self.open_dialog)
        self.__valid = True
        self.valid = True

    def make_output(self, output_format):
        attributes_to_save, contents_to_save, tags, alls = Rules.get_separated_list_of_values_saved(self.used_rules)
        try:
            self.output = Output(output_format, alls=alls, attributes=attributes_to_save, contents=contents_to_save,
                                 tag_type=tags[0])
        except IndexError:
            self.output = Output(output_format, alls=alls, attributes=attributes_to_save, contents=contents_to_save)

    def receive_dialog_message(self, message):
        self.set_label(message[0])
        self.used_rules = message[1]
        self.make_output(message[0])

    def set_label(self, text):
        self.ui.replaceWithLabel.setText(text)

    def set_valid(self, value):
        self.valid = value

    @property
    def valid(self):
        return self.__valid

    @valid.setter
    def valid(self, value):
        if value:
            self.__valid = True
            self.setStyleSheet("background-color: #FFFFFF")
        else:
            self.__valid = False
            self.setStyleSheet("background-color: #FFBABA")

    def open_dialog(self):
        self.dialog.open_window(self.rules)

    def rules_changed(self, rules):
        print(rules)
        self.rules = rules
        self.dialog.setup(rules)
        self.dialog.validate_format()

    def rename(self, number):
        self.id = number
        self.ui.groupLabel.setText('Group ' + str(number))


class RuleDialogSigs(QtCore.QObject):
    result = QtCore.pyqtSignal(dict)


class RuleDialogLocal(QtWidgets.QDialog):
    def __init__(self):
        super(RuleDialogLocal, self).__init__()
        self.ui = AddRuleDialog.Ui_Dialog()
        self.ui.setupUi(self)
        self.rule_names = get_rule_names()
        self.rule = None
        self.rule_type = None
        self.setup_additional()
        self.signals = RuleDialogSigs()
        self.show()

    def accept(self):
        true_or_false = self.ui.trueOrFalseDropdown.currentText() == 'True'
        rule = self.rule_type(does=true_or_false, attribute_value=self.ui.keyLineEdit.text(),
                              condition=self.ui.valueLineEdit.text())
        self.signals.result.emit({'rule': rule, 'dialog': self})

        super(RuleDialogLocal, self).accept()

    def setup_additional(self):
        retain_size = QtWidgets.QSizePolicy()
        retain_size.setRetainSizeWhenHidden(True)
        self.ui.keyFrame.setSizePolicy(retain_size)
        self.ui.valueFrame.setSizePolicy(retain_size)
        self.ui.trueOrFalseFrame.setSizePolicy(retain_size)
        self.add_all_rules()
        self.ui.ruleTypeDropdown.addItem('OR')
        self.ui.ruleTypeDropdown.setItemData(self.ui.ruleTypeDropdown.count() - 1, Rules.Or)
        self.ui.ruleTypeDropdown.currentTextChanged.connect(self.on_rule_type_change)
        self.on_rule_type_change()
        self.ui.trueOrFalseDropdown.addItems(['True', "False"])
        self.ui.keyLineEdit.textChanged.connect(self.on_line_edit_value_change)
        self.ui.valueLineEdit.textChanged.connect(self.on_line_edit_value_change)

    def on_rule_type_change(self):
        self.rule_type = self.ui.ruleTypeDropdown.currentData()
        self.ui.valueFrame.setVisible(self.rule_type.needs_condition)
        self.ui.keyFrame.setVisible(self.rule_type.needs_attribute)
        self.ui.trueOrFalseFrame.setVisible(self.rule_type.needs_does)
        self.on_line_edit_value_change()

    @staticmethod
    def is_line_edit_filled(line_edit):
        if line_edit.parent().isHidden() or line_edit.text() != '':
            return True
        else:
            return False

    def on_line_edit_value_change(self):
        self.ui.buttons.buttons()[0].setEnabled(self.is_line_edit_filled(self.ui.valueLineEdit)
                                                and self.is_line_edit_filled(self.ui.keyLineEdit))

    @staticmethod
    def determine_if_value_should_be_shown(rule_type):
        try:
            rule_type_sig = signature(rule_type)
            if len(rule_type_sig.parameters) > 1:
                return True
            else:
                return False
        except TypeError:
            return False

    @staticmethod
    def determine_if_key_should_be_shown(rule_type):
        try:
            rule_type_sig = signature(rule_type)
            if len(rule_type_sig.parameters) > 2:
                return True
            else:
                return False
        except TypeError:
            return False

    @staticmethod
    def determine_if_true_or_false_should_be_shown(rule_type):
        name = rule_type.__name__
        print(name)
        if not name.lower() == 'or':
            return True
        else:
            return False

    def get_current_rule_type(self):
        return Rules.get_rule_from_string(self.ui.ruleTypeDropdown.currentData().toString())

    def add_all_rules(self):
        for subclass in Rules.Rule.__subclasses__():
            for rule in subclass.__subclasses__():
                self.ui.ruleTypeDropdown.addItem(get_name_with_spaces_and_tag(rule.__name__))
                self.ui.ruleTypeDropdown.setItemData(self.ui.ruleTypeDropdown.count() - 1, rule)


class RuleListSigs(QtCore.QObject):
    changed_rules = pyqtSignal()


class RuleWidgetLocal(QtWidgets.QWidget):
    def __init__(self, parent):
        super(RuleWidgetLocal, self).__init__()
        self.setSizePolicy(350, 24)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(parent)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ruleTypeDropdown = QtWidgets.QComboBox(parent)
        self.ruleTypeDropdown.setObjectName("ruleTypeDropdown")
        self.horizontalLayout_2.addWidget(self.ruleTypeDropdown)
        self.line = QtWidgets.QFrame(parent)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.conditionLineEdit = QtWidgets.QLineEdit(parent)
        self.conditionLineEdit.setObjectName("conditionLineEdit")
        self.horizontalLayout_2.addWidget(self.conditionLineEdit)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(2, 2)
        self.ruleTypeDropdown.show()
        self.line.show()
        self.conditionLineEdit.show()

    def sizeHint(self):
        return QtCore.QSize(350, 24)


class RuleResult(QtWidgets.QListWidgetItem):
    def __init__(self, value=''):
        super(RuleResult, self).__init__(value)
        self.rule = None
        self.rule_dialog = None


class TagToReplaceResult(QtWidgets.QListWidgetItem):
    def __init__(self):
        super(TagToReplaceResult, self).__init__()
        self.setFlags(self.flags() | QtCore.Qt.ItemIsEditable)
        self.letters = ''

    def setData(self, p_int, Any):
        new_any = Any
        letters = Any.replace('<', '')
        self.letters = letters.replace('>', '')
        if not str(new_any).startswith('<'):
            new_any = '<' + new_any
        if not str(new_any).endswith('>'):
            new_any = new_any + '>'
        super(TagToReplaceResult, self).setData(p_int, new_any)


class GroupResult(QtWidgets.QListWidgetItem):
    def __init__(self, number):
        super(GroupResult, self).__init__()
        self.id = number
        self.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont('MS Shell Dlg 2', 10)
        font.setBold(True)
        self.setFont(font)
        self.setText('Group ' + str(number))


class GroupListSignals(QtCore.QObject):
    removed_group = pyqtSignal(int)


class GroupListWidget(QtWidgets.QListWidget):
    def __init__(self):
        super(GroupListWidget, self).__init__()
        model = self.model()
        model.rowsMoved.connect(self.layout_changed)
        self.signals = GroupListSignals()

    def layout_changed(self, old_row_index, old_row_int_1, old_row_int_2, new_row_index, new_row_int):
        if new_row_int == 0:
            self.try_to_move_to_0()
        elif old_row_int_2 == 0:
            self.try_to_move_group_1(new_row_int - 1)

    def try_to_move_to_0(self):
        try:
            if not self.item(0).id == 1:
                item = self.takeItem(0)
                self.insertItem(1, item)
        except AttributeError:
            item = self.takeItem(0)
            self.insertItem(1, item)

    def try_to_move_group_1(self, row):
        try:
            if self.item(row).id == 1:
                item = self.takeItem(row)
                self.insertItem(0, item)
        except AttributeError:
            pass

    def get_all_values_from_group(self, g_int):
        within_group = False
        items = []
        for item_index in range(0, self.count()):
            item = self.item(item_index)
            try:
                if item.id == g_int:
                    within_group = True
                else:
                    within_group = False
            except AttributeError:
                if within_group:
                    items.append(item)
        return items

    def remove_item_from_list_widget(self):
        for item in self.selectedItems():
            if not isinstance(item, GroupResult):
                self.takeItem(self.row(item))
            else:
                self.signals.removed_group.emit(item.id)

    def remove_group_item(self, number):
        for index in range(0, self.count()):
            list_item = self.item(index)
            try:
                if list_item.id == number and list_item.id != 1:
                    self.takeItem(index)
            except AttributeError:
                pass

    def rename_group_list_items(self):
        for index in range(0, len(self.get_list_of_groups())):
            correct_id = index + 1
            item = self.get_list_of_groups()[index]
            if item.id != correct_id:
                item.id = correct_id
                item.setText("Group " + str(correct_id))

    def get_list_of_group_ids(self):
        group_ids = []
        for index in range(0, self.count()):
            list_item = self.item(index)
            try:
                group_ids.append(list_item.id)
            except AttributeError:
                pass
        return group_ids

    def add_group(self):
        list_item = GroupResult(len(self.get_list_of_groups()) + 1)
        self.addItem(list_item)

    def get_list_of_groups(self):
        groups = []
        for index in range(0, self.count()):
            list_item = self.item(index)
            if isinstance(list_item, GroupResult):
                groups.append(list_item)
        return groups


class TagsListWidget(GroupListWidget):
    def edit_tag_button_clicked(self):
        items = self.selectedItems()
        if len(items) == 1:
            self.editItem(items[0])

    def add_tag_button_clicked(self):
        list_item = TagToReplaceResult()
        self.addItem(list_item)
        index = self.row(list_item)
        self.editItem(self.item(index))

    def get_list_of_tags(self):
        tags = []
        for index in range(0, self.count()):
            try:
                tags.append(self.item(index).letters)
            except AttributeError:
                pass
        return tags

    def get_list_of_tags_from_group(self, g_int):
        tags = []
        tags_list = self.get_all_values_from_group(g_int)
        for tag in tags_list:
            tags.append(tag.letters)
        return tags


class RulesListWidget(GroupListWidget):
    def __init__(self):
        super(RulesListWidget, self).__init__()
        self.add_rule_dialog = None
        self.local_signals = RuleListSigs()
        self.valid = True

    @property
    def valid(self):
        return self.are_rules_valid()

    @valid.setter
    def valid(self, value):
        if value:
            self.setGraphicsEffect(None)
        else:
            shadow = QtWidgets.QGraphicsDropShadowEffect()
            shadow.setColor(QtGui.QColor(255, 0, 0))
            shadow.setOffset(0)
            shadow.setBlurRadius(10)
            self.setGraphicsEffect(shadow)

    def validate_rules(self):
        self.valid = self.are_rules_valid()

    def are_rules_valid(self):
        for g_int in range(len(self.get_list_of_groups())):
            for or_group in self.get_list_of_rules_from_group(g_int+1):
                count = 0
                for rule in or_group:
                    if isinstance(rule, Rules.TagIs):
                        count += 1
                if count > 1:
                    return False
        return True

    def add_group(self):
        super(RulesListWidget, self).add_group()
        self.local_signals.changed_rules.emit()

    def remove_group_item(self, number):
        super(RulesListWidget, self).remove_group_item(number)
        self.local_signals.changed_rules.emit()

    def remove_item_from_list_widget(self):
        super(RulesListWidget, self).remove_item_from_list_widget()
        self.local_signals.changed_rules.emit()

    def layout_changed(self, old_row_index, old_row_int_1, old_row_int_2, new_row_index, new_row_int):
        super(RulesListWidget, self).layout_changed(old_row_index, old_row_int_1, old_row_int_2,
                                                    new_row_index, new_row_int)
        self.local_signals.changed_rules.emit()
        self.validate_rules()

    def add_rule_button_clicked(self):
        self.add_rule_dialog = RuleDialogLocal()
        try:
            self.add_rule_dialog.signals.disconnect()
        except TypeError:
            pass
        self.add_rule_dialog.signals.result.connect(self.append_rule)
        self.add_rule_dialog.show()

    def append_rule(self, rule_dict):
        list_item = RuleResult(rule_dict['rule'].readable_string)
        list_item.rule = rule_dict['rule']
        list_item.rule_dialog = rule_dict['dialog']
        self.addItem(list_item)
        self.local_signals.changed_rules.emit()
        self.validate_rules()

    def edit_rule(self, rule_dict):
        self.remove_item_from_list_widget()
        self.append_rule(rule_dict)
        self.local_signals.changed_rules.emit()
        self.validate_rules()

    def edit_rule_button_clicked(self):
        if len(self.selectedItems()) == 1:
            item = self.selectedItems()[0]
            self.add_rule_dialog = self.item(self.row(item)).rule_dialog
            self.add_rule_dialog.signals.disconnect()
            self.add_rule_dialog.signals.result.connect(self.edit_rule)
            self.add_rule_dialog.show()

    def get_list_of_rules(self):
        rules = [[]]
        or_index = 0
        for index in range(0, self.count()):
            try:
                item = self.item(index).rule
            except AttributeError:
                continue
            if issubclass(type(item), Rules.Rule):
                rules[or_index].append(item)
            elif isinstance(item, Rules.Or):
                or_index += 1
                rules[or_index] = []
        return rules

    def get_list_of_rules_from_group(self, g_int):
        rules = [[]]
        or_index = 0
        rules_list = self.get_all_values_from_group(g_int)
        for rule in [rule.rule for rule in rules_list]:
            if issubclass(type(rule), Rules.Rule):
                rules[or_index].append(rule)
            elif isinstance(rule, Rules.Or):
                or_index += 1
                rules.append([])
        return rules


class OutputScrollAreaSigs(QtCore.QObject):
    # Needs Group ID
    output_button_clicked = pyqtSignal(int)


class OutputScrollArea(QtWidgets.QScrollArea):
    def __init__(self):
        super(OutputScrollArea, self).__init__()
        self.setStyleSheet(".QWidget {background-color: #ffffff;}")
        layout = QtWidgets.QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setAlignment(QtCore.Qt.AlignTop)
        self.signals = OutputScrollAreaSigs()
        self.local_widget = QtWidgets.QWidget()
        self.local_widget.setLayout(layout)
        self.local_widget.setMaximumWidth(self.width())
        self.setWidget(self.local_widget)
        self.setWidgetResizable(True)
        self.setMinimumHeight(100)

    @property
    def valid(self):
        for widget in self.get_list_of_groups():
            if not widget.valid:
                return False
        return True

    def add_group(self):
        output_widget = OutputWidgetLocal(self.local_widget.layout().count() + 1, parent=self)
        output_widget.signals.button_pushed.connect(output_widget.open_dialog)
        self.local_widget.layout().addWidget(output_widget)

    def remove_group_item(self, number):
        for widget in self.get_list_of_groups():
            try:
                if widget.id == number and not widget.id == 1:
                    self.local_widget.layout().takeAt(widget.id - 1)
                    widget.deleteLater()
            except AttributeError:
                pass

    def rename_group_list_items(self):
        for index in range(0, len(self.get_list_of_groups())):
            correct_id = index + 1
            item = self.get_list_of_groups()[index]
            try:
                if item.id != correct_id:
                    item.rename(correct_id)
            except AttributeError:
                pass

    def get_group_widget_at_index(self, g_int):
        for widget in self.get_list_of_groups():
            if widget.id == g_int:
                return widget

    def get_list_of_groups(self):
        groups = []
        for index in range(0, self.local_widget.layout().count()):
            item = self.local_widget.layout().itemAt(index).widget()
            if isinstance(item, OutputWidgetLocal):
                groups.append(item)
        return groups

    def get_dict_of_group_outputs(self):
        g_dict = {}
        for g in self.get_list_of_groups():
            g_dict[g.id] = g
        return g_dict

    def send_rules_to_outputs(self, group_list):
        for group_id in range(len(group_list)):
            for output in self.get_list_of_groups():
                if output.id == group_id + 1:
                    output.rules_changed(group_list[group_id])


def get_rule_names():
    rule_names = []
    for rule in Rules.Rule.__subclasses__():
        name = re.sub(r"(\w)([A-Z])", r"\1 \2", rule.__name__)
        rule_names.append(name)
    return rule_names


def get_name_with_spaces_and_tag(name):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", name)
