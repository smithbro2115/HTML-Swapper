from PyQt5 import QtCore, QtGui, QtWidgets
import YoutubeEmbedToLinkGui
import converter
import pyperclip
import TextColor
import CustomWidgets
import RuleWidget


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
        self.addRuleButton.clicked.connect(self.add_rule)

    def add_rule(self):
        self.add_rule_dialog = CustomWidgets.RuleDialogLocal()
        self.add_rule_dialog.signals.result.connect(print)
        self.add_rule_dialog.show()

    def text_slider_change(self, event, scroll_to_track):
        scroll_to_track.verticalScrollBar().setValue(event)

    def convert_local(self):
        edited, indexes = self.converter.convert(self.original.toPlainText())
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
