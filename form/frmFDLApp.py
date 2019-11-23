# -*- coding:utf-8 -*-
import os
import logging
from urllib.parse import urlparse
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QDialog, QMessageBox
from PyQt5.QtGui import QValidator
from PyQt5.QtCore import QProcess
from ui.Ui_fdldialog import Ui_MainWindow
from form.frmUrlLinkDialog import UrlLinkDialog
from form.frmChangeLanguageDialog import ChangeLanguageDialog, ChangeLanguage2Dialog
from form.frmDownloadFileInfoDialog import DownloadFileInfoDialog
from form.frmDownloadDialog import DownloadDialog
from form.frmHelp import AboutDialog
from utils.Constants import getConfValue, setConfValue

logger = logging.getLogger(__name__)


# noinspection PyPep8Naming
class FDLApp(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Task Menu Action
        self.mAddNewTaskAction.triggered.connect(self.showNewTaskDialog)
        self.mExitAction.triggered.connect(qApp.exit)

        # Setting Menu Action
        self.mEnglishAction.triggered.connect(self.onUseEnglishDialog)
        self.mChineseAction.triggered.connect(self.onUseChineseDialog)

        # Help Menu Action
        self.mAboutAction.triggered.connect(self.onAbout)

    def showNewTaskDialog(self):
        content = QApplication.clipboard().text()
        dialog = UrlLinkDialog(self)

        pos = 0
        if dialog.mUrlValidator.validate(content, pos)[0] == QValidator.Acceptable:
            dialog.mLinkComboBox.setEditText(content)

        if dialog.exec() == QDialog.Accepted:
            link_input = dialog.mLinkComboBox.currentText()
            if dialog.mUrlValidator.validate(link_input, pos)[0] == QValidator.Acceptable:
                url = link_input
                downloadFileInfoDialog = DownloadFileInfoDialog(self)
                downloadFileInfoDialog.mUrlLineEdit.setText(url)
                fileName = urlparse(url).path.split('/')[-1]
                filePath = os.path.join(os.getcwd(), fileName)
                downloadFileInfoDialog.mSaveLineEdit.setText(filePath)
                downloadFileInfoDialog.mStartDownloadPushButton.clicked.connect(self.showDownload)
                downloadFileInfoDialog.show()
            else:
                box = QMessageBox(dialog)
                box.resize(400, 200)
                box.setWindowTitle("URL 格式不正确")
                box.setText(link_input)
                if box.exec() == QDialog.Accepted:
                    box.close()
                else:
                    return

    def showDownload(self):
        sender = self.sender()
        fileInfoDialog = sender.parent()
        url = fileInfoDialog.mUrlLineEdit.text()
        filePath = fileInfoDialog.mSaveLineEdit.text()
        fileInfoDialog.deleteLater()
        fileDir = os.path.split(filePath)[0]
        if not os.path.exists(fileDir):
            os.mkdir(fileDir)
        tempf = open(filePath, "w")  # 清空文件
        tempf.close()
        threadno = getConfValue("ThreadNo")
        response = requests.head(url)
        totalSize = int(response.headers.get("Content-Length", 0))
        if totalSize <= 0:
            return
        threadno = 1 if totalSize < 1000000 else threadno
        downloadDialog = DownloadDialog(url, filePath, threadno, totalSize, self)
        downloadDialog.show()

    def onUseEnglishDialog(self):
        dialog = ChangeLanguageDialog(self)
        setConfValue("Lang", "en_US")
        if dialog.exec() == QDialog.Accepted:
            qApp.closeAllWindows()
            QProcess.startDetached(qApp.applicationFilePath(), [])
        else:
            dialog.close()

    def onUseChineseDialog(self):
        dialog = ChangeLanguage2Dialog(self)
        setConfValue("Lang", "zh_CN")
        if dialog.exec() == QDialog.Accepted:
            qApp.closeAllWindows()
            QProcess.startDetached(qApp.applicationFilePath(), [])
        else:
            dialog.close()

    def onAbout(self):
        dialog = AboutDialog(self)
        if dialog.exec() == QDialog.Accepted:
            dialog.close()
