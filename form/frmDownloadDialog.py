# -*- coding: utf-8 -*-
import os
import sys
import time
import traceback
import logging
import threading
import requests
from PyQt5.QtCore import QThread, QObject, pyqtSlot, pyqtSignal, QMutex, QThreadPool, QRunnable
from PyQt5.QtWidgets import QDialog
from ui.Ui_downloaddialog import Ui_DownloadDialog

logger = logging.getLogger(__name__)


# noinspection PyPep8Naming
class DownloadDialog(QDialog, Ui_DownloadDialog):
    def __init__(self, url, filePath, threadno, totalSize, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(os.path.split(filePath)[1])
        self.url = url
        self.filePath = filePath
        self.threadno = threadno
        self.totalSize = totalSize
        self.downloadTask = None
        self.workerThread = QThread(self)
        self.workerThread.started.connect(self.notifyStarted)
        self.workerThread.finished.connect(self.notifyFinished)
        self.mStopPushButton.clicked.connect(self.stopProcess)
        self.mCancelPushButton.clicked.connect(self.cancelProcess)
        self.toggleDownloadTask()

    @pyqtSlot(int)
    def setProgress(self, v):
        self.mProgressBar.setValue(v)
        if v == self.totalSize:
            self.workerThread.quit()
            self.workerThread.wait()

    def toggleDownloadTask(self):
        self.mProgressBar.setMaximum(self.totalSize)
        self.downloadTask = DownloadTask(self.url, self.filePath, self.totalSize, self.threadno)
        self.downloadTask.progressed.connect(self.setProgress)
        self.workerThread.started.connect(self.downloadTask.startDownload)
        self.workerThread.finished.connect(self.downloadTask.deleteLater)
        self.downloadTask.moveToThread(self.workerThread)
        self.workerThread.start()

    @pyqtSlot()
    def stopProcess(self):
        logger.info("stop task of downloading {} finished.".format(self.url))
        if self.workerThread.isRunning():
            self.workerThread.terminate()
            self.workerThread.wait()
            self.mStopPushButton.setText("Start")
        else:
            self.mStopPushButton.setText("Stop")

    @pyqtSlot()
    def cancelProcess(self):
        logger.info("cancel task of downloading {} finished.".format(self.url))
        if self.workerThread.isRunning():
            self.workerThread.terminate()
            self.workerThread.wait()

    @pyqtSlot()
    def notifyStarted(self):
        pass

    @pyqtSlot()
    def notifyFinished(self):
        logger.info("finished download {}".format(self.url))


# noinspection PyPep8Naming
class DownloadTask(QObject):
    progressed = pyqtSignal(int)

    def __init__(self, url, filePath, totalSize, threadno):
        super().__init__()
        self.url = url
        self.filePath = filePath
        self.totalSize = totalSize
        self.threadno = threadno
        self.threadpool = QThreadPool()
        self.processing = 0  # 进度
        self.mutex_lock = QMutex()

    @pyqtSlot()
    def startDownload(self):
        logger.info("start download {}".format(self.url))
        threadsInfoList = self.splitFileToNPic(self.totalSize, self.threadno)
        threadList = []
        f = open(self.filePath, "rb+")
        fileno = f.fileno()
        # for i, item in enumerate(threadsInfoList, 1):
        #     logger.info(str(i)+str(item))
        #     dup = os.dup(fileno)  # 复制文件句柄
        #     fd = os.fdopen(dup, 'rb+', -1)  # 打开文件
        #     t = DownloadThread(self.url, item[0], item[1], fd)
        #     t.start()
        #     threadList.append(t)
        # for x in threadList:
        #     x.join()
        # f.close()
        # self.progressed.emit(self.totalSize)

        for i, item in enumerate(threadsInfoList, 1):
            dup = os.dup(fileno)  # 复制文件句柄
            fd = os.fdopen(dup, 'rb+', -1)  # 打开文件
            worker = Worker(self.executeThisFn, i, self.url, item[0], item[1], fd)
            worker.signals.result.connect(self.printOutput)
            worker.signals.finished.connect(self.threadComplete)
            worker.signals.progress.connect(self.progressFn)
            self.threadpool.start(worker)
        f.close()

    @staticmethod
    def executeThisFn(threadNo, url, startpos, endpos, fd, progress_callback):
        # FIXME: 更为细的读 nio 优化
        headers = {"Range": "bytes={}-{}".format(startpos, endpos)}
        logger.info("GET {}".format(headers))
        res = requests.get(url, headers=headers)
        fd.seek(startpos)
        fd.write(res.content)
        progress_callback.emit(endpos - startpos + 1)
        return "Thread {} Done.".format(threadNo)

    @pyqtSlot(object)
    def printOutput(self, s):
        print(s)

    @pyqtSlot()
    def threadComplete(self):
        pass

    @pyqtSlot(int)
    def progressFn(self, n):
        self.mutex_lock.lock()
        self.processing += n
        self.progressed.emit(self.processing)
        self.mutex_lock.unlock()

    @staticmethod
    def splitFileToNPic(fileSize, n):
        groups = []
        start = 0
        end = -1
        step = fileSize // n
        while end < fileSize - 1:
            start = end + 1
            end = start + step - 1
            if end > fileSize:
                end = fileSize
            groups.append((start, end))
        return groups


class DownloadThread(threading.Thread):

    def __init__(self, url, startpos, endpos, fd):
        super().__init__()
        self.url = url
        self.startpos = startpos
        self.endpos = endpos
        self.fd = fd

    def run(self):
        startTime = time.time()
        headers = {"Range": "bytes={}-{}".format(self.startpos, self.endpos)}
        logger.info(headers)
        res = requests.get(self.url, headers=headers)
        self.fd.seek(self.startpos)
        self.fd.write(res.content)
        logger.info("done:{}-{}， spend {}".format(self.startpos, self.endpos, int(time.time() - startTime)))


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done