# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Wed Oct 19 21:35:26 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(398, 300)
        Dialog.setAutoFillBackground(True)
        self.login = QtGui.QPushButton(Dialog)
        self.login.setGeometry(QtCore.QRect(150, 210, 96, 26))
        self.login.setObjectName(_fromUtf8("login"))
        self.unametextbox = QtGui.QPlainTextEdit(Dialog)
        self.unametextbox.setGeometry(QtCore.QRect(140, 60, 171, 31))
        self.unametextbox.setObjectName(_fromUtf8("unametextbox"))
        self.passtextbox = QtGui.QPlainTextEdit(Dialog)
        self.passtextbox.setGeometry(QtCore.QRect(140, 120, 171, 31))
        self.passtextbox.setObjectName(_fromUtf8("passtextbox"))
        self.usernamelabel = QtGui.QLabel(Dialog)
        self.usernamelabel.setGeometry(QtCore.QRect(30, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.usernamelabel.setFont(font)
        self.usernamelabel.setTextFormat(QtCore.Qt.RichText)
        self.usernamelabel.setObjectName(_fromUtf8("usernamelabel"))
        self.passwordlabel = QtGui.QLabel(Dialog)
        self.passwordlabel.setGeometry(QtCore.QRect(30, 130, 91, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.passwordlabel.setFont(font)
        self.passwordlabel.setObjectName(_fromUtf8("passwordlabel"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.login.setText(_translate("Dialog", "Login", None))
        self.usernamelabel.setText(_translate("Dialog", "Username", None))
        self.passwordlabel.setText(_translate("Dialog", "Password", None))

