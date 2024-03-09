# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1200, 800)
        font = QFont()
        font.setFamilies([u"Nirmala UI Semilight"])
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"background-color:rgb(241, 208, 215);")
        self.gmail = QLabel(Dialog)
        self.gmail.setObjectName(u"gmail")
        self.gmail.setGeometry(QRect(440, 240, 71, 31))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(11)
        self.gmail.setFont(font1)
        self.gmail.setStyleSheet(u"background-color: None")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(490, 80, 191, 61))
        font2 = QFont()
        font2.setPointSize(27)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: None;")
        self.gmail_input = QLineEdit(Dialog)
        self.gmail_input.setObjectName(u"gmail_input")
        self.gmail_input.setGeometry(QRect(510, 230, 261, 41))
        self.gmail_input.setStyleSheet(u"background-color: rgb(234, 234, 234)")
        self.gmail_2 = QLabel(Dialog)
        self.gmail_2.setObjectName(u"gmail_2")
        self.gmail_2.setGeometry(QRect(400, 330, 141, 31))
        self.gmail_2.setFont(font1)
        self.gmail_2.setStyleSheet(u"background-color: None")
        self.graphicsView = QGraphicsView(Dialog)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(380, 150, 410, 490))
        self.graphicsView.setStyleSheet(u"border-radius: 20px; background-color: white;")
        self.register_btn = QPushButton(Dialog)
        self.register_btn.setObjectName(u"register_btn")
        self.register_btn.setGeometry(QRect(480, 520, 211, 41))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(14)
        self.register_btn.setFont(font3)
        self.register_btn.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(180, 235, 255)")
        self.password_input = QLineEdit(Dialog)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(510, 320, 261, 41))
        self.password_input.setStyleSheet(u"background-color: rgb(234, 234, 234)")
        self.login_btn = QPushButton(Dialog)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(480, 450, 211, 41))
        self.login_btn.setFont(font3)
        self.login_btn.setStyleSheet(u"border-radius: 20px;\n"
"background-color:rgb(241, 208, 215);")
        self.error_txt = QLabel(Dialog)
        self.error_txt.setObjectName(u"error_txt")
        self.error_txt.setGeometry(QRect(440, 400, 291, 21))
        self.error_txt.setStyleSheet(u"background-color: None; Color: Red;")
        self.graphicsView.raise_()
        self.gmail.raise_()
        self.label.raise_()
        self.gmail_input.raise_()
        self.gmail_2.raise_()
        self.register_btn.raise_()
        self.password_input.raise_()
        self.login_btn.raise_()
        self.error_txt.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.gmail.setText(QCoreApplication.translate("Dialog", u"Gmail: ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"CURATE", None))
        self.gmail_2.setText(QCoreApplication.translate("Dialog", u"password:", None))
        self.register_btn.setText(QCoreApplication.translate("Dialog", u"Register", None))
        self.login_btn.setText(QCoreApplication.translate("Dialog", u"login", None))
        self.error_txt.setText("")
    # retranslateUi

