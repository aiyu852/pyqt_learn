# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(500, 400))
        Form.setMaximumSize(QSize(500, 400))
        icon = QIcon()
        icon.addFile(u"images/20210619023354_1.jpg", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 0, 311, 191))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setPixmap(QPixmap(u"images/20210614035147_1.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 200, 111, 31))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.edt_username = QLineEdit(Form)
        self.edt_username.setObjectName(u"edt_username")
        self.edt_username.setGeometry(QRect(80, 260, 113, 20))
        self.edt_password = QLineEdit(Form)
        self.edt_password.setObjectName(u"edt_password")
        self.edt_password.setGeometry(QRect(280, 260, 113, 20))
        self.edt_password.setEchoMode(QLineEdit.Password)
        self.btn_login = QPushButton(Form)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(200, 330, 75, 23))
        font1 = QFont()
        font1.setFamily(u"Times New Roman")
        self.btn_login.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Something", None))
        self.edt_username.setPlaceholderText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.edt_password.setPlaceholderText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.btn_login.setText(QCoreApplication.translate("Form", u"start", None))
    # retranslateUi

