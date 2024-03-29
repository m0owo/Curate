# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFrame,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)
import icons_rc
import logo_rc
import logo_rc

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
        self.info_button.setStyleSheet(u" background-color: rgb(88,130,126)")
        self.address_button = QPushButton(self.profile_frame)
        self.address_button.setObjectName(u"address_button")
        self.address_button.setGeometry(QRect(50, 130, 171, 51))
        self.address_button.setFont(font1)
        self.address_button.setLayoutDirection(Qt.LeftToRight)
        self.address_button.setStyleSheet(u"border-color: black")
        self.editinfo_frame = QFrame(self.header)
        self.editinfo_frame.setObjectName(u"editinfo_frame")
        self.editinfo_frame.setGeometry(QRect(330, 100, 701, 601))
        self.editinfo_frame.setStyleSheet(u"background-color: rgb(232,243,242); border-radius: 20px;")
        self.editinfo_frame.setFrameShape(QFrame.StyledPanel)
        self.editinfo_frame.setFrameShadow(QFrame.Raised)
        self.page_label_5 = QLabel(self.editinfo_frame)
        self.page_label_5.setObjectName(u"page_label_5")
        self.page_label_5.setGeometry(QRect(30, 20, 231, 41))
        self.page_label_5.setFont(font1)
        self.page_label_5.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(self.editinfo_frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(80, 100, 160, 381))
        self.vertical = QVBoxLayout(self.verticalLayoutWidget)
        self.vertical.setObjectName(u"vertical")
        self.vertical.setContentsMargins(0, 0, 0, 0)
        self.name_label = QLabel(self.verticalLayoutWidget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setFont(font1)
        self.name_label.setAlignment(Qt.AlignCenter)

        self.vertical.addWidget(self.name_label, 0, Qt.AlignLeft)

        self.gmail_label = QLabel(self.verticalLayoutWidget)
        self.gmail_label.setObjectName(u"gmail_label")
        self.gmail_label.setFont(font1)
        self.gmail_label.setAlignment(Qt.AlignCenter)

        self.vertical.addWidget(self.gmail_label, 0, Qt.AlignLeft)

        self.phone_label = QLabel(self.verticalLayoutWidget)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setFont(font1)
        self.phone_label.setAlignment(Qt.AlignCenter)

        self.vertical.addWidget(self.phone_label, 0, Qt.AlignLeft)

        self.gender_label = QLabel(self.verticalLayoutWidget)
        self.gender_label.setObjectName(u"gender_label")
        self.gender_label.setFont(font1)
        self.gender_label.setAlignment(Qt.AlignCenter)

        self.vertical.addWidget(self.gender_label, 0, Qt.AlignLeft)

        self.birth_label = QLabel(self.verticalLayoutWidget)
        self.birth_label.setObjectName(u"birth_label")
        self.birth_label.setFont(font1)
        self.birth_label.setAlignment(Qt.AlignCenter)

        self.vertical.addWidget(self.birth_label, 0, Qt.AlignLeft)

        self.name_edit = QTextEdit(self.editinfo_frame)
        self.name_edit.setObjectName(u"name_edit")
        self.name_edit.setGeometry(QRect(240, 120, 340, 30))
        self.name_edit.setStyleSheet(u"background-color: white; border-radius: 40px;")
        self.mail_edit = QTextEdit(self.editinfo_frame)
        self.mail_edit.setObjectName(u"mail_edit")
        self.mail_edit.setGeometry(QRect(240, 200, 340, 30))
        self.mail_edit.setStyleSheet(u"background-color: white")
        self.phonenum_edit = QTextEdit(self.editinfo_frame)
        self.phonenum_edit.setObjectName(u"phonenum_edit")
        self.phonenum_edit.setGeometry(QRect(240, 280, 340, 30))
        self.phonenum_edit.setStyleSheet(u"background-color: white")
        self.male_botton = QRadioButton(self.editinfo_frame)
        self.male_botton.setObjectName(u"male_botton")
        self.male_botton.setGeometry(QRect(250, 360, 121, 22))
        font3 = QFont()
        font3.setFamilies([u"Manrope"])
        self.male_botton.setFont(font3)
        self.male_botton_2 = QRadioButton(self.editinfo_frame)
        self.male_botton_2.setObjectName(u"male_botton_2")
        self.male_botton_2.setGeometry(QRect(330, 360, 185, 22))
        self.male_botton_2.setFont(font3)
        self.male_botton_3 = QRadioButton(self.editinfo_frame)
        self.male_botton_3.setObjectName(u"male_botton_3")
        self.male_botton_3.setGeometry(QRect(420, 360, 377, 22))
        self.male_botton_3.setFont(font3)
        self.dateEdit = QDateEdit(self.editinfo_frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(250, 440, 101, 21))
        self.save_button = QPushButton(self.editinfo_frame)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(280, 510, 171, 51))
        self.save_button.setFont(font1)
        self.save_button.setLayoutDirection(Qt.RightToLeft)
        self.save_button.setStyleSheet(u"background-color: rgb(88,130,126)")
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
        self.page_label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt;\">My infomation</span></p></body></html>", None))
        self.name_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Name</span></p></body></html>", None))
        self.gmail_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Gmail</span></p></body></html>", None))
        self.phone_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Phone number</span></p></body></html>", None))
        self.gender_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Gender</span></p></body></html>", None))
        self.birth_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Birth</span></p></body></html>", None))
        self.male_botton.setText(QCoreApplication.translate("Dialog", u"Male", None))
        self.male_botton_2.setText(QCoreApplication.translate("Dialog", u"Female", None))
        self.male_botton_3.setText(QCoreApplication.translate("Dialog", u"Others", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Save", None))
    # retranslateUi

