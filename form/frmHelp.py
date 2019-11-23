# -*- coding:utf-8 -*-
import os
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from ui.Ui_about import Ui_AboutDialog


class AboutDialog(QDialog, Ui_AboutDialog):

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        image = QImage()
        path = os.path.join(os.getcwd(), 'FDL.png')
        image.load(path)
        self.mLogoLabel.setPixmap(QPixmap.fromImage(image.scaled(150, 150, Qt.KeepAspectRatio)))
