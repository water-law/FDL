# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QDialog
from ui.Ui_changelanguage import Ui_ChangeLanguageDialog
from ui.Ui_changelanguage2 import Ui_ChangeLanguage2Dialog


class ChangeLanguageDialog(QDialog, Ui_ChangeLanguageDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class ChangeLanguage2Dialog(QDialog, Ui_ChangeLanguage2Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
