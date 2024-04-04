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
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)
import icons_rc
import logo_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1200, 803)
        Dialog.setStyleSheet(u"QDialog{	\n"
"	background-color: white;  	\n"
"	border: None;\n"
"}\n"
"QPushButton{\n"
"	border: None;\n"
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
        self.frame_4 = QFrame(self.header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(50, 90, 1011, 631))
        self.frame_4.setStyleSheet(u"QLabel{\n"
"	color: black;\n"
"}\n"
"QPushButton{\n"
"	 background-color: rgb(88,130,126); \n"
"	color:white;\n"
"	border-radius: 20px;\n"
"	border: None;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.profile_frame = QFrame(self.frame_4)
        self.profile_frame.setObjectName(u"profile_frame")
        self.profile_frame.setGeometry(QRect(10, 10, 271, 601))
        self.profile_frame.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"	background-color: None;\n"
"	color: black;\n"
"}\n"
"\n"
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
        font3 = QFont()
        font3.setFamilies([u"Manrope"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.page_label_4.setFont(font3)
        self.page_label_4.setStyleSheet(u"color: black;")
        self.page_label_4.setAlignment(Qt.AlignCenter)
        self.info_button = QPushButton(self.profile_frame)
        self.info_button.setObjectName(u"info_button")
        self.info_button.setGeometry(QRect(50, 70, 171, 51))
        font4 = QFont()
        font4.setFamilies([u"Manrope"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.info_button.setFont(font4)
        self.info_button.setLayoutDirection(Qt.RightToLeft)
        self.info_button.setStyleSheet(u"color: black;")
        self.address_button = QPushButton(self.profile_frame)
        self.address_button.setObjectName(u"address_button")
        self.address_button.setGeometry(QRect(50, 130, 171, 51))
        self.address_button.setFont(font4)
        self.address_button.setLayoutDirection(Qt.LeftToRight)
        self.address_button.setStyleSheet(u"color: black;")
        self.create_shop_button = QPushButton(self.profile_frame)
        self.create_shop_button.setObjectName(u"create_shop_button")
        self.create_shop_button.setGeometry(QRect(50, 190, 171, 51))
        self.create_shop_button.setFont(font4)
        self.create_shop_button.setLayoutDirection(Qt.LeftToRight)
        self.create_shop_button.setStyleSheet(u"color: black;")
        self.editinfo_frame = QFrame(self.frame_4)
        self.editinfo_frame.setObjectName(u"editinfo_frame")
        self.editinfo_frame.setGeometry(QRect(290, 10, 701, 601))
        self.editinfo_frame.setStyleSheet(u"QFrame{\n"
"background-color:rgb(232, 243, 242)}")
        self.editinfo_frame.setFrameShape(QFrame.StyledPanel)
        self.editinfo_frame.setFrameShadow(QFrame.Raised)
        self.address_label = QLabel(self.editinfo_frame)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setGeometry(QRect(40, 20, 141, 41))
        self.address_label.setFont(font1)
        self.address_label.setAlignment(Qt.AlignCenter)
        self.my_address_label = QLabel(self.editinfo_frame)
        self.my_address_label.setObjectName(u"my_address_label")
        self.my_address_label.setGeometry(QRect(50, 90, 111, 41))
        font5 = QFont()
        font5.setFamilies([u"Manrope"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.my_address_label.setFont(font5)
        self.my_address_label.setAlignment(Qt.AlignCenter)
        self.add_address_button = QPushButton(self.editinfo_frame)
        self.add_address_button.setObjectName(u"add_address_button")
        self.add_address_button.setGeometry(QRect(440, 90, 171, 51))
        self.add_address_button.setFont(font3)
        self.add_address_button.setLayoutDirection(Qt.RightToLeft)
        self.add_address_button.setStyleSheet(u"")
        self.frame_3 = QFrame(self.editinfo_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(50, 160, 591, 421))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	background-color: white;\n"
"}\n"
"\n"
"QScrollArea {\n"
"	border-radius: 4px;\n"
"\n"
"}\n"
"\n"
"QPushBitton{\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.scrollArea = QScrollArea(self.frame_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 591, 421))
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"	border: None;\n"
"}\n"
"\n"
"QWidget{\n"
"	border-radius: 15px;\n"
"	border: 1px solid black\n"
"}\n"
"QLabel{\n"
"	border: None;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border: None;\n"
"}\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 589, 419))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 551, 381))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.verticalLayoutWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setFont(font5)
        self.widget_3.setStyleSheet(u"")
        self.first_label_3 = QLabel(self.widget_3)
        self.first_label_3.setObjectName(u"first_label_3")
        self.first_label_3.setGeometry(QRect(20, 10, 401, 41))
        self.first_label_3.setFont(font5)
        self.address_label_4 = QLabel(self.widget_3)
        self.address_label_4.setObjectName(u"address_label_4")
        self.address_label_4.setGeometry(QRect(20, 40, 411, 41))
        font6 = QFont()
        font6.setFamilies([u"Manrope"])
        font6.setPointSize(9)
        font6.setBold(True)
        self.address_label_4.setFont(font6)
        self.pushButton_3 = QPushButton(self.widget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(430, 20, 111, 41))
        self.pushButton_3.setFont(font6)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(88,130,126); \n"
"	color:white;\n"
"	border-radius: 20px;\n"
"}")

        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.verticalLayoutWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setFont(font5)
        self.widget_2.setStyleSheet(u"")
        self.first_label_2 = QLabel(self.widget_2)
        self.first_label_2.setObjectName(u"first_label_2")
        self.first_label_2.setGeometry(QRect(20, 10, 401, 41))
        self.first_label_2.setFont(font5)
        self.address_label_3 = QLabel(self.widget_2)
        self.address_label_3.setObjectName(u"address_label_3")
        self.address_label_3.setGeometry(QRect(20, 40, 411, 41))
        self.address_label_3.setFont(font6)
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(430, 20, 111, 41))
        self.pushButton_2.setFont(font6)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(88,130,126); \n"
"	color:white;\n"
"	border-radius: 20px;\n"
"}")

        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.verticalLayoutWidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setFont(font5)
        self.widget_4.setStyleSheet(u"")
        self.first_label_4 = QLabel(self.widget_4)
        self.first_label_4.setObjectName(u"first_label_4")
        self.first_label_4.setGeometry(QRect(20, 10, 401, 41))
        self.first_label_4.setFont(font5)
        self.address_label_5 = QLabel(self.widget_4)
        self.address_label_5.setObjectName(u"address_label_5")
        self.address_label_5.setGeometry(QRect(20, 40, 411, 41))
        self.address_label_5.setFont(font6)
        self.pushButton_4 = QPushButton(self.widget_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(430, 20, 111, 41))
        self.pushButton_4.setFont(font6)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(88,130,126); \n"
"	color:white;\n"
"	border-radius: 20px;\n"
"}")

        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget = QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setFont(font5)
        self.widget.setStyleSheet(u"")
        self.first_label = QLabel(self.widget)
        self.first_label.setObjectName(u"first_label")
        self.first_label.setGeometry(QRect(20, 10, 401, 41))
        self.first_label.setFont(font5)
        self.address_label_2 = QLabel(self.widget)
        self.address_label_2.setObjectName(u"address_label_2")
        self.address_label_2.setGeometry(QRect(20, 40, 411, 41))
        self.address_label_2.setFont(font6)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(430, 20, 111, 41))
        self.pushButton.setFont(font6)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(88,130,126); \n"
"	color:white;\n"
"	border-radius: 20px;\n"
"}")

        self.verticalLayout_2.addWidget(self.widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

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
        self.create_shop_button.setText(QCoreApplication.translate("Dialog", u"Create Shop", None))
        self.address_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:18pt;\">Address</span></p></body></html>", None))
        self.my_address_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:10pt;\">My address</span></p></body></html>", None))
        self.add_address_button.setText(QCoreApplication.translate("Dialog", u"+Add address", None))
        self.first_label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Moomoo Iceland +66  123456789</p></body></html>", None))
        self.address_label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:400;\">123 Skycastle Soi Disney Road Disney , Disneyland, 12345</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"edit", None))
        self.first_label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Moomoo Iceland +66  123456789</p></body></html>", None))
        self.address_label_3.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:400;\">123 Skycastle Soi Disney Road Disney , Disneyland, 12345</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"edit", None))
        self.first_label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Moomoo Iceland +66  123456789</p></body></html>", None))
        self.address_label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:400;\">123 Skycastle Soi Disney Road Disney , Disneyland, 12345</span></p></body></html>", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"edit", None))
        self.first_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Moomoo Iceland +66  123456789</p></body></html>", None))
        self.address_label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-weight:400;\">123 Skycastle Soi Disney Road Disney , Disneyland, 12345</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"edit", None))
    # retranslateUi

