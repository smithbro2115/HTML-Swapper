from PyQt5 import QtCore, QtGui, QtWidgets
import YoutubeEmbedToLinkGui
import converter
import pyperclip
import TextColor


class Gui(YoutubeEmbedToLinkGui.Ui_MainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.converter = converter.Converter()
        self.copied_label_animation = None
        self.fade_effect = None
        self.fade_animation = None
        self.unfade_effect = None
        self.unfade_animation = None

    def setup_ui_additional(self):
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Gui()
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    ui.setup_ui_additional()
    MainWindow.show()
    sys.exit(app.exec_())
