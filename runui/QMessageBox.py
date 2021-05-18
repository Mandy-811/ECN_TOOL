# —*-  coding:utf-8  -*-
"""
作者：mandy.meng
日期：2021年01月18日
QMessageBox:
1.关于对话框
2.错误对话框
3.警告对话框
4.提问疑问对话框
5.消息对话框
有2点差异
1：显示对话框的图标不一样
2：对话框显示的按钮是不一样的
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ecn import ECN


class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.initui()
        self.ecn = ECN()

    def initui(self):
        self.setWindowTitle("QMessageBox案例")
        self.resize(300, 400)

        layout = QVBoxLayout()
        self.button1 = QPushButton()
        self.button1.setText('显示关于对话框')
        self.button1.clicked.connect(self.showDialog)
        layout.addWidget(self.button1)
        self.setLayout(layout)

        self.button2 = QPushButton()
        self.button2.setText("显示消息对话框")
        self.button2.clicked.connect(self.showDialog)
        layout.addWidget(self.button2)

        self.button3 = QPushButton()
        self.button3.setText("显示警告对话框")
        self.button3.clicked.connect(self.showDialog)
        layout.addWidget(self.button3)

        self.button4 = QPushButton()
        self.button4.setText("显示错误对话框")
        self.button4.clicked.connect(self.showDialog)
        layout.addWidget(self.button4)

        self.button5 = QPushButton()
        self.button5.setText("显示提问对话框")
        self.button5.clicked.connect(self.showDialog)
        layout.addWidget(self.button5)

    def showDialog(self):
        text = self.sender().text()
        print(text)
        if text == "显示关于对话框":
            self.ecn.pushButton_openbom.setEnabled(False)
            self.ecn.lineEdit_bompath.setEnabled(False)
            self.ecn.show()

        elif text == "显示消息对话框":
            self.ecn.pushButton_openrecord.setEnabled(False)
            self.ecn.lineEdit_recordpath.setEnabled(False)
            self.ecn.show()

        # elif text == "显示警告对话框":
        #     QMessageBox.warning(self, '警告', '这是一个警告对话框', QMessageBox.Yes | QMessageBox.No,
        #                                     QMessageBox.Yes)
        # elif text == "显示错误对话框":
        #     QMessageBox.critical(self, '错误', '这是一个错误对话框', QMessageBox.Yes | QMessageBox.No,
        #                                     QMessageBox.Yes)
        # elif text == "显示提问对话框":
        #     QMessageBox.question(self, '提问', '这是一个提问对话框', QMessageBox.Yes | QMessageBox.No,
        #                                     QMessageBox.Yes)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMessageBoxDemo()
    win.show()
    sys.exit(app.exec_())