# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './designer/downloaddialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DownloadDialog(object):
    def setupUi(self, DownloadDialog):
        DownloadDialog.setObjectName("DownloadDialog")
        DownloadDialog.resize(699, 407)
        DownloadDialog.setWindowTitle("Dialog")
        self.tabWidget = QtWidgets.QTabWidget(DownloadDialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 651, 221))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(-5, -9, 651, 211))
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setGridSize(QtCore.QSize(0, 0))
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.mProgressBar = QtWidgets.QProgressBar(DownloadDialog)
        self.mProgressBar.setGeometry(QtCore.QRect(10, 270, 651, 23))
        self.mProgressBar.setMaximum(0)
        self.mProgressBar.setProperty("value", 0)
        self.mProgressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.mProgressBar.setTextVisible(True)
        self.mProgressBar.setObjectName("mProgressBar")
        self.tableWidget = QtWidgets.QTableWidget(DownloadDialog)
        self.tableWidget.setGeometry(QtCore.QRect(15, 361, 651, 201))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.layoutWidget = QtWidgets.QWidget(DownloadDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 311, 651, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(438, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.mStopPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.mStopPushButton.setObjectName("mStopPushButton")
        self.horizontalLayout.addWidget(self.mStopPushButton)
        self.mCancelPushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.mCancelPushButton.setObjectName("mCancelPushButton")
        self.horizontalLayout.addWidget(self.mCancelPushButton)

        self.retranslateUi(DownloadDialog)
        self.tabWidget.setCurrentIndex(0)
        self.listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(DownloadDialog)

    def retranslateUi(self, DownloadDialog):
        _translate = QtCore.QCoreApplication.translate
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("DownloadDialog", "Download Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DownloadDialog", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("DownloadDialog", "Tab 3"))
        self.mProgressBar.setFormat(_translate("DownloadDialog", "%v/%m"))
        self.mStopPushButton.setText(_translate("DownloadDialog", "Stop"))
        self.mCancelPushButton.setText(_translate("DownloadDialog", "Cancel"))

