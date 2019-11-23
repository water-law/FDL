# -*- coding:utf-8 -*-
import os
import logging
import threading
import time
import pickle
import requests
from urllib.parse import urlparse
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QDialog, QMessageBox
from PyQt5.QtGui import QValidator
from PyQt5.QtCore import QProcess
from ui.Ui_fdldialog import Ui_MainWindow
from form.frmUrlLinkDialog import UrlLinkDialog
from form.frmChangeLanguageDialog import ChangeLanguageDialog, ChangeLanguage2Dialog
from form.frmHelp import AboutDialog

logger = logging.getLogger(__name__)


class DownloadThread(threading.Thread):

    def __init__(self, url, startpos, endpos, f):
        super(DownloadThread, self).__init__()
        self.url = url
        self.startpos = startpos
        self.endpos = endpos
        self.fd = f

    def download(self):
        startTime = time.time()
        headers = {"Range": "bytes={}-{}".format(self.startpos, self.endpos)}
        print(headers)
        res = requests.get(self.url, headers=headers)
        self.fd.seek(self.startpos)
        self.fd.write(res.content)
        print("done:{}-{}， spend {}".format(self.startpos, self.endpos, int(time.time() - startTime)))

    def run(self):
        self.download()


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

    # noinspection PyPep8Naming
    def showNewTaskDialog(self):
        content = QApplication.clipboard().text()
        dialog = UrlLinkDialog(self)

        pos = 0
        if dialog.urlValidator.validate(content, pos)[0] == QValidator.Acceptable:
            dialog.mLinkComboBox.setEditText(content)

        if dialog.exec_() == QDialog.Accepted:
            link_input = dialog.mLinkComboBox.currentText()
            if dialog.urlValidator.validate(link_input, pos)[0] == QValidator.Acceptable:
                url = link_input
            else:
                box = QMessageBox(dialog)
                box.resize(400, 200)
                box.setWindowTitle("URL 格式不正确")
                box.setText(link_input)
                if box.exec_() == QDialog.Accepted:
                    box.close()
                else:
                    return
                # QMessageBox.warning(dialog, "URL 格式不正确", link_input)
            try:
                response = requests.head(url)
            except Exception as e:
                logger.critical(msg="请求 %s 失败: %s" % (url, str(e)))
                return
            response.raise_for_status()
            print(response.headers)
            fileSize = int(response.headers.get("Content-Length", 0))
            print(fileSize)
            fileName = urlparse(url).path.split('/')[-1]
            threadnum = 8
            threading.BoundedSemaphore(threadnum)
            tempf = open(fileName, "w")  # 清空文件
            tempf.close()
            start = 0
            end = -1
            step = fileSize // threadnum
            mtd_list = []
            with open(fileName, "rb+") as f:
                fileno = f.fileno()
                while end < fileSize - 1:
                    start = end + 1
                    end = start + step - 1
                    if end > fileSize:
                        end = fileSize
                    print("download: {}-{}".format(start, end))
                    # 复制文件句柄
                    dup = os.dup(fileno)
                    # 打开文件
                    fd = os.fdopen(dup, 'rb+', -1)
                    t = DownloadThread(url, start, end, fd)
                    t.start()
                    mtd_list.append(t)
            for i in mtd_list:
                i.join()

    def onUseEnglishDialog(self):
        dialog = ChangeLanguageDialog(self)
        try:
            data = pickle.load(open("data", "rb"))
        except EOFError:
            mData = {"currLanguage": "en_US", "nextLanguage": "en_US"}
        else:
            mData = {"currLanguage": data["currLanguage"], "nextLanguage": "en_US"}
        pickle.dump(mData, open("data", "wb"))
        if dialog.exec() == QDialog.Accepted:
            qApp.closeAllWindows()
            QProcess.startDetached(qApp.applicationFilePath(), [])
        else:
            dialog.close()

    def onUseChineseDialog(self):
        dialog = ChangeLanguage2Dialog(self)
        try:
            data = pickle.load(open("data", "rb"))
        except EOFError:
            mData = {"currLanguage": "en_US", "nextLanguage": "en_US"}
        else:
            mData = {"currLanguage": data["currLanguage"], "nextLanguage": "zh_CN"}
        pickle.dump(mData, open("data", "wb"))
        if dialog.exec() == QDialog.Accepted:
            qApp.closeAllWindows()
            QProcess.startDetached(qApp.applicationFilePath(), [])
        else:
            dialog.close()

    def onAbout(self):
        dialog = AboutDialog(self)
        if dialog.exec() == QDialog.Accepted:
            dialog.close()
