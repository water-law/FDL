# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './designer/downloadFileInfoDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DownloadFIleInfoDialog(object):
    def setupUi(self, DownloadFIleInfoDialog):
        DownloadFIleInfoDialog.setObjectName("DownloadFIleInfoDialog")
        DownloadFIleInfoDialog.resize(569, 166)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DownloadFIleInfoDialog.sizePolicy().hasHeightForWidth())
        DownloadFIleInfoDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(DownloadFIleInfoDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.mUrlLabel = QtWidgets.QLabel(DownloadFIleInfoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mUrlLabel.sizePolicy().hasHeightForWidth())
        self.mUrlLabel.setSizePolicy(sizePolicy)
        self.mUrlLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mUrlLabel.setObjectName("mUrlLabel")
        self.gridLayout.addWidget(self.mUrlLabel, 0, 0, 1, 1)
        self.mUrlLineEdit = QtWidgets.QLineEdit(DownloadFIleInfoDialog)
        self.mUrlLineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(13)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mUrlLineEdit.sizePolicy().hasHeightForWidth())
        self.mUrlLineEdit.setSizePolicy(sizePolicy)
        self.mUrlLineEdit.setObjectName("mUrlLineEdit")
        self.gridLayout.addWidget(self.mUrlLineEdit, 0, 1, 1, 1)
        self.mCategoryLabel = QtWidgets.QLabel(DownloadFIleInfoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mCategoryLabel.sizePolicy().hasHeightForWidth())
        self.mCategoryLabel.setSizePolicy(sizePolicy)
        self.mCategoryLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mCategoryLabel.setObjectName("mCategoryLabel")
        self.gridLayout.addWidget(self.mCategoryLabel, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mCateoryComboBox = QtWidgets.QComboBox(DownloadFIleInfoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mCateoryComboBox.sizePolicy().hasHeightForWidth())
        self.mCateoryComboBox.setSizePolicy(sizePolicy)
        self.mCateoryComboBox.setAcceptDrops(False)
        self.mCateoryComboBox.setEditable(True)
        self.mCateoryComboBox.setObjectName("mCateoryComboBox")
        self.horizontalLayout_2.addWidget(self.mCateoryComboBox)
        self.pushButton_5 = QtWidgets.QPushButton(DownloadFIleInfoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(30, 20))
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        spacerItem = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.mLogoLabel = QtWidgets.QLabel(DownloadFIleInfoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mLogoLabel.sizePolicy().hasHeightForWidth())
        self.mLogoLabel.setSizePolicy(sizePolicy)
        self.mLogoLabel.setObjectName("mLogoLabel")
        self.gridLayout.addWidget(self.mLogoLabel, 1, 2, 2, 1)
        self.mSaveAsLabel = QtWidgets.QLabel(DownloadFIleInfoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mSaveAsLabel.sizePolicy().hasHeightForWidth())
        self.mSaveAsLabel.setSizePolicy(sizePolicy)
        self.mSaveAsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mSaveAsLabel.setObjectName("mSaveAsLabel")
        self.gridLayout.addWidget(self.mSaveAsLabel, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mSaveLineEdit = QtWidgets.QLineEdit(DownloadFIleInfoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mSaveLineEdit.sizePolicy().hasHeightForWidth())
        self.mSaveLineEdit.setSizePolicy(sizePolicy)
        self.mSaveLineEdit.setObjectName("mSaveLineEdit")
        self.horizontalLayout_3.addWidget(self.mSaveLineEdit)
        self.mFilePushButton = QtWidgets.QPushButton(DownloadFIleInfoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mFilePushButton.sizePolicy().hasHeightForWidth())
        self.mFilePushButton.setSizePolicy(sizePolicy)
        self.mFilePushButton.setMinimumSize(QtCore.QSize(30, 20))
        self.mFilePushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.mFilePushButton.setObjectName("mFilePushButton")
        self.horizontalLayout_3.addWidget(self.mFilePushButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.mDescLabel = QtWidgets.QLabel(DownloadFIleInfoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mDescLabel.sizePolicy().hasHeightForWidth())
        self.mDescLabel.setSizePolicy(sizePolicy)
        self.mDescLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mDescLabel.setObjectName("mDescLabel")
        self.gridLayout.addWidget(self.mDescLabel, 3, 0, 1, 1)
        self.mDescLineEdit = QtWidgets.QLineEdit(DownloadFIleInfoDialog)
        self.mDescLineEdit.setObjectName("mDescLineEdit")
        self.gridLayout.addWidget(self.mDescLineEdit, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(28, 17, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mLaterDownloadPushButton = QtWidgets.QPushButton(DownloadFIleInfoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mLaterDownloadPushButton.sizePolicy().hasHeightForWidth())
        self.mLaterDownloadPushButton.setSizePolicy(sizePolicy)
        self.mLaterDownloadPushButton.setObjectName("mLaterDownloadPushButton")
        self.horizontalLayout.addWidget(self.mLaterDownloadPushButton)
        self.mStartDownloadPushButton = QtWidgets.QPushButton(DownloadFIleInfoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mStartDownloadPushButton.sizePolicy().hasHeightForWidth())
        self.mStartDownloadPushButton.setSizePolicy(sizePolicy)
        self.mStartDownloadPushButton.setObjectName("mStartDownloadPushButton")
        self.horizontalLayout.addWidget(self.mStartDownloadPushButton)
        self.mCancelPushButton = QtWidgets.QPushButton(DownloadFIleInfoDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mCancelPushButton.sizePolicy().hasHeightForWidth())
        self.mCancelPushButton.setSizePolicy(sizePolicy)
        self.mCancelPushButton.setObjectName("mCancelPushButton")
        self.horizontalLayout.addWidget(self.mCancelPushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(DownloadFIleInfoDialog)
        self.mCancelPushButton.clicked.connect(DownloadFIleInfoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DownloadFIleInfoDialog)

    def retranslateUi(self, DownloadFIleInfoDialog):
        _translate = QtCore.QCoreApplication.translate
        DownloadFIleInfoDialog.setWindowTitle(_translate("DownloadFIleInfoDialog", "Download FIle Info"))
        self.mUrlLabel.setText(_translate("DownloadFIleInfoDialog", "URL"))
        self.mCategoryLabel.setText(_translate("DownloadFIleInfoDialog", "Category"))
        self.pushButton_5.setText(_translate("DownloadFIleInfoDialog", "+"))
        self.mLogoLabel.setText(_translate("DownloadFIleInfoDialog", "TextLabel"))
        self.mSaveAsLabel.setText(_translate("DownloadFIleInfoDialog", "Save As"))
        self.mFilePushButton.setText(_translate("DownloadFIleInfoDialog", "..."))
        self.mDescLabel.setText(_translate("DownloadFIleInfoDialog", "Desc"))
        self.mLaterDownloadPushButton.setText(_translate("DownloadFIleInfoDialog", "Download Later"))
        self.mStartDownloadPushButton.setText(_translate("DownloadFIleInfoDialog", "StartDownload"))
        self.mCancelPushButton.setText(_translate("DownloadFIleInfoDialog", "Cancel"))
