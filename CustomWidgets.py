from PyQt5 import QtWidgets, QtCore, QtGui
import re
import Rules
import RuleWidget
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


def get_rule_names():
    rule_names = []
    for rule in Rules.Rule.__subclasses__():
        rule_names.append(re.sub(r"(\w)([A-Z])", r"\1 \2", rule.__class__.__name__))
    return rule_names
