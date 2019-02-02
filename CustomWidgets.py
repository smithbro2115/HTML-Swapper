from PyQt5 import QtWidgets, QtCore, QtGui
import re
import Rules
import AddRuleDialog
from inspect import signature
import RuleWidgetTwoValues
import TagToReplaceWidget


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
        try:
            rule = self.rule_type(true_or_false, self.ui.keyLineEdit.text(), self.ui.valueLineEdit.text())
            self.signals.result.emit({'rule': rule, 'dialog': self})
        except TypeError:
            try:
                rule = self.rule_type(true_or_false, self.ui.valueLineEdit.text())
                self.signals.result.emit({'rule': rule, 'dialog': self})
            except TypeError:
                rule = self.rule_type(true_or_false)
                self.signals.result.emit({'rule': rule, 'dialog': self})

        super(RuleDialogLocal, self).accept()

    def setup_additional(self):
        retain_size = QtWidgets.QSizePolicy()
        retain_size.setRetainSizeWhenHidden(True)
        self.ui.keyFrame.setSizePolicy(retain_size)
        self.ui.valueFrame.setSizePolicy(retain_size)
        self.ui.ruleTypeDropdown.addItems(self.rule_names)
        self.ui.ruleTypeDropdown.currentTextChanged.connect(self.on_rule_type_change)
        self.on_rule_type_change(self.ui.ruleTypeDropdown.currentText())
        self.ui.trueOrFalseDropdown.addItems(['True', "False"])
        self.ui.keyLineEdit.textChanged.connect(self.on_line_edit_value_change)
        self.ui.valueLineEdit.textChanged.connect(self.on_line_edit_value_change)

    def on_rule_type_change(self, text):
        rule_type_name = text[4:]
        self.rule_type = Rules.get_rule_from_string(rule_type_name)
        self.ui.valueFrame.setVisible(self.determine_if_value_should_be_shown(self.rule_type))
        self.ui.keyFrame.setVisible(self.determine_if_key_should_be_shown(self.rule_type))
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
        rule_type_sig = signature(rule_type)
        if len(rule_type_sig.parameters) > 1:
            return True
        else:
            return False

    @staticmethod
    def determine_if_key_should_be_shown(rule_type):
        rule_type_sig = signature(rule_type)
        if len(rule_type_sig.parameters) > 2:
            return True
        else:
            return False

    def get_current_rule_type(self):
        return Rules.get_rule_from_string(self.ui.ruleTypeDropdown.currentData().toString())


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


class GroupListWidget(QtWidgets.QListWidget):
    def __init__(self):
        super(GroupListWidget, self).__init__()
        model = self.model()
        model.rowsMoved.connect(self.layout_changed)

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


def get_rule_names():
    rule_names = []
    for rule in Rules.Rule.__subclasses__():
        name = 'Tag ' + re.sub(r"(\w)([A-Z])", r"\1 \2", rule.__name__)
        rule_names.append(name)
    return rule_names
