# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ECN.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ECN(object):
    # def __init__(self):
    #     self.pushButton_openbom = QtWidgets.QPushButton()
    #     self.lineEdit_bompath = QtWidgets.QLineEdit()
    #     self.pushButton_openrecord = QtWidgets.QPushButton()
    #     self.lineEdit_recordpath = QtWidgets.QLineEdit()


    def setupUi(self, ECN):
        ECN.setObjectName("ECN")
        ECN.resize(547, 305)
        ECN.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(ECN)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(ECN)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(20, 20, 40, 20)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_openbom = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_openbom.setObjectName("pushButton_openbom")
        self.gridLayout.addWidget(self.pushButton_openbom, 0, 0, 1, 1)
        self.lineEdit_bompath = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_bompath.setObjectName("lineEdit_bompath")
        self.gridLayout.addWidget(self.lineEdit_bompath, 0, 1, 1, 1)
        self.pushButton_openrecord = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_openrecord.setObjectName("pushButton_openrecord")
        self.gridLayout.addWidget(self.pushButton_openrecord, 1, 0, 1, 1)
        self.lineEdit_recordpath = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_recordpath.setObjectName("lineEdit_recordpath")
        self.gridLayout.addWidget(self.lineEdit_recordpath, 1, 1, 1, 1)
        self.pushButton_openECN = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_openECN.setObjectName("pushButton_openECN")
        self.gridLayout.addWidget(self.pushButton_openECN, 2, 0, 1, 1)
        self.lineEdit_ECNpath = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_ECNpath.setObjectName("lineEdit_ECNpath")
        self.gridLayout.addWidget(self.lineEdit_ECNpath, 2, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_start = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout.addWidget(self.pushButton_start)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(ECN)
        QtCore.QMetaObject.connectSlotsByName(ECN)

    def retranslateUi(self, ECN):
        _translate = QtCore.QCoreApplication.translate
        ECN.setWindowTitle(_translate("ECN", "Form"))
        self.pushButton_openbom.setText(_translate("ECN", "打开BOM"))
        self.pushButton_openrecord.setText(_translate("ECN", "打开变更记录"))
        self.pushButton_openECN.setText(_translate("ECN", "打开ECN表"))
        self.pushButton_start.setText(_translate("ECN", "开始"))

