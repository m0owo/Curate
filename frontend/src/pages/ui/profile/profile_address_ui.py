# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_address.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)
from .icons_rc import *
from .logo_rc import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1200, 800)
        self.header = QWidget(Dialog)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(70, 20, 1080, 720))
        self.header.setMaximumSize(QSize(1080, 720))
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        self.header.setFont(font)
        self.header.setStyleSheet(u"")
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(120, 10, 921, 71))
        self.frame.setStyleSheet(u"QFrame#search_frame{\n"
"    background-color: #FFFBF3;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#filter_button{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton :hover{\n"
"    background-color: #E8F3F2;\n"
"}\n"
"\n"
"QTextEdit#search_edit{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QLabel#page_label{\n"
"    background-color: #E8F3F2;\n"
"    border-radius: 10px;\n"
"    border: solid;\n"
"    border-width: 1px;\n"
"    border-color:rgb(154, 152, 148)\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.home_button = QPushButton(self.frame)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setGeometry(QRect(740, 20, 41, 30))
        font1 = QFont()
        font1.setFamilies([u"Manrope"])
        font1.setBold(True)
        self.home_button.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icon_images/home_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon)
        self.home_button.setIconSize(QSize(20, 20))
        self.history_button = QPushButton(self.frame)
        self.history_button.setObjectName(u"history_button")
        self.history_button.setGeometry(QRect(780, 20, 41, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icon_images/history_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.history_button.setIcon(icon1)
        self.history_button.setIconSize(QSize(20, 20))
        self.wishlist_button = QPushButton(self.frame)
        self.wishlist_button.setObjectName(u"wishlist_button")
        self.wishlist_button.setGeometry(QRect(820, 20, 41, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icon_images/wishlist_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.wishlist_button.setIcon(icon2)
        self.wishlist_button.setIconSize(QSize(20, 20))
        self.profile_button = QPushButton(self.frame)
        self.profile_button.setObjectName(u"profile_button")
        self.profile_button.setGeometry(QRect(860, 20, 41, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icon_images/profile_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_button.setIcon(icon3)
        self.profile_button.setIconSize(QSize(20, 20))
        self.page_label = QLabel(self.frame)
        self.page_label.setObjectName(u"page_label")
        self.page_label.setGeometry(QRect(30, 20, 71, 30))
        self.page_label.setFont(font1)
        self.page_label.setAlignment(Qt.AlignCenter)
        self.page_label_2 = QLabel(self.frame)
        self.page_label_2.setObjectName(u"page_label_2")
        self.page_label_2.setGeometry(QRect(580, 20, 71, 30))
        self.page_label_2.setFont(font1)
        self.page_label_2.setAlignment(Qt.AlignCenter)
        self.page_label_3 = QLabel(self.frame)
        self.page_label_3.setObjectName(u"page_label_3")
        self.page_label_3.setGeometry(QRect(650, 20, 71, 30))
        self.page_label_3.setFont(font1)
        self.page_label_3.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 10, 120, 71))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.curate_label = QLabel(self.frame_2)
        self.curate_label.setObjectName(u"curate_label")
        self.curate_label.setGeometry(QRect(-10, -10, 161, 91))
        font2 = QFont()
        font2.setFamilies([u"Mogena"])
        font2.setPointSize(18)
        self.curate_label.setFont(font2)
        self.curate_label.setPixmap(QPixmap(u":/logos/curatelogo.png"))
        self.curate_label.setScaledContents(True)
        self.curate_label.setAlignment(Qt.AlignCenter)
        self.profile_frame = QFrame(self.header)
        self.profile_frame.setObjectName(u"profile_frame")
        self.profile_frame.setGeometry(QRect(50, 100, 271, 601))
        self.profile_frame.setStyleSheet(u"border-radius: 20px;")
        self.profile_frame.setFrameShape(QFrame.StyledPanel)
        self.profile_frame.setFrameShadow(QFrame.Raised)
        self.page_label_4 = QLabel(self.profile_frame)
        self.page_label_4.setObjectName(u"page_label_4")
        self.page_label_4.setGeometry(QRect(20, 20, 141, 41))
        self.page_label_4.setFont(font1)
        self.page_label_4.setAlignment(Qt.AlignCenter)
        self.info_button = QPushButton(self.profile_frame)
        self.info_button.setObjectName(u"info_button")
        self.info_button.setGeometry(QRect(50, 70, 171, 51))
        self.info_button.setFont(font1)
        self.info_button.setLayoutDirection(Qt.RightToLeft)
        self.info_button.setStyleSheet(u"")
        self.address_button = QPushButton(self.profile_frame)
        self.address_button.setObjectName(u"address_button")
        self.address_button.setGeometry(QRect(50, 130, 171, 51))
        self.address_button.setFont(font1)
        self.address_button.setLayoutDirection(Qt.LeftToRight)
        self.address_button.setStyleSheet(u" background-color: rgb(88,130,126)")
        self.editinfo_frame = QFrame(self.header)
        self.editinfo_frame.setObjectName(u"editinfo_frame")
        self.editinfo_frame.setGeometry(QRect(330, 100, 701, 601))
        self.editinfo_frame.setStyleSheet(u"background-color: rgb(232,243,242); border-radius: 20px;")
        self.editinfo_frame.setFrameShape(QFrame.StyledPanel)
        self.editinfo_frame.setFrameShadow(QFrame.Raised)
        self.page_label_5 = QLabel(self.editinfo_frame)
        self.page_label_5.setObjectName(u"page_label_5")
        self.page_label_5.setGeometry(QRect(40, 20, 141, 41))
        self.page_label_5.setFont(font1)
        self.page_label_5.setAlignment(Qt.AlignCenter)
        self.page_label_6 = QLabel(self.editinfo_frame)
        self.page_label_6.setObjectName(u"page_label_6")
        self.page_label_6.setGeometry(QRect(50, 90, 101, 41))
        self.page_label_6.setFont(font1)
        self.page_label_6.setAlignment(Qt.AlignCenter)
        self.add_address_button = QPushButton(self.editinfo_frame)
        self.add_address_button.setObjectName(u"add_address_button")
        self.add_address_button.setGeometry(QRect(450, 90, 171, 51))
        font3 = QFont()
        font3.setFamilies([u"Manrope"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.add_address_button.setFont(font3)
        self.add_address_button.setLayoutDirection(Qt.RightToLeft)
        self.add_address_button.setStyleSheet(u" background-color: rgb(88,130,126); color:white;")
        self.frame_3 = QFrame(self.editinfo_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(50, 170, 591, 421))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame_3)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 531, 80))
        self.page_label_7 = QLabel(self.widget)
        self.page_label_7.setObjectName(u"page_label_7")
        self.page_label_7.setGeometry(QRect(20, 10, 211, 41))
        font4 = QFont()
        font4.setFamilies([u"Manrope"])
        font4.setPointSize(8)
        font4.setBold(True)
        self.page_label_7.setFont(font4)
        self.page_label_7.setAlignment(Qt.AlignCenter)
        self.page_label_8 = QLabel(self.widget)
        self.page_label_8.setObjectName(u"page_label_8")
        self.page_label_8.setGeometry(QRect(10, 40, 371, 41))
        self.page_label_8.setFont(font4)
        self.page_label_8.setAlignment(Qt.AlignCenter)
        self.editinfo_frame.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.profile_frame.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.home_button.setText("")
        self.history_button.setText("")
        self.wishlist_button.setText("")
        self.profile_button.setText("")
        self.page_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Profile</p></body></html>", None))
        self.page_label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Follower</span></p></body></html>", None))
        self.page_label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Following</span></p></body></html>", None))
        self.curate_label.setText("")
        self.page_label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">My Account</span></p></body></html>", None))
        self.info_button.setText(QCoreApplication.translate("Dialog", u"My infomation", None))
        self.address_button.setText(QCoreApplication.translate("Dialog", u"Address", None))
        self.page_label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt;\">Address</span></p></body></html>", None))
        self.page_label_6.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">My address</span></p></body></html>", None))
        self.add_address_button.setText(QCoreApplication.translate("Dialog", u"+Add address", None))
        self.page_label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Moomoo Iceland +66  123456789</p></body></html>", None))
        self.page_label_8.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:400;\">123 Skycastle Soi Disney Road Disney , Disneyland, 12345</span></p></body></html>", None))
    # retranslateUi

