# -*- coding:utf-8 -*-
from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QRegExpValidator
from ui.Ui_urlLinkDialog import Ui_UrlLinkDialog


class UrlLinkDialog(QDialog, Ui_UrlLinkDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        rx = QRegExp(r"^https?://.*")
        self.mUrlValidator = QRegExpValidator(rx, self)
        self.mLinkComboBox.setValidator(self.mUrlValidator)
