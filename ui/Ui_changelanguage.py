# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './designer/changelanguage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChangeLanguageDialog(object):
    def setupUi(self, ChangeLanguageDialog):
        ChangeLanguageDialog.setObjectName("ChangeLanguageDialog")
        ChangeLanguageDialog.resize(473, 175)
        ChangeLanguageDialog.setStyleSheet("Dialog {border-images: url( E:/Projects/FDL/favicon.png)}")
        self.verticalLayout = QtWidgets.QVBoxLayout(ChangeLanguageDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.mTipLabel = QtWidgets.QLabel(ChangeLanguageDialog)
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
        spacerItem = QtWidgets.QSpacerItem(290, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.mSavePushButton = QtWidgets.QPushButton(ChangeLanguageDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mSavePushButton.sizePolicy().hasHeightForWidth())
        self.mSavePushButton.setSizePolicy(sizePolicy)
        self.mSavePushButton.setMinimumSize(QtCore.QSize(88, 29))
        self.mSavePushButton.setMaximumSize(QtCore.QSize(88, 29))
        self.mSavePushButton.setObjectName("mSavePushButton")
        self.horizontalLayout.addWidget(self.mSavePushButton)
        self.mCacelPushButton = QtWidgets.QPushButton(ChangeLanguageDialog)
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

        self.retranslateUi(ChangeLanguageDialog)
        self.mSavePushButton.clicked.connect(ChangeLanguageDialog.accept)
        self.mCacelPushButton.clicked.connect(ChangeLanguageDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ChangeLanguageDialog)

    def retranslateUi(self, ChangeLanguageDialog):
        _translate = QtCore.QCoreApplication.translate
        ChangeLanguageDialog.setWindowTitle(_translate("ChangeLanguageDialog", "FDL - PyQt5 Downloader"))
        self.mTipLabel.setText(_translate("ChangeLanguageDialog", "  The language changes on the main dialog will apply only after only after restart FDL.\n"
"  Do you wish to restart FDL now?"))
        self.mSavePushButton.setText(_translate("ChangeLanguageDialog", "是"))
        self.mCacelPushButton.setText(_translate("ChangeLanguageDialog", "否"))

