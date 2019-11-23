# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './designer/urlLinkDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UrlLinkDialog(object):
    def setupUi(self, UrlLinkDialog):
        UrlLinkDialog.setObjectName("UrlLinkDialog")
        UrlLinkDialog.resize(546, 74)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UrlLinkDialog.sizePolicy().hasHeightForWidth())
        UrlLinkDialog.setSizePolicy(sizePolicy)
        self.layoutWidget = QtWidgets.QWidget(UrlLinkDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 523, 56))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.mAddressLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mAddressLabel.sizePolicy().hasHeightForWidth())
        self.mAddressLabel.setSizePolicy(sizePolicy)
        self.mAddressLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.mAddressLabel.setMaximumSize(QtCore.QSize(40, 16777215))
        self.mAddressLabel.setObjectName("mAddressLabel")
        self.gridLayout.addWidget(self.mAddressLabel, 0, 0, 1, 1)
        self.mLinkComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.mLinkComboBox.setEditable(True)
        self.mLinkComboBox.setObjectName("mLinkComboBox")
        self.gridLayout.addWidget(self.mLinkComboBox, 0, 1, 1, 1)
        self.mSavePushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mSavePushButton.sizePolicy().hasHeightForWidth())
        self.mSavePushButton.setSizePolicy(sizePolicy)
        self.mSavePushButton.setObjectName("mSavePushButton")
        self.gridLayout.addWidget(self.mSavePushButton, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(438, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.mCacelPushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mCacelPushButton.sizePolicy().hasHeightForWidth())
        self.mCacelPushButton.setSizePolicy(sizePolicy)
        self.mCacelPushButton.setObjectName("mCacelPushButton")
        self.horizontalLayout.addWidget(self.mCacelPushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 3)

        self.retranslateUi(UrlLinkDialog)
        self.mCacelPushButton.clicked.connect(UrlLinkDialog.close)
        self.mSavePushButton.clicked.connect(UrlLinkDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(UrlLinkDialog)

    def retranslateUi(self, UrlLinkDialog):
        _translate = QtCore.QCoreApplication.translate
        UrlLinkDialog.setWindowTitle(_translate("UrlLinkDialog", "Input Task Download Url"))
        self.mAddressLabel.setText(_translate("UrlLinkDialog", "URL"))
        self.mSavePushButton.setText(_translate("UrlLinkDialog", "OK"))
        self.mCacelPushButton.setText(_translate("UrlLinkDialog", "Cancel"))

