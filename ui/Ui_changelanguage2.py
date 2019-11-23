# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './designer/changelanguage2.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChangeLanguage2Dialog(object):
    def setupUi(self, ChangeLanguage2Dialog):
        ChangeLanguage2Dialog.setObjectName("ChangeLanguage2Dialog")
        ChangeLanguage2Dialog.resize(351, 142)
        ChangeLanguage2Dialog.setStyleSheet("Dialog {border-images: url( E:/Projects/FDL/favicon.png)}")
        self.verticalLayout = QtWidgets.QVBoxLayout(ChangeLanguage2Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.mTipLabel = QtWidgets.QLabel(ChangeLanguage2Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mTipLabel.sizePolicy().hasHeightForWidth())
        self.mTipLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(9)
        font.setKerning(True)
        self.mTipLabel.setFont(font)
        self.mTipLabel.setTabletTracking(False)
        self.mTipLabel.setAcceptDrops(False)
        self.mTipLabel.setAutoFillBackground(False)
        self.mTipLabel.setStyleSheet("QLabel {background-color: #fff}")
        self.mTipLabel.setInputMethodHints(QtCore.Qt.ImhNone)
        self.mTipLabel.setTextFormat(QtCore.Qt.AutoText)
        self.mTipLabel.setScaledContents(False)
        self.mTipLabel.setWordWrap(True)
        self.mTipLabel.setObjectName("mTipLabel")
        self.gridLayout.addWidget(self.mTipLabel, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(160, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.mSavePushButton = QtWidgets.QPushButton(ChangeLanguage2Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mSavePushButton.sizePolicy().hasHeightForWidth())
        self.mSavePushButton.setSizePolicy(sizePolicy)
        self.mSavePushButton.setMinimumSize(QtCore.QSize(88, 29))
        self.mSavePushButton.setMaximumSize(QtCore.QSize(88, 29))
        self.mSavePushButton.setObjectName("mSavePushButton")
        self.horizontalLayout.addWidget(self.mSavePushButton)
        self.mCacelPushButton = QtWidgets.QPushButton(ChangeLanguage2Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mCacelPushButton.sizePolicy().hasHeightForWidth())
        self.mCacelPushButton.setSizePolicy(sizePolicy)
        self.mCacelPushButton.setMinimumSize(QtCore.QSize(88, 29))
        self.mCacelPushButton.setMaximumSize(QtCore.QSize(88, 29))
        self.mCacelPushButton.setObjectName("mCacelPushButton")
        self.horizontalLayout.addWidget(self.mCacelPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(ChangeLanguage2Dialog)
        self.mSavePushButton.clicked.connect(ChangeLanguage2Dialog.accept)
        self.mCacelPushButton.clicked.connect(ChangeLanguage2Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ChangeLanguage2Dialog)

    def retranslateUi(self, ChangeLanguage2Dialog):
        _translate = QtCore.QCoreApplication.translate
        ChangeLanguage2Dialog.setWindowTitle(_translate("ChangeLanguage2Dialog", "FDL - PyQt5 Downloader"))
        self.mTipLabel.setText(_translate("ChangeLanguage2Dialog", "    界面语言将在 FDL 重启之后改变， 您希望现在重启 FDL 吗?"))
        self.mSavePushButton.setText(_translate("ChangeLanguage2Dialog", "是"))
        self.mCacelPushButton.setText(_translate("ChangeLanguage2Dialog", "否"))

