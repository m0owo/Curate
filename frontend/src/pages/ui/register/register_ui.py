# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGraphicsView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1200, 800)
        Dialog.setStyleSheet(u"background-color:rgb(241, 208, 215);")
        self.gmail = QLabel(Dialog)
        self.gmail.setObjectName(u"gmail")
        self.gmail.setGeometry(QRect(430, 250, 71, 31))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(11)
        self.gmail.setFont(font)
        self.gmail.setStyleSheet(u"background-color: None")
        self.password_input = QLineEdit(Dialog)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(500, 400, 261, 41))
        self.password_input.setStyleSheet(u"background-color: rgb(234, 234, 234)")
        self.gmail_3 = QLabel(Dialog)
        self.gmail_3.setObjectName(u"gmail_3")
        self.gmail_3.setGeometry(QRect(400, 400, 141, 31))
        self.gmail_3.setFont(font)
        self.gmail_3.setStyleSheet(u"background-color: None")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 170, 181, 61))
        font1 = QFont()
        font1.setPointSize(21)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: None;")
        self.new_gmail_input = QLineEdit(Dialog)
        self.new_gmail_input.setObjectName(u"new_gmail_input")
        self.new_gmail_input.setGeometry(QRect(500, 240, 261, 41))
        self.new_gmail_input.setStyleSheet(u"background-color: rgb(234, 234, 234)")
        self.consent_cb = QCheckBox(Dialog)
        self.consent_cb.setObjectName(u"consent_cb")
        self.consent_cb.setGeometry(QRect(450, 550, 261, 20))
        font2 = QFont()
        font2.setPointSize(8)
        self.consent_cb.setFont(font2)
        self.consent_cb.setStyleSheet(u"background-color: None;\n"
"")
        self.gmail_2 = QLabel(Dialog)
        self.gmail_2.setObjectName(u"gmail_2")
        self.gmail_2.setGeometry(QRect(390, 330, 141, 31))
        self.gmail_2.setFont(font)
        self.gmail_2.setStyleSheet(u"background-color: None")
        self.gmail_4 = QLabel(Dialog)
        self.gmail_4.setObjectName(u"gmail_4")
        self.gmail_4.setGeometry(QRect(380, 480, 241, 31))
        self.gmail_4.setFont(font)
        self.gmail_4.setStyleSheet(u"background-color: None")
        self.graphicsView = QGraphicsView(Dialog)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(370, 150, 410, 490))
        self.graphicsView.setStyleSheet(u"border-radius: 20px; background-color: white;")
        self.reconfirm_input = QLineEdit(Dialog)
        self.reconfirm_input.setObjectName(u"reconfirm_input")
        self.reconfirm_input.setGeometry(QRect(500, 490, 261, 41))
        self.reconfirm_input.setStyleSheet(u"background-color: rgb(234, 234, 234)")
        self.register_btn = QPushButton(Dialog)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setGeometry(QRect(470, 590, 211, 41))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(14)
        self.register_btn.setFont(font3)
        self.register_btn.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(180, 235, 255)")
        self.gmail_5 = QLabel(Dialog)
        self.gmail_5.setObjectName(u"gmail_5")
        self.gmail_5.setGeometry(QRect(380, 500, 251, 31))
        self.gmail_5.setFont(font)
        self.gmail_5.setStyleSheet(u"background-color: None")
        self.username_input = QLineEdit(Dialog)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setGeometry(QRect(500, 320, 261, 41))
        self.username_input.setStyleSheet(u"background-color: rgb(234, 234, 234)")
        self.graphicsView.raise_()
        self.gmail.raise_()
        self.password_input.raise_()
        self.gmail_3.raise_()
        self.label.raise_()
        self.new_gmail_input.raise_()
        self.consent_cb.raise_()
        self.gmail_2.raise_()
        self.gmail_4.raise_()
        self.reconfirm_input.raise_()
        self.register_btn.raise_()
        self.gmail_5.raise_()
        self.username_input.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.gmail.setText(QCoreApplication.translate("Dialog", u"Gmail: ", None))
        self.gmail_3.setText(QCoreApplication.translate("Dialog", u"Password: ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"REGISTER", None))
        self.consent_cb.setText(QCoreApplication.translate("Dialog", u"Recieve our news and update via email", None))
        self.gmail_2.setText(QCoreApplication.translate("Dialog", u"Username:", None))
        self.gmail_4.setText(QCoreApplication.translate("Dialog", u"Re-confirm: ", None))
        self.register_btn.setText(QCoreApplication.translate("Dialog", u"Register", None))
        self.gmail_5.setText(QCoreApplication.translate("Dialog", u"password", None))
    # retranslateUi

