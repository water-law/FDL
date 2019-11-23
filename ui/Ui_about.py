# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './designer/about.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(454, 200)
        self.verticalLayout = QtWidgets.QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.mLogoLabel = QtWidgets.QLabel(AboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mLogoLabel.sizePolicy().hasHeightForWidth())
        self.mLogoLabel.setSizePolicy(sizePolicy)
        self.mLogoLabel.setObjectName("mLogoLabel")
        self.gridLayout.addWidget(self.mLogoLabel, 0, 0, 2, 1)
        self.mAppLabel = QtWidgets.QLabel(AboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mAppLabel.sizePolicy().hasHeightForWidth())
        self.mAppLabel.setSizePolicy(sizePolicy)
        self.mAppLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.mAppLabel.setAcceptDrops(False)
        self.mAppLabel.setTextFormat(QtCore.Qt.AutoText)
        self.mAppLabel.setObjectName("mAppLabel")
        self.gridLayout.addWidget(self.mAppLabel, 0, 1, 1, 1)
        self.mCopyrightLabel = QtWidgets.QLabel(AboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mCopyrightLabel.sizePolicy().hasHeightForWidth())
        self.mCopyrightLabel.setSizePolicy(sizePolicy)
        self.mCopyrightLabel.setWordWrap(True)
        self.mCopyrightLabel.setObjectName("mCopyrightLabel")
        self.gridLayout.addWidget(self.mCopyrightLabel, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.mClosePushButton = QtWidgets.QPushButton(AboutDialog)
        self.mClosePushButton.setObjectName("mClosePushButton")
        self.horizontalLayout.addWidget(self.mClosePushButton)
        spacerItem1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(AboutDialog)
        self.mClosePushButton.clicked.connect(AboutDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About FDL"))
        self.mLogoLabel.setText(_translate("AboutDialog", "TextLabel"))
        self.mAppLabel.setText(_translate("AboutDialog", "About FDL"))
        self.mCopyrightLabel.setText(_translate("AboutDialog", "版本 0.0.1\n"
"FDL is a downloader for quick download files.\n"
"\n"
"Copyright (C) 2019 Water Law."))
        self.mClosePushButton.setText(_translate("AboutDialog", "Close"))

