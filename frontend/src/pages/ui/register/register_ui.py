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
from PySide6.QtWidgets import (QApplication, QDialog, QGraphicsView, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1200, 800)
        font = QFont()
        font.setFamilies([u"Manrope"])
        font.setBold(True)
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"background-color:rgb(241, 208, 215);")
        self.gmail_lable = QLabel(Dialog)
        self.gmail_lable.setObjectName(u"gmail_lable")
        self.gmail_lable.setGeometry(QRect(440, 180, 71, 31))
        font1 = QFont()
        font1.setFamilies([u"Manrope"])
        font1.setPointSize(9)
        font1.setBold(True)
        self.gmail_lable.setFont(font1)
        self.gmail_lable.setStyleSheet(u"background-color: None")
        self.password_input = QLineEdit(Dialog)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(440, 370, 261, 41))
        self.password_input.setStyleSheet(u"background-color: rgb(234, 234, 234)")
        self.password_label = QLabel(Dialog)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(440, 340, 141, 31))
        self.password_label.setFont(font1)
        self.password_label.setStyleSheet(u"background-color: None")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(490, 100, 181, 61))
        font2 = QFont()
        font2.setFamilies([u"Manrope"])
        font2.setPointSize(22)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: None; color: white;")
        self.gmail_input = QLineEdit(Dialog)
        self.gmail_input.setObjectName(u"gmail_input")
        self.gmail_input.setGeometry(QRect(440, 210, 261, 41))
        self.gmail_input.setStyleSheet(u"background-color: rgb(234, 234, 234)")
        self.username_label = QLabel(Dialog)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(440, 260, 141, 31))
        self.username_label.setFont(font1)
        self.username_label.setStyleSheet(u"background-color: None")
        self.reconfirm_label = QLabel(Dialog)
        self.reconfirm_label.setObjectName(u"reconfirm_label")
        self.reconfirm_label.setGeometry(QRect(440, 420, 241, 31))
        self.reconfirm_label.setFont(font1)
        self.reconfirm_label.setStyleSheet(u"background-color: None")
        self.graphicsView = QGraphicsView(Dialog)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(370, 150, 410, 490))
        self.graphicsView.setStyleSheet(u"border-radius: 20px; background-color: white;")
        self.reconfirm_input = QLineEdit(Dialog)
        self.reconfirm_input.setObjectName(u"reconfirm_input")
        self.reconfirm_input.setGeometry(QRect(440, 450, 261, 41))
        self.reconfirm_input.setStyleSheet(u"background-color: rgb(234, 234, 234)")
        self.register_button = QPushButton(Dialog)
        self.register_button.setObjectName(u"register_button")
        self.register_button.setGeometry(QRect(450, 560, 231, 41))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(14)
        self.register_button.setFont(font3)
        self.register_button.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(180, 235, 255)")
        self.username_input = QLineEdit(Dialog)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setGeometry(QRect(440, 290, 261, 41))
        self.username_input.setStyleSheet(u"background-color: rgb(234, 234, 234)")
        self.buyer_button = QRadioButton(Dialog)
        self.buyer_button.setObjectName(u"buyer_button")
        self.buyer_button.setGeometry(QRect(420, 520, 141, 21))
        font4 = QFont()
        font4.setFamilies([u"Manrope"])
        font4.setBold(False)
        self.buyer_button.setFont(font4)
        self.buyer_button.setStyleSheet(u"background-color: None;")
        self.seller_button = QRadioButton(Dialog)
        self.seller_button.setObjectName(u"seller_button")
        self.seller_button.setGeometry(QRect(570, 520, 151, 21))
        font5 = QFont()
        font5.setFamilies([u"Manrope"])
        self.seller_button.setFont(font5)
        self.seller_button.setStyleSheet(u"background-color: None;")
        self.noti_label = QLabel(Dialog)
        self.noti_label.setObjectName(u"noti_label")
        self.noti_label.setGeometry(QRect(440, 490, 331, 31))
        self.noti_label.setFont(font1)
        self.noti_label.setStyleSheet(u"background-color: None")
        self.graphicsView.raise_()
        self.gmail_lable.raise_()
        self.password_input.raise_()
        self.password_label.raise_()
        self.label.raise_()
        self.gmail_input.raise_()
        self.username_label.raise_()
        self.reconfirm_label.raise_()
        self.reconfirm_input.raise_()
        self.register_button.raise_()
        self.username_input.raise_()
        self.buyer_button.raise_()
        self.seller_button.raise_()
        self.noti_label.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.gmail_lable.setText(QCoreApplication.translate("Dialog", u"Gmail", None))
        self.password_label.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"REGISTER", None))
        self.username_label.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.reconfirm_label.setText(QCoreApplication.translate("Dialog", u"Re-confirm password", None))
        self.register_button.setText(QCoreApplication.translate("Dialog", u"Register", None))
        self.buyer_button.setText(QCoreApplication.translate("Dialog", u"Registere as buyer", None))
        self.seller_button.setText(QCoreApplication.translate("Dialog", u"Registere as seller", None))
        self.noti_label.setText(QCoreApplication.translate("Dialog", u"Password", None))
    # retranslateUi

