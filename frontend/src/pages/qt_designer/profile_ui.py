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
    QTextEdit, QWidget)
import icons_rc
import logo_rc
import logo_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1200, 800)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: white; \n"
"	border: None;\n"
"}\n"
"QFrame{\n"
"	border: None;	\n"
"}\n"
"QLabel{\n"
"	color: black;\n"
"}\n"
"QPushButton{\n"
"	border: None\n"
"}")
        self.header = QWidget(Dialog)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(70, 20, 1080, 720))
        self.header.setMaximumSize(QSize(1080, 720))
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        self.header.setFont(font)
        self.header.setStyleSheet(u"background-color: white;")
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
        self.page_label_2.setStyleSheet(u"color: black;")
        self.page_label_2.setAlignment(Qt.AlignCenter)
        self.page_label_3 = QLabel(self.frame)
        self.page_label_3.setObjectName(u"page_label_3")
        self.page_label_3.setGeometry(QRect(650, 20, 71, 30))
        self.page_label_3.setFont(font1)
        self.page_label_3.setStyleSheet(u"color: black;")
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
        self.profile_frame_2 = QFrame(self.header)
        self.profile_frame_2.setObjectName(u"profile_frame_2")
        self.profile_frame_2.setGeometry(QRect(50, 80, 1011, 631))
        self.profile_frame_2.setStyleSheet(u"")
        self.profile_frame_2.setFrameShape(QFrame.StyledPanel)
        self.profile_frame_2.setFrameShadow(QFrame.Raised)
        self.editinfo_frame = QFrame(self.profile_frame_2)
        self.editinfo_frame.setObjectName(u"editinfo_frame")
        self.editinfo_frame.setGeometry(QRect(290, 10, 701, 601))
        font3 = QFont()
        font3.setFamilies([u"Manrope"])
        font3.setPointSize(10)
        self.editinfo_frame.setFont(font3)
        self.editinfo_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(232,243,242);\n"
"	border-radius: 20px;\n"
"}\n"
"QVBoxLayout{\n"
"	background-color: rgb(232,243,242);\n"
"}\n"
"QPushButton{\n"
"	border-radius: 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QRadioButton{\n"
"	background-color: rgb(232,243,242);\n"
"}\n"
"\n"
"QTextEdit{\n"
"	color: black;\n"
"}\n"
"QTextLabel{\n"
"	background-color: None\n"
"}\n"
"QDateEdit {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    background-color: #f0f0f0;\n"
"    border-left: 1px solid #ccc;\n"
"}\n"
"\n"
"QDateEdit::down-arrow, QDateEdit::up-arrow {\n"
"    width: 20px;\n"
"    height: 20px; \n"
"    padding: 0px; \n"
"}")
        self.editinfo_frame.setFrameShape(QFrame.StyledPanel)
        self.editinfo_frame.setFrameShadow(QFrame.Raised)
        self.page_label_5 = QLabel(self.editinfo_frame)
        self.page_label_5.setObjectName(u"page_label_5")
        self.page_label_5.setGeometry(QRect(20, 20, 211, 41))
        self.page_label_5.setFont(font1)
        self.page_label_5.setStyleSheet(u"color: black;")
        self.page_label_5.setAlignment(Qt.AlignCenter)
        self.name_edit = QTextEdit(self.editinfo_frame)
        self.name_edit.setObjectName(u"name_edit")
        self.name_edit.setGeometry(QRect(240, 120, 341, 41))
        font4 = QFont()
        font4.setFamilies([u"Manrope"])
        font4.setBold(False)
        self.name_edit.setFont(font4)
        self.name_edit.setStyleSheet(u"background-color: white; border-radius: 40px;")
        self.mail_edit = QTextEdit(self.editinfo_frame)
        self.mail_edit.setObjectName(u"mail_edit")
        self.mail_edit.setGeometry(QRect(240, 200, 341, 41))
        font5 = QFont()
        font5.setFamilies([u"Manrope"])
        self.mail_edit.setFont(font5)
        self.mail_edit.setStyleSheet(u"background-color: white")
        self.phonenum_edit = QTextEdit(self.editinfo_frame)
        self.phonenum_edit.setObjectName(u"phonenum_edit")
        self.phonenum_edit.setGeometry(QRect(240, 280, 341, 41))
        self.phonenum_edit.setFont(font4)
        self.phonenum_edit.setStyleSheet(u"background-color: white")
        self.male_button = QRadioButton(self.editinfo_frame)
        self.male_button.setObjectName(u"male_button")
        self.male_button.setGeometry(QRect(250, 360, 121, 22))
        self.male_button.setFont(font3)
        self.male_button.setStyleSheet(u"color: black;")
        self.female_button = QRadioButton(self.editinfo_frame)
        self.female_button.setObjectName(u"female_button")
        self.female_button.setGeometry(QRect(330, 360, 185, 22))
        self.female_button.setFont(font3)
        self.female_button.setStyleSheet(u"color: black;")
        self.others_button = QRadioButton(self.editinfo_frame)
        self.others_button.setObjectName(u"others_button")
        self.others_button.setGeometry(QRect(430, 360, 91, 22))
        self.others_button.setFont(font3)
        self.date_edit = QDateEdit(self.editinfo_frame)
        self.date_edit.setObjectName(u"date_edit")
        self.date_edit.setGeometry(QRect(250, 440, 241, 21))
        font6 = QFont()
        font6.setFamilies([u"Manrope"])
        font6.setPointSize(8)
        self.date_edit.setFont(font6)
        self.date_edit.setStyleSheet(u"color: black;")
        self.save_button = QPushButton(self.editinfo_frame)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(280, 510, 171, 51))
        font7 = QFont()
        font7.setFamilies([u"Manrope"])
        font7.setPointSize(10)
        font7.setBold(True)
        self.save_button.setFont(font7)
        self.save_button.setLayoutDirection(Qt.RightToLeft)
        self.save_button.setStyleSheet(u"color: white; background-color: rgb(88,130,126)")
        self.name_label = QLabel(self.editinfo_frame)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(60, 120, 45, 31))
        self.name_label.setFont(font1)
        self.name_label.setStyleSheet(u"color: black;")
        self.name_label.setAlignment(Qt.AlignCenter)
        self.gmail_label = QLabel(self.editinfo_frame)
        self.gmail_label.setObjectName(u"gmail_label")
        self.gmail_label.setGeometry(QRect(60, 200, 41, 41))
        self.gmail_label.setFont(font1)
        self.gmail_label.setStyleSheet(u"color: black;")
        self.gmail_label.setAlignment(Qt.AlignCenter)
        self.phone_label = QLabel(self.editinfo_frame)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setGeometry(QRect(60, 280, 113, 41))
        self.phone_label.setFont(font1)
        self.phone_label.setStyleSheet(u"color: black;")
        self.phone_label.setAlignment(Qt.AlignCenter)
        self.gender_label = QLabel(self.editinfo_frame)
        self.gender_label.setObjectName(u"gender_label")
        self.gender_label.setGeometry(QRect(60, 350, 58, 31))
        self.gender_label.setFont(font1)
        self.gender_label.setStyleSheet(u"color: black;")
        self.gender_label.setAlignment(Qt.AlignCenter)
        self.birth_label = QLabel(self.editinfo_frame)
        self.birth_label.setObjectName(u"birth_label")
        self.birth_label.setGeometry(QRect(60, 430, 37, 41))
        self.birth_label.setFont(font1)
        self.birth_label.setStyleSheet(u"color: black;")
        self.birth_label.setAlignment(Qt.AlignCenter)
        self.profile_frame = QFrame(self.profile_frame_2)
        self.profile_frame.setObjectName(u"profile_frame")
        self.profile_frame.setGeometry(QRect(10, 10, 271, 601))
        self.profile_frame.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(88,130,126);\n"
"	border-radius: 20px;\n"
"\n"
"}\n"
"")
        self.profile_frame.setFrameShape(QFrame.StyledPanel)
        self.profile_frame.setFrameShadow(QFrame.Raised)
        self.page_label_4 = QLabel(self.profile_frame)
        self.page_label_4.setObjectName(u"page_label_4")
        self.page_label_4.setGeometry(QRect(20, 20, 141, 41))
        font8 = QFont()
        font8.setFamilies([u"Manrope"])
        font8.setPointSize(12)
        font8.setBold(True)
        self.page_label_4.setFont(font8)
        self.page_label_4.setStyleSheet(u"color: black;")
        self.page_label_4.setAlignment(Qt.AlignCenter)
        self.info_button = QPushButton(self.profile_frame)
        self.info_button.setObjectName(u"info_button")
        self.info_button.setGeometry(QRect(50, 70, 171, 51))
        font9 = QFont()
        font9.setFamilies([u"Manrope"])
        font9.setPointSize(11)
        font9.setBold(True)
        self.info_button.setFont(font9)
        self.info_button.setLayoutDirection(Qt.RightToLeft)
        self.info_button.setStyleSheet(u"color: black;")
        self.address_button = QPushButton(self.profile_frame)
        self.address_button.setObjectName(u"address_button")
        self.address_button.setGeometry(QRect(50, 130, 171, 51))
        self.address_button.setFont(font9)
        self.address_button.setLayoutDirection(Qt.LeftToRight)
        self.address_button.setStyleSheet(u"color: black;")
        self.address_button_2 = QPushButton(self.profile_frame)
        self.address_button_2.setObjectName(u"address_button_2")
        self.address_button_2.setGeometry(QRect(50, 190, 171, 51))
        self.address_button_2.setFont(font9)
        self.address_button_2.setLayoutDirection(Qt.LeftToRight)
        self.address_button_2.setStyleSheet(u"color: black;")

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
        self.page_label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt;\">My infomation</span></p></body></html>", None))
        self.name_edit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Manrope'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">sample_name</span></p></body></html>", None))
        self.mail_edit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Manrope'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">sample_email</span></p></body></html>", None))
        self.phonenum_edit.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Manrope'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">sameple_phonenumber</span></p></body></html>", None))
        self.male_button.setText(QCoreApplication.translate("Dialog", u"Male", None))
        self.female_button.setText(QCoreApplication.translate("Dialog", u"Female", None))
        self.others_button.setText(QCoreApplication.translate("Dialog", u"Others", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.name_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Name</span></p></body></html>", None))
        self.gmail_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Email</span></p></body></html>", None))
        self.phone_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Phone number</span></p></body></html>", None))
        self.gender_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Gender</span></p></body></html>", None))
        self.birth_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Birth</span></p></body></html>", None))
        self.page_label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:14pt;\">My Account</span></p></body></html>", None))
        self.info_button.setText(QCoreApplication.translate("Dialog", u"My infomation", None))
        self.address_button.setText(QCoreApplication.translate("Dialog", u"Address", None))
        self.address_button_2.setText(QCoreApplication.translate("Dialog", u"Create Shop", None))
    # retranslateUi

