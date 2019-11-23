# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QDialog
from ui.Ui_downloadFileInfoDialog import Ui_DownloadFIleInfoDialog


class DownloadFileInfoDialog(QDialog, Ui_DownloadFIleInfoDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
