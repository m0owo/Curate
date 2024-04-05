# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 's_info.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)
import icons_rc
import delivery_icons_rc
import logo_rc
import post_images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 800))
        MainWindow.setMaximumSize(QSize(1200, 800))
        MainWindow.setStyleSheet(u"#centralwidget {\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"QFrame {\n"
"    border:  none;\n"
"}\n"
"\n"
"* {\n"
"	color: black;\n"
"}")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(60, 20, 1080, 91))
        self.header.setMaximumSize(QSize(1080, 720))
        font = QFont()
        font.setFamilies([u".AppleSystemUIFont"])
        self.header.setFont(font)
        self.header.setAutoFillBackground(False)
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
        self.search_frame = QFrame(self.frame)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setEnabled(True)
        self.search_frame.setGeometry(QRect(130, 20, 581, 30))
        font1 = QFont()
        font1.setFamilies([u"Manrope"])
        self.search_frame.setFont(font1)
        self.search_frame.setStyleSheet(u"QLineEdit{\n"
"    color: rgb(190, 123, 193);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"#search_frame{\n"
"    border: solid;\n"
"    border-width: 1px;\n"
"    border-color: rgb(154, 152, 148);\n"
"}")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.search_icon = QLabel(self.search_frame)
        self.search_icon.setObjectName(u"search_icon")
        self.search_icon.setGeometry(QRect(10, 5, 18, 18))
        self.search_icon.setPixmap(QPixmap(u":/icon_images/search_icon.png"))
        self.search_icon.setScaledContents(True)
        self.filter_button = QPushButton(self.search_frame)
        self.filter_button.setObjectName(u"filter_button")
        self.filter_button.setGeometry(QRect(540, 0, 41, 30))
        icon = QIcon()
        icon.addFile(u":/icon_images/filter_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.filter_button.setIcon(icon)
        self.filter_button.setIconSize(QSize(20, 20))
        self.search_edit = QLineEdit(self.search_frame)
        self.search_edit.setObjectName(u"search_edit")
        self.search_edit.setGeometry(QRect(40, 5, 491, 16))
        self.search_edit.setFont(font1)
        self.home_button = QPushButton(self.frame)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setGeometry(QRect(740, 20, 41, 30))
        font2 = QFont()
        font2.setFamilies([u"Manrope"])
        font2.setBold(True)
        self.home_button.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/icon_images/home_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_button.setIcon(icon1)
        self.home_button.setIconSize(QSize(20, 20))
        self.history_button = QPushButton(self.frame)
        self.history_button.setObjectName(u"history_button")
        self.history_button.setGeometry(QRect(780, 20, 41, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icon_images/history_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.history_button.setIcon(icon2)
        self.history_button.setIconSize(QSize(20, 20))
        self.wishlist_button = QPushButton(self.frame)
        self.wishlist_button.setObjectName(u"wishlist_button")
        self.wishlist_button.setGeometry(QRect(820, 20, 41, 30))
        icon3 = QIcon()
        icon3.addFile(u":/icon_images/wishlist_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.wishlist_button.setIcon(icon3)
        self.wishlist_button.setIconSize(QSize(20, 20))
        self.profile_button = QPushButton(self.frame)
        self.profile_button.setObjectName(u"profile_button")
        self.profile_button.setGeometry(QRect(860, 20, 41, 30))
        icon4 = QIcon()
        icon4.addFile(u":/icon_images/profile_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_button.setIcon(icon4)
        self.profile_button.setIconSize(QSize(20, 20))
        self.page_label = QLabel(self.frame)
        self.page_label.setObjectName(u"page_label")
        self.page_label.setGeometry(QRect(30, 20, 71, 30))
        self.page_label.setFont(font2)
        self.page_label.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 10, 120, 71))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.curate_label = QLabel(self.frame_2)
        self.curate_label.setObjectName(u"curate_label")
        self.curate_label.setGeometry(QRect(-10, -10, 161, 91))
        font3 = QFont()
        font3.setFamilies([u"Mogena"])
        font3.setPointSize(18)
        self.curate_label.setFont(font3)
        self.curate_label.setPixmap(QPixmap(u":/logos/curatelogo.png"))
        self.curate_label.setScaledContents(True)
        self.curate_label.setAlignment(Qt.AlignCenter)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(60, 110, 1080, 630))
        self.frame_3.setMinimumSize(QSize(1080, 630))
        self.frame_3.setMaximumSize(QSize(1080, 630))
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet(u"QPushButton {\n"
"    background-color:#F5F9F9;\n"
"	border-radius: 20px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #E8F3F2;\n"
"}\n"
"\n"
"Line {\n"
"	background-color: #CCCCCC;\n"
"}\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(200, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"Manrope"])
        font4.setPointSize(26)
        font4.setBold(True)
        self.label.setFont(font4)

        self.verticalLayout.addWidget(self.label)

        self.info_button = QPushButton(self.frame_4)
        self.info_button.setObjectName(u"info_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.info_button.sizePolicy().hasHeightForWidth())
        self.info_button.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamilies([u"Manrope"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.info_button.setFont(font5)

        self.verticalLayout.addWidget(self.info_button)

        self.products_button = QPushButton(self.frame_4)
        self.products_button.setObjectName(u"products_button")
        sizePolicy1.setHeightForWidth(self.products_button.sizePolicy().hasHeightForWidth())
        self.products_button.setSizePolicy(sizePolicy1)
        self.products_button.setFont(font5)

        self.verticalLayout.addWidget(self.products_button)

        self.collections_button = QPushButton(self.frame_4)
        self.collections_button.setObjectName(u"collections_button")
        sizePolicy1.setHeightForWidth(self.collections_button.sizePolicy().hasHeightForWidth())
        self.collections_button.setSizePolicy(sizePolicy1)
        self.collections_button.setFont(font5)

        self.verticalLayout.addWidget(self.collections_button)

        self.orders_button = QPushButton(self.frame_4)
        self.orders_button.setObjectName(u"orders_button")
        sizePolicy1.setHeightForWidth(self.orders_button.sizePolicy().hasHeightForWidth())
        self.orders_button.setSizePolicy(sizePolicy1)
        self.orders_button.setFont(font5)

        self.verticalLayout.addWidget(self.orders_button)

        self.reviews_button = QPushButton(self.frame_4)
        self.reviews_button.setObjectName(u"reviews_button")
        sizePolicy1.setHeightForWidth(self.reviews_button.sizePolicy().hasHeightForWidth())
        self.reviews_button.setSizePolicy(sizePolicy1)
        self.reviews_button.setFont(font5)

        self.verticalLayout.addWidget(self.reviews_button)

        self.verticalSpacer = QSpacerItem(20, 260, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_4)

        self.line = QFrame(self.frame_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.main_frame = QFrame(self.frame_3)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 630))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.information = QWidget()
        self.information.setObjectName(u"information")
        self.information.setMinimumSize(QSize(0, 0))
        self.information.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.information)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.information)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font4)

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame_19 = QFrame(self.information)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"}")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_7 = QFrame(self.frame_19)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(180, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        font6 = QFont()
        font6.setFamilies([u"Manrope"])
        font6.setPointSize(16)
        font6.setBold(True)
        self.label_6.setFont(font6)

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font6)

        self.verticalLayout_5.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setFont(font6)

        self.verticalLayout_5.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setFont(font6)

        self.verticalLayout_5.addWidget(self.label_9)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_9.addWidget(self.frame_7)

        self.frame_9 = QFrame(self.frame_19)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"* {\n"
"	border-radius: 10px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.info_page_name_edit = QTextEdit(self.frame_9)
        self.info_page_name_edit.setObjectName(u"info_page_name_edit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.info_page_name_edit.sizePolicy().hasHeightForWidth())
        self.info_page_name_edit.setSizePolicy(sizePolicy3)
        self.info_page_name_edit.setMaximumSize(QSize(16777215, 30))
        font7 = QFont()
        font7.setFamilies([u"Manrope"])
        font7.setPointSize(12)
        self.info_page_name_edit.setFont(font7)
        self.info_page_name_edit.setStyleSheet(u"background-color: white")

        self.verticalLayout_6.addWidget(self.info_page_name_edit)

        self.info_page_email_edit = QTextEdit(self.frame_9)
        self.info_page_email_edit.setObjectName(u"info_page_email_edit")
        sizePolicy3.setHeightForWidth(self.info_page_email_edit.sizePolicy().hasHeightForWidth())
        self.info_page_email_edit.setSizePolicy(sizePolicy3)
        self.info_page_email_edit.setMaximumSize(QSize(16777215, 30))
        self.info_page_email_edit.setFont(font1)
        self.info_page_email_edit.setStyleSheet(u"background-color: white")

        self.verticalLayout_6.addWidget(self.info_page_email_edit)

        self.info_page_phone_number_edit = QTextEdit(self.frame_9)
        self.info_page_phone_number_edit.setObjectName(u"info_page_phone_number_edit")
        sizePolicy3.setHeightForWidth(self.info_page_phone_number_edit.sizePolicy().hasHeightForWidth())
        self.info_page_phone_number_edit.setSizePolicy(sizePolicy3)
        self.info_page_phone_number_edit.setMaximumSize(QSize(16777215, 30))
        font8 = QFont()
        font8.setFamilies([u"Manrope"])
        font8.setBold(False)
        self.info_page_phone_number_edit.setFont(font8)
        self.info_page_phone_number_edit.setStyleSheet(u"background-color: white")

        self.verticalLayout_6.addWidget(self.info_page_phone_number_edit)

        self.info_page_description_edit = QTextEdit(self.frame_9)
        self.info_page_description_edit.setObjectName(u"info_page_description_edit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.info_page_description_edit.sizePolicy().hasHeightForWidth())
        self.info_page_description_edit.setSizePolicy(sizePolicy4)
        self.info_page_description_edit.setFont(font8)
        self.info_page_description_edit.setStyleSheet(u"background-color: white")

        self.verticalLayout_6.addWidget(self.info_page_description_edit)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.horizontalLayout_9.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.frame_19)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setStyleSheet(u"QPushButton {\n"
"    background-color:#58827E;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #4D7672;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy5)
        self.label_12.setFont(font6)

        self.horizontalLayout_10.addWidget(self.label_12)

        self.info_page_edit_button = QPushButton(self.frame_10)
        self.info_page_edit_button.setObjectName(u"info_page_edit_button")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.info_page_edit_button.sizePolicy().hasHeightForWidth())
        self.info_page_edit_button.setSizePolicy(sizePolicy6)
        self.info_page_edit_button.setMinimumSize(QSize(0, 30))
        self.info_page_edit_button.setMaximumSize(QSize(16777215, 30))
        font9 = QFont()
        font9.setFamilies([u"Manrope"])
        font9.setPointSize(15)
        font9.setBold(True)
        self.info_page_edit_button.setFont(font9)

        self.horizontalLayout_10.addWidget(self.info_page_edit_button)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_13)


        self.verticalLayout_7.addWidget(self.frame_10)

        self.info_page_picture = QLabel(self.frame_8)
        self.info_page_picture.setObjectName(u"info_page_picture")
        sizePolicy3.setHeightForWidth(self.info_page_picture.sizePolicy().hasHeightForWidth())
        self.info_page_picture.setSizePolicy(sizePolicy3)
        self.info_page_picture.setMaximumSize(QSize(250, 250))
        self.info_page_picture.setPixmap(QPixmap(u":/post_images/IMG_7109.jpg"))
        self.info_page_picture.setScaledContents(True)
        self.info_page_picture.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.info_page_picture)

        self.verticalSpacer_4 = QSpacerItem(20, 205, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.frame_17 = QFrame(self.frame_8)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy2.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy2)
        self.frame_17.setStyleSheet(u"QPushButton {\n"
"    background-color:#58827E;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #4D7672;\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)

        self.info_page_save_button = QPushButton(self.frame_17)
        self.info_page_save_button.setObjectName(u"info_page_save_button")
        sizePolicy6.setHeightForWidth(self.info_page_save_button.sizePolicy().hasHeightForWidth())
        self.info_page_save_button.setSizePolicy(sizePolicy6)
        self.info_page_save_button.setMinimumSize(QSize(0, 30))
        self.info_page_save_button.setMaximumSize(QSize(16777215, 30))
        self.info_page_save_button.setFont(font9)

        self.horizontalLayout_11.addWidget(self.info_page_save_button)


        self.verticalLayout_7.addWidget(self.frame_17)


        self.horizontalLayout_9.addWidget(self.frame_8)


        self.verticalLayout_2.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.information)
        self.product = QWidget()
        self.product.setObjectName(u"product")
        self.verticalLayout_23 = QVBoxLayout(self.product)
        self.verticalLayout_23.setSpacing(10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.product_label_frame = QFrame(self.product)
        self.product_label_frame.setObjectName(u"product_label_frame")
        sizePolicy2.setHeightForWidth(self.product_label_frame.sizePolicy().hasHeightForWidth())
        self.product_label_frame.setSizePolicy(sizePolicy2)
        self.product_label_frame.setStyleSheet(u"QPushButton {\n"
"    background-color:#58827E;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #4D7672;\n"
"}")
        self.product_label_frame.setFrameShape(QFrame.StyledPanel)
        self.product_label_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.product_label_frame)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.products_label = QLabel(self.product_label_frame)
        self.products_label.setObjectName(u"products_label")
        sizePolicy5.setHeightForWidth(self.products_label.sizePolicy().hasHeightForWidth())
        self.products_label.setSizePolicy(sizePolicy5)
        self.products_label.setFont(font4)

        self.horizontalLayout_4.addWidget(self.products_label)

        self.product_page_add_product_button = QPushButton(self.product_label_frame)
        self.product_page_add_product_button.setObjectName(u"product_page_add_product_button")
        sizePolicy6.setHeightForWidth(self.product_page_add_product_button.sizePolicy().hasHeightForWidth())
        self.product_page_add_product_button.setSizePolicy(sizePolicy6)
        self.product_page_add_product_button.setMinimumSize(QSize(0, 30))
        self.product_page_add_product_button.setMaximumSize(QSize(30, 30))
        self.product_page_add_product_button.setFont(font9)

        self.horizontalLayout_4.addWidget(self.product_page_add_product_button)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)


        self.verticalLayout_23.addWidget(self.product_label_frame)

        self.product_tab = QWidget(self.product)
        self.product_tab.setObjectName(u"product_tab")
        sizePolicy5.setHeightForWidth(self.product_tab.sizePolicy().hasHeightForWidth())
        self.product_tab.setSizePolicy(sizePolicy5)
        self.product_tab.setMaximumSize(QSize(16777215, 50))
        self.product_tab.setStyleSheet(u"QPushButton {\n"
"    background-color:#F5F9F9;\n"
"	border-radius: 20px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #E8F3F2;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.product_tab)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.product_page_all_button = QPushButton(self.product_tab)
        self.product_page_all_button.setObjectName(u"product_page_all_button")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.product_page_all_button.sizePolicy().hasHeightForWidth())
        self.product_page_all_button.setSizePolicy(sizePolicy7)
        font10 = QFont()
        font10.setFamilies([u"Manrope"])
        font10.setPointSize(13)
        font10.setBold(True)
        self.product_page_all_button.setFont(font10)

        self.horizontalLayout_3.addWidget(self.product_page_all_button)

        self.product_page_live_button = QPushButton(self.product_tab)
        self.product_page_live_button.setObjectName(u"product_page_live_button")
        sizePolicy7.setHeightForWidth(self.product_page_live_button.sizePolicy().hasHeightForWidth())
        self.product_page_live_button.setSizePolicy(sizePolicy7)
        self.product_page_live_button.setFont(font10)

        self.horizontalLayout_3.addWidget(self.product_page_live_button)

        self.product_page_starting_button = QPushButton(self.product_tab)
        self.product_page_starting_button.setObjectName(u"product_page_starting_button")
        sizePolicy7.setHeightForWidth(self.product_page_starting_button.sizePolicy().hasHeightForWidth())
        self.product_page_starting_button.setSizePolicy(sizePolicy7)
        self.product_page_starting_button.setFont(font10)

        self.horizontalLayout_3.addWidget(self.product_page_starting_button)

        self.product_page_completed_button = QPushButton(self.product_tab)
        self.product_page_completed_button.setObjectName(u"product_page_completed_button")
        sizePolicy7.setHeightForWidth(self.product_page_completed_button.sizePolicy().hasHeightForWidth())
        self.product_page_completed_button.setSizePolicy(sizePolicy7)
        self.product_page_completed_button.setFont(font10)

        self.horizontalLayout_3.addWidget(self.product_page_completed_button)


        self.verticalLayout_23.addWidget(self.product_tab)

        self.products_scrollArea = QScrollArea(self.product)
        self.products_scrollArea.setObjectName(u"products_scrollArea")
        sizePolicy5.setHeightForWidth(self.products_scrollArea.sizePolicy().hasHeightForWidth())
        self.products_scrollArea.setSizePolicy(sizePolicy5)
        self.products_scrollArea.setMinimumSize(QSize(0, 0))
        self.products_scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.products_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.products_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.products_scrollArea.setWidgetResizable(True)
        self.products_crollAreaWidgetContents = QWidget()
        self.products_crollAreaWidgetContents.setObjectName(u"products_crollAreaWidgetContents")
        self.products_crollAreaWidgetContents.setGeometry(QRect(0, 0, 851, 680))
        sizePolicy5.setHeightForWidth(self.products_crollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.products_crollAreaWidgetContents.setSizePolicy(sizePolicy5)
        self.products_crollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.products_crollAreaWidgetContents.setMaximumSize(QSize(16777215, 16777215))
        self.products_crollAreaWidgetContents.setAutoFillBackground(False)
        self.products_crollAreaWidgetContents.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QFrame {\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color:#58827E;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #4D7672;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.products_crollAreaWidgetContents)
        self.verticalLayout_13.setSpacing(20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.product_box_1 = QFrame(self.products_crollAreaWidgetContents)
        self.product_box_1.setObjectName(u"product_box_1")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.product_box_1.sizePolicy().hasHeightForWidth())
        self.product_box_1.setSizePolicy(sizePolicy8)
        self.product_box_1.setMinimumSize(QSize(0, 150))
        self.product_box_1.setMaximumSize(QSize(16777215, 150))
        self.product_box_1.setAutoFillBackground(False)
        self.product_box_1.setFrameShape(QFrame.StyledPanel)
        self.product_box_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.product_box_1)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(15)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.product_frame = QFrame(self.product_box_1)
        self.product_frame.setObjectName(u"product_frame")
        self.product_frame.setMinimumSize(QSize(400, 0))
        self.product_frame.setMaximumSize(QSize(500, 16777215))
        self.product_frame.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"}")
        self.product_frame.setFrameShape(QFrame.StyledPanel)
        self.product_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.product_frame)
        self.horizontalLayout_18.setSpacing(15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(20, 15, 20, 15)
        self.product_image_label = QLabel(self.product_frame)
        self.product_image_label.setObjectName(u"product_image_label")
        self.product_image_label.setMaximumSize(QSize(110, 110))
        self.product_image_label.setStyleSheet(u"")
        self.product_image_label.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.product_image_label.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.product_image_label)

        self.frame_6 = QFrame(self.product_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.product_name_label = QLabel(self.frame_6)
        self.product_name_label.setObjectName(u"product_name_label")
        sizePolicy2.setHeightForWidth(self.product_name_label.sizePolicy().hasHeightForWidth())
        self.product_name_label.setSizePolicy(sizePolicy2)
        self.product_name_label.setFont(font6)

        self.verticalLayout_14.addWidget(self.product_name_label)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_9)

        self.price_label = QLabel(self.frame_6)
        self.price_label.setObjectName(u"price_label")
        self.price_label.setFont(font10)
        self.price_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.price_label)


        self.horizontalLayout_18.addWidget(self.frame_6)


        self.horizontalLayout_17.addWidget(self.product_frame)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(10)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.info_frame = QFrame(self.product_box_1)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMinimumSize(QSize(0, 0))
        self.info_frame.setMaximumSize(QSize(16777215, 120))
        self.info_frame.setStyleSheet(u"QFrame {\n"
"    background-color:#E8F3F2;\n"
"	border: none;\n"
"}")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.info_frame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(20, 12, 20, 12)
        self.sale_date_label = QLabel(self.info_frame)
        self.sale_date_label.setObjectName(u"sale_date_label")
        self.sale_date_label.setFont(font10)

        self.verticalLayout_16.addWidget(self.sale_date_label)

        self.mode_label = QLabel(self.info_frame)
        self.mode_label.setObjectName(u"mode_label")
        self.mode_label.setFont(font10)

        self.verticalLayout_16.addWidget(self.mode_label)

        self.status_label = QLabel(self.info_frame)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setFont(font10)

        self.verticalLayout_16.addWidget(self.status_label)


        self.verticalLayout_15.addWidget(self.info_frame)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(14)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer)

        self.view_product_button = QPushButton(self.product_box_1)
        self.view_product_button.setObjectName(u"view_product_button")
        sizePolicy6.setHeightForWidth(self.view_product_button.sizePolicy().hasHeightForWidth())
        self.view_product_button.setSizePolicy(sizePolicy6)
        self.view_product_button.setMinimumSize(QSize(0, 30))
        self.view_product_button.setFont(font10)

        self.horizontalLayout_19.addWidget(self.view_product_button)


        self.verticalLayout_15.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_17.addLayout(self.verticalLayout_15)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_17)


        self.verticalLayout_13.addWidget(self.product_box_1)

        self.product_box_2 = QFrame(self.products_crollAreaWidgetContents)
        self.product_box_2.setObjectName(u"product_box_2")
        sizePolicy8.setHeightForWidth(self.product_box_2.sizePolicy().hasHeightForWidth())
        self.product_box_2.setSizePolicy(sizePolicy8)
        self.product_box_2.setMinimumSize(QSize(0, 150))
        self.product_box_2.setMaximumSize(QSize(16777215, 150))
        self.product_box_2.setAutoFillBackground(False)
        self.product_box_2.setFrameShape(QFrame.StyledPanel)
        self.product_box_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.product_box_2)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setSpacing(15)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.product_frame_6 = QFrame(self.product_box_2)
        self.product_frame_6.setObjectName(u"product_frame_6")
        self.product_frame_6.setMinimumSize(QSize(400, 0))
        self.product_frame_6.setMaximumSize(QSize(500, 16777215))
        self.product_frame_6.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"}")
        self.product_frame_6.setFrameShape(QFrame.StyledPanel)
        self.product_frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.product_frame_6)
        self.horizontalLayout_34.setSpacing(15)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(20, 15, 20, 15)
        self.product_image_label_6 = QLabel(self.product_frame_6)
        self.product_image_label_6.setObjectName(u"product_image_label_6")
        self.product_image_label_6.setMaximumSize(QSize(110, 110))
        self.product_image_label_6.setStyleSheet(u"")
        self.product_image_label_6.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.product_image_label_6.setScaledContents(True)

        self.horizontalLayout_34.addWidget(self.product_image_label_6)

        self.frame_11 = QFrame(self.product_frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_11)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.product_name_label_6 = QLabel(self.frame_11)
        self.product_name_label_6.setObjectName(u"product_name_label_6")
        sizePolicy2.setHeightForWidth(self.product_name_label_6.sizePolicy().hasHeightForWidth())
        self.product_name_label_6.setSizePolicy(sizePolicy2)
        self.product_name_label_6.setFont(font6)

        self.verticalLayout_30.addWidget(self.product_name_label_6)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_14)

        self.price_label_6 = QLabel(self.frame_11)
        self.price_label_6.setObjectName(u"price_label_6")
        self.price_label_6.setFont(font10)
        self.price_label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_30.addWidget(self.price_label_6)


        self.horizontalLayout_34.addWidget(self.frame_11)


        self.horizontalLayout_33.addWidget(self.product_frame_6)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setSpacing(10)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.info_frame_6 = QFrame(self.product_box_2)
        self.info_frame_6.setObjectName(u"info_frame_6")
        self.info_frame_6.setMinimumSize(QSize(0, 0))
        self.info_frame_6.setMaximumSize(QSize(16777215, 120))
        self.info_frame_6.setStyleSheet(u"QFrame {\n"
"    background-color:#E8F3F2;\n"
"	border: none;\n"
"}")
        self.info_frame_6.setFrameShape(QFrame.StyledPanel)
        self.info_frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.info_frame_6)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(20, 12, 20, 12)
        self.sale_date_label_6 = QLabel(self.info_frame_6)
        self.sale_date_label_6.setObjectName(u"sale_date_label_6")
        self.sale_date_label_6.setFont(font10)

        self.verticalLayout_32.addWidget(self.sale_date_label_6)

        self.mode_label_6 = QLabel(self.info_frame_6)
        self.mode_label_6.setObjectName(u"mode_label_6")
        self.mode_label_6.setFont(font10)

        self.verticalLayout_32.addWidget(self.mode_label_6)

        self.status_label_6 = QLabel(self.info_frame_6)
        self.status_label_6.setObjectName(u"status_label_6")
        self.status_label_6.setFont(font10)

        self.verticalLayout_32.addWidget(self.status_label_6)


        self.verticalLayout_31.addWidget(self.info_frame_6)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(14)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_6)

        self.view_product_button_6 = QPushButton(self.product_box_2)
        self.view_product_button_6.setObjectName(u"view_product_button_6")
        sizePolicy6.setHeightForWidth(self.view_product_button_6.sizePolicy().hasHeightForWidth())
        self.view_product_button_6.setSizePolicy(sizePolicy6)
        self.view_product_button_6.setMinimumSize(QSize(0, 30))
        self.view_product_button_6.setFont(font10)

        self.horizontalLayout_35.addWidget(self.view_product_button_6)


        self.verticalLayout_31.addLayout(self.horizontalLayout_35)


        self.horizontalLayout_33.addLayout(self.verticalLayout_31)


        self.horizontalLayout_32.addLayout(self.horizontalLayout_33)


        self.verticalLayout_13.addWidget(self.product_box_2)

        self.product_box_3 = QFrame(self.products_crollAreaWidgetContents)
        self.product_box_3.setObjectName(u"product_box_3")
        sizePolicy8.setHeightForWidth(self.product_box_3.sizePolicy().hasHeightForWidth())
        self.product_box_3.setSizePolicy(sizePolicy8)
        self.product_box_3.setMinimumSize(QSize(0, 150))
        self.product_box_3.setMaximumSize(QSize(16777215, 150))
        self.product_box_3.setAutoFillBackground(False)
        self.product_box_3.setFrameShape(QFrame.StyledPanel)
        self.product_box_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.product_box_3)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setSpacing(15)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.product_frame_7 = QFrame(self.product_box_3)
        self.product_frame_7.setObjectName(u"product_frame_7")
        self.product_frame_7.setMinimumSize(QSize(400, 0))
        self.product_frame_7.setMaximumSize(QSize(500, 16777215))
        self.product_frame_7.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"}")
        self.product_frame_7.setFrameShape(QFrame.StyledPanel)
        self.product_frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.product_frame_7)
        self.horizontalLayout_38.setSpacing(15)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(20, 15, 20, 15)
        self.product_image_label_7 = QLabel(self.product_frame_7)
        self.product_image_label_7.setObjectName(u"product_image_label_7")
        self.product_image_label_7.setMaximumSize(QSize(110, 110))
        self.product_image_label_7.setStyleSheet(u"")
        self.product_image_label_7.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.product_image_label_7.setScaledContents(True)

        self.horizontalLayout_38.addWidget(self.product_image_label_7)

        self.frame_12 = QFrame(self.product_frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_12)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.product_name_label_7 = QLabel(self.frame_12)
        self.product_name_label_7.setObjectName(u"product_name_label_7")
        sizePolicy2.setHeightForWidth(self.product_name_label_7.sizePolicy().hasHeightForWidth())
        self.product_name_label_7.setSizePolicy(sizePolicy2)
        self.product_name_label_7.setFont(font6)

        self.verticalLayout_33.addWidget(self.product_name_label_7)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_16)

        self.price_label_7 = QLabel(self.frame_12)
        self.price_label_7.setObjectName(u"price_label_7")
        self.price_label_7.setFont(font10)
        self.price_label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_33.addWidget(self.price_label_7)


        self.horizontalLayout_38.addWidget(self.frame_12)


        self.horizontalLayout_37.addWidget(self.product_frame_7)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setSpacing(10)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.info_frame_7 = QFrame(self.product_box_3)
        self.info_frame_7.setObjectName(u"info_frame_7")
        self.info_frame_7.setMinimumSize(QSize(0, 0))
        self.info_frame_7.setMaximumSize(QSize(16777215, 120))
        self.info_frame_7.setStyleSheet(u"QFrame {\n"
"    background-color:#E8F3F2;\n"
"	border: none;\n"
"}")
        self.info_frame_7.setFrameShape(QFrame.StyledPanel)
        self.info_frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.info_frame_7)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(20, 12, 20, 12)
        self.sale_date_label_7 = QLabel(self.info_frame_7)
        self.sale_date_label_7.setObjectName(u"sale_date_label_7")
        self.sale_date_label_7.setFont(font10)

        self.verticalLayout_35.addWidget(self.sale_date_label_7)

        self.mode_label_7 = QLabel(self.info_frame_7)
        self.mode_label_7.setObjectName(u"mode_label_7")
        self.mode_label_7.setFont(font10)

        self.verticalLayout_35.addWidget(self.mode_label_7)

        self.status_label_7 = QLabel(self.info_frame_7)
        self.status_label_7.setObjectName(u"status_label_7")
        self.status_label_7.setFont(font10)

        self.verticalLayout_35.addWidget(self.status_label_7)


        self.verticalLayout_34.addWidget(self.info_frame_7)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setSpacing(14)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_7)

        self.view_product_button_7 = QPushButton(self.product_box_3)
        self.view_product_button_7.setObjectName(u"view_product_button_7")
        sizePolicy6.setHeightForWidth(self.view_product_button_7.sizePolicy().hasHeightForWidth())
        self.view_product_button_7.setSizePolicy(sizePolicy6)
        self.view_product_button_7.setMinimumSize(QSize(0, 30))
        self.view_product_button_7.setFont(font10)

        self.horizontalLayout_39.addWidget(self.view_product_button_7)


        self.verticalLayout_34.addLayout(self.horizontalLayout_39)


        self.horizontalLayout_37.addLayout(self.verticalLayout_34)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_37)


        self.verticalLayout_13.addWidget(self.product_box_3)

        self.product_box_4 = QFrame(self.products_crollAreaWidgetContents)
        self.product_box_4.setObjectName(u"product_box_4")
        sizePolicy8.setHeightForWidth(self.product_box_4.sizePolicy().hasHeightForWidth())
        self.product_box_4.setSizePolicy(sizePolicy8)
        self.product_box_4.setMinimumSize(QSize(0, 150))
        self.product_box_4.setMaximumSize(QSize(16777215, 150))
        self.product_box_4.setAutoFillBackground(False)
        self.product_box_4.setFrameShape(QFrame.StyledPanel)
        self.product_box_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.product_box_4)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setSpacing(15)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.product_frame_8 = QFrame(self.product_box_4)
        self.product_frame_8.setObjectName(u"product_frame_8")
        self.product_frame_8.setMinimumSize(QSize(400, 0))
        self.product_frame_8.setMaximumSize(QSize(500, 16777215))
        self.product_frame_8.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"}")
        self.product_frame_8.setFrameShape(QFrame.StyledPanel)
        self.product_frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.product_frame_8)
        self.horizontalLayout_42.setSpacing(15)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(20, 15, 20, 15)
        self.product_image_label_8 = QLabel(self.product_frame_8)
        self.product_image_label_8.setObjectName(u"product_image_label_8")
        self.product_image_label_8.setMaximumSize(QSize(110, 110))
        self.product_image_label_8.setStyleSheet(u"")
        self.product_image_label_8.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.product_image_label_8.setScaledContents(True)

        self.horizontalLayout_42.addWidget(self.product_image_label_8)

        self.frame_13 = QFrame(self.product_frame_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_13)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.product_name_label_8 = QLabel(self.frame_13)
        self.product_name_label_8.setObjectName(u"product_name_label_8")
        sizePolicy2.setHeightForWidth(self.product_name_label_8.sizePolicy().hasHeightForWidth())
        self.product_name_label_8.setSizePolicy(sizePolicy2)
        self.product_name_label_8.setFont(font6)

        self.verticalLayout_36.addWidget(self.product_name_label_8)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_17)

        self.price_label_8 = QLabel(self.frame_13)
        self.price_label_8.setObjectName(u"price_label_8")
        self.price_label_8.setFont(font10)
        self.price_label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_36.addWidget(self.price_label_8)


        self.horizontalLayout_42.addWidget(self.frame_13)


        self.horizontalLayout_41.addWidget(self.product_frame_8)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setSpacing(10)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.info_frame_8 = QFrame(self.product_box_4)
        self.info_frame_8.setObjectName(u"info_frame_8")
        self.info_frame_8.setMinimumSize(QSize(0, 0))
        self.info_frame_8.setMaximumSize(QSize(16777215, 120))
        self.info_frame_8.setStyleSheet(u"QFrame {\n"
"    background-color:#E8F3F2;\n"
"	border: none;\n"
"}")
        self.info_frame_8.setFrameShape(QFrame.StyledPanel)
        self.info_frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.info_frame_8)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(20, 12, 20, 12)
        self.sale_date_label_8 = QLabel(self.info_frame_8)
        self.sale_date_label_8.setObjectName(u"sale_date_label_8")
        self.sale_date_label_8.setFont(font10)

        self.verticalLayout_38.addWidget(self.sale_date_label_8)

        self.mode_label_8 = QLabel(self.info_frame_8)
        self.mode_label_8.setObjectName(u"mode_label_8")
        self.mode_label_8.setFont(font10)

        self.verticalLayout_38.addWidget(self.mode_label_8)

        self.status_label_8 = QLabel(self.info_frame_8)
        self.status_label_8.setObjectName(u"status_label_8")
        self.status_label_8.setFont(font10)

        self.verticalLayout_38.addWidget(self.status_label_8)


        self.verticalLayout_37.addWidget(self.info_frame_8)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setSpacing(14)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_8)

        self.view_product_button_8 = QPushButton(self.product_box_4)
        self.view_product_button_8.setObjectName(u"view_product_button_8")
        sizePolicy6.setHeightForWidth(self.view_product_button_8.sizePolicy().hasHeightForWidth())
        self.view_product_button_8.setSizePolicy(sizePolicy6)
        self.view_product_button_8.setMinimumSize(QSize(0, 30))
        self.view_product_button_8.setFont(font10)

        self.horizontalLayout_43.addWidget(self.view_product_button_8)


        self.verticalLayout_37.addLayout(self.horizontalLayout_43)


        self.horizontalLayout_41.addLayout(self.verticalLayout_37)


        self.horizontalLayout_40.addLayout(self.horizontalLayout_41)


        self.verticalLayout_13.addWidget(self.product_box_4)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_15)

        self.products_scrollArea.setWidget(self.products_crollAreaWidgetContents)

        self.verticalLayout_23.addWidget(self.products_scrollArea)

        self.stackedWidget.addWidget(self.product)
        self.collection = QWidget()
        self.collection.setObjectName(u"collection")
        self.verticalLayout_3 = QVBoxLayout(self.collection)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.collection)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy2.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy2)
        self.frame_18.setStyleSheet(u"QPushButton {\n"
"    background-color:#58827E;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #4D7672;\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.collection_label = QLabel(self.frame_18)
        self.collection_label.setObjectName(u"collection_label")
        sizePolicy5.setHeightForWidth(self.collection_label.sizePolicy().hasHeightForWidth())
        self.collection_label.setSizePolicy(sizePolicy5)
        self.collection_label.setFont(font4)

        self.horizontalLayout_5.addWidget(self.collection_label)

        self.collection_page_add_collection_button = QPushButton(self.frame_18)
        self.collection_page_add_collection_button.setObjectName(u"collection_page_add_collection_button")
        sizePolicy6.setHeightForWidth(self.collection_page_add_collection_button.sizePolicy().hasHeightForWidth())
        self.collection_page_add_collection_button.setSizePolicy(sizePolicy6)
        self.collection_page_add_collection_button.setMinimumSize(QSize(0, 30))
        self.collection_page_add_collection_button.setMaximumSize(QSize(30, 30))
        self.collection_page_add_collection_button.setFont(font9)

        self.horizontalLayout_5.addWidget(self.collection_page_add_collection_button)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_14)


        self.verticalLayout_3.addWidget(self.frame_18)

        self.history_tabs_3 = QWidget(self.collection)
        self.history_tabs_3.setObjectName(u"history_tabs_3")
        sizePolicy5.setHeightForWidth(self.history_tabs_3.sizePolicy().hasHeightForWidth())
        self.history_tabs_3.setSizePolicy(sizePolicy5)
        self.history_tabs_3.setMaximumSize(QSize(16777215, 50))
        self.history_tabs_3.setStyleSheet(u"QPushButton {\n"
"    background-color:#F5F9F9;\n"
"	border-radius: 20px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #E8F3F2;\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.history_tabs_3)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.collection_page_all_button = QPushButton(self.history_tabs_3)
        self.collection_page_all_button.setObjectName(u"collection_page_all_button")
        sizePolicy7.setHeightForWidth(self.collection_page_all_button.sizePolicy().hasHeightForWidth())
        self.collection_page_all_button.setSizePolicy(sizePolicy7)
        self.collection_page_all_button.setFont(font10)

        self.horizontalLayout_6.addWidget(self.collection_page_all_button)

        self.collection_page_live_button = QPushButton(self.history_tabs_3)
        self.collection_page_live_button.setObjectName(u"collection_page_live_button")
        sizePolicy7.setHeightForWidth(self.collection_page_live_button.sizePolicy().hasHeightForWidth())
        self.collection_page_live_button.setSizePolicy(sizePolicy7)
        self.collection_page_live_button.setFont(font10)

        self.horizontalLayout_6.addWidget(self.collection_page_live_button)

        self.collection_page_starting_button = QPushButton(self.history_tabs_3)
        self.collection_page_starting_button.setObjectName(u"collection_page_starting_button")
        sizePolicy7.setHeightForWidth(self.collection_page_starting_button.sizePolicy().hasHeightForWidth())
        self.collection_page_starting_button.setSizePolicy(sizePolicy7)
        self.collection_page_starting_button.setFont(font10)

        self.horizontalLayout_6.addWidget(self.collection_page_starting_button)

        self.collection_page_completed_button = QPushButton(self.history_tabs_3)
        self.collection_page_completed_button.setObjectName(u"collection_page_completed_button")
        sizePolicy7.setHeightForWidth(self.collection_page_completed_button.sizePolicy().hasHeightForWidth())
        self.collection_page_completed_button.setSizePolicy(sizePolicy7)
        self.collection_page_completed_button.setFont(font10)

        self.horizontalLayout_6.addWidget(self.collection_page_completed_button)


        self.verticalLayout_3.addWidget(self.history_tabs_3)

        self.collections_scrollArea = QScrollArea(self.collection)
        self.collections_scrollArea.setObjectName(u"collections_scrollArea")
        sizePolicy5.setHeightForWidth(self.collections_scrollArea.sizePolicy().hasHeightForWidth())
        self.collections_scrollArea.setSizePolicy(sizePolicy5)
        self.collections_scrollArea.setMinimumSize(QSize(0, 0))
        self.collections_scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.collections_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.collections_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.collections_scrollArea.setWidgetResizable(True)
        self.collections_scrollAreaWidgetContents = QWidget()
        self.collections_scrollAreaWidgetContents.setObjectName(u"collections_scrollAreaWidgetContents")
        self.collections_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 851, 510))
        sizePolicy5.setHeightForWidth(self.collections_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.collections_scrollAreaWidgetContents.setSizePolicy(sizePolicy5)
        self.collections_scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.collections_scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 16777215))
        self.collections_scrollAreaWidgetContents.setAutoFillBackground(False)
        self.collections_scrollAreaWidgetContents.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QFrame {\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color:#58827E;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #4D7672;\n"
"}")
        self.verticalLayout_39 = QVBoxLayout(self.collections_scrollAreaWidgetContents)
        self.verticalLayout_39.setSpacing(20)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.collection_box = QFrame(self.collections_scrollAreaWidgetContents)
        self.collection_box.setObjectName(u"collection_box")
        sizePolicy8.setHeightForWidth(self.collection_box.sizePolicy().hasHeightForWidth())
        self.collection_box.setSizePolicy(sizePolicy8)
        self.collection_box.setMinimumSize(QSize(0, 150))
        self.collection_box.setMaximumSize(QSize(16777215, 150))
        self.collection_box.setAutoFillBackground(False)
        self.collection_box.setFrameShape(QFrame.StyledPanel)
        self.collection_box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.collection_box)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setSpacing(15)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.product_frame_9 = QFrame(self.collection_box)
        self.product_frame_9.setObjectName(u"product_frame_9")
        self.product_frame_9.setMinimumSize(QSize(400, 0))
        self.product_frame_9.setMaximumSize(QSize(500, 16777215))
        self.product_frame_9.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"}")
        self.product_frame_9.setFrameShape(QFrame.StyledPanel)
        self.product_frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.product_frame_9)
        self.horizontalLayout_46.setSpacing(15)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(20, 15, 20, 15)
        self.product_image_label_9 = QLabel(self.product_frame_9)
        self.product_image_label_9.setObjectName(u"product_image_label_9")
        self.product_image_label_9.setMaximumSize(QSize(110, 110))
        self.product_image_label_9.setStyleSheet(u"")
        self.product_image_label_9.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.product_image_label_9.setScaledContents(True)

        self.horizontalLayout_46.addWidget(self.product_image_label_9)

        self.frame_14 = QFrame(self.product_frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_14)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.collection_name_label = QLabel(self.frame_14)
        self.collection_name_label.setObjectName(u"collection_name_label")
        sizePolicy2.setHeightForWidth(self.collection_name_label.sizePolicy().hasHeightForWidth())
        self.collection_name_label.setSizePolicy(sizePolicy2)
        self.collection_name_label.setFont(font6)

        self.verticalLayout_40.addWidget(self.collection_name_label)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_18)


        self.horizontalLayout_46.addWidget(self.frame_14)


        self.horizontalLayout_45.addWidget(self.product_frame_9)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setSpacing(10)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.info_frame_9 = QFrame(self.collection_box)
        self.info_frame_9.setObjectName(u"info_frame_9")
        self.info_frame_9.setMinimumSize(QSize(0, 0))
        self.info_frame_9.setMaximumSize(QSize(16777215, 120))
        self.info_frame_9.setStyleSheet(u"QFrame {\n"
"    background-color:#E8F3F2;\n"
"	border: none;\n"
"}")
        self.info_frame_9.setFrameShape(QFrame.StyledPanel)
        self.info_frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.info_frame_9)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(20, 12, 20, 12)
        self.sale_date_label_9 = QLabel(self.info_frame_9)
        self.sale_date_label_9.setObjectName(u"sale_date_label_9")
        self.sale_date_label_9.setFont(font10)

        self.verticalLayout_42.addWidget(self.sale_date_label_9)

        self.mode_label_9 = QLabel(self.info_frame_9)
        self.mode_label_9.setObjectName(u"mode_label_9")
        self.mode_label_9.setFont(font10)

        self.verticalLayout_42.addWidget(self.mode_label_9)

        self.status_label_9 = QLabel(self.info_frame_9)
        self.status_label_9.setObjectName(u"status_label_9")
        self.status_label_9.setFont(font10)

        self.verticalLayout_42.addWidget(self.status_label_9)


        self.verticalLayout_41.addWidget(self.info_frame_9)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setSpacing(14)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_10)

        self.view_product_button_10 = QPushButton(self.collection_box)
        self.view_product_button_10.setObjectName(u"view_product_button_10")
        sizePolicy6.setHeightForWidth(self.view_product_button_10.sizePolicy().hasHeightForWidth())
        self.view_product_button_10.setSizePolicy(sizePolicy6)
        self.view_product_button_10.setMinimumSize(QSize(0, 30))
        self.view_product_button_10.setFont(font10)

        self.horizontalLayout_47.addWidget(self.view_product_button_10)


        self.verticalLayout_41.addLayout(self.horizontalLayout_47)


        self.horizontalLayout_45.addLayout(self.verticalLayout_41)


        self.horizontalLayout_44.addLayout(self.horizontalLayout_45)


        self.verticalLayout_39.addWidget(self.collection_box)

        self.collection_box_2 = QFrame(self.collections_scrollAreaWidgetContents)
        self.collection_box_2.setObjectName(u"collection_box_2")
        sizePolicy8.setHeightForWidth(self.collection_box_2.sizePolicy().hasHeightForWidth())
        self.collection_box_2.setSizePolicy(sizePolicy8)
        self.collection_box_2.setMinimumSize(QSize(0, 150))
        self.collection_box_2.setMaximumSize(QSize(16777215, 150))
        self.collection_box_2.setAutoFillBackground(False)
        self.collection_box_2.setFrameShape(QFrame.StyledPanel)
        self.collection_box_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.collection_box_2)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setSpacing(15)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.product_frame_10 = QFrame(self.collection_box_2)
        self.product_frame_10.setObjectName(u"product_frame_10")
        self.product_frame_10.setMinimumSize(QSize(400, 0))
        self.product_frame_10.setMaximumSize(QSize(500, 16777215))
        self.product_frame_10.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"}")
        self.product_frame_10.setFrameShape(QFrame.StyledPanel)
        self.product_frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.product_frame_10)
        self.horizontalLayout_50.setSpacing(15)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(20, 15, 20, 15)
        self.product_image_label_10 = QLabel(self.product_frame_10)
        self.product_image_label_10.setObjectName(u"product_image_label_10")
        self.product_image_label_10.setMaximumSize(QSize(110, 110))
        self.product_image_label_10.setStyleSheet(u"")
        self.product_image_label_10.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.product_image_label_10.setScaledContents(True)

        self.horizontalLayout_50.addWidget(self.product_image_label_10)

        self.frame_15 = QFrame(self.product_frame_10)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_15)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.collection_name_label_2 = QLabel(self.frame_15)
        self.collection_name_label_2.setObjectName(u"collection_name_label_2")
        sizePolicy2.setHeightForWidth(self.collection_name_label_2.sizePolicy().hasHeightForWidth())
        self.collection_name_label_2.setSizePolicy(sizePolicy2)
        self.collection_name_label_2.setFont(font6)

        self.verticalLayout_43.addWidget(self.collection_name_label_2)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_43.addItem(self.verticalSpacer_19)


        self.horizontalLayout_50.addWidget(self.frame_15)


        self.horizontalLayout_49.addWidget(self.product_frame_10)

        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setSpacing(10)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.info_frame_10 = QFrame(self.collection_box_2)
        self.info_frame_10.setObjectName(u"info_frame_10")
        self.info_frame_10.setMinimumSize(QSize(0, 0))
        self.info_frame_10.setMaximumSize(QSize(16777215, 120))
        self.info_frame_10.setStyleSheet(u"QFrame {\n"
"    background-color:#E8F3F2;\n"
"	border: none;\n"
"}")
        self.info_frame_10.setFrameShape(QFrame.StyledPanel)
        self.info_frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.info_frame_10)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(20, 12, 20, 12)
        self.sale_date_label_10 = QLabel(self.info_frame_10)
        self.sale_date_label_10.setObjectName(u"sale_date_label_10")
        self.sale_date_label_10.setFont(font10)

        self.verticalLayout_45.addWidget(self.sale_date_label_10)

        self.mode_label_10 = QLabel(self.info_frame_10)
        self.mode_label_10.setObjectName(u"mode_label_10")
        self.mode_label_10.setFont(font10)

        self.verticalLayout_45.addWidget(self.mode_label_10)

        self.status_label_10 = QLabel(self.info_frame_10)
        self.status_label_10.setObjectName(u"status_label_10")
        self.status_label_10.setFont(font10)

        self.verticalLayout_45.addWidget(self.status_label_10)


        self.verticalLayout_44.addWidget(self.info_frame_10)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setSpacing(14)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_11)

        self.view_product_button_11 = QPushButton(self.collection_box_2)
        self.view_product_button_11.setObjectName(u"view_product_button_11")
        sizePolicy6.setHeightForWidth(self.view_product_button_11.sizePolicy().hasHeightForWidth())
        self.view_product_button_11.setSizePolicy(sizePolicy6)
        self.view_product_button_11.setMinimumSize(QSize(0, 30))
        self.view_product_button_11.setFont(font10)

        self.horizontalLayout_51.addWidget(self.view_product_button_11)


        self.verticalLayout_44.addLayout(self.horizontalLayout_51)


        self.horizontalLayout_49.addLayout(self.verticalLayout_44)


        self.horizontalLayout_48.addLayout(self.horizontalLayout_49)


        self.verticalLayout_39.addWidget(self.collection_box_2)

        self.collection_box_3 = QFrame(self.collections_scrollAreaWidgetContents)
        self.collection_box_3.setObjectName(u"collection_box_3")
        sizePolicy8.setHeightForWidth(self.collection_box_3.sizePolicy().hasHeightForWidth())
        self.collection_box_3.setSizePolicy(sizePolicy8)
        self.collection_box_3.setMinimumSize(QSize(0, 150))
        self.collection_box_3.setMaximumSize(QSize(16777215, 150))
        self.collection_box_3.setAutoFillBackground(False)
        self.collection_box_3.setFrameShape(QFrame.StyledPanel)
        self.collection_box_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.collection_box_3)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setSpacing(15)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.product_frame_11 = QFrame(self.collection_box_3)
        self.product_frame_11.setObjectName(u"product_frame_11")
        self.product_frame_11.setMinimumSize(QSize(400, 0))
        self.product_frame_11.setMaximumSize(QSize(500, 16777215))
        self.product_frame_11.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"}")
        self.product_frame_11.setFrameShape(QFrame.StyledPanel)
        self.product_frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.product_frame_11)
        self.horizontalLayout_54.setSpacing(15)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(20, 15, 20, 15)
        self.product_image_label_11 = QLabel(self.product_frame_11)
        self.product_image_label_11.setObjectName(u"product_image_label_11")
        self.product_image_label_11.setMaximumSize(QSize(110, 110))
        self.product_image_label_11.setStyleSheet(u"")
        self.product_image_label_11.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.product_image_label_11.setScaledContents(True)

        self.horizontalLayout_54.addWidget(self.product_image_label_11)

        self.frame_16 = QFrame(self.product_frame_11)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_16)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.collection_name_label_3 = QLabel(self.frame_16)
        self.collection_name_label_3.setObjectName(u"collection_name_label_3")
        sizePolicy2.setHeightForWidth(self.collection_name_label_3.sizePolicy().hasHeightForWidth())
        self.collection_name_label_3.setSizePolicy(sizePolicy2)
        self.collection_name_label_3.setFont(font6)

        self.verticalLayout_46.addWidget(self.collection_name_label_3)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_20)


        self.horizontalLayout_54.addWidget(self.frame_16)


        self.horizontalLayout_53.addWidget(self.product_frame_11)

        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setSpacing(10)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.info_frame_11 = QFrame(self.collection_box_3)
        self.info_frame_11.setObjectName(u"info_frame_11")
        self.info_frame_11.setMinimumSize(QSize(0, 0))
        self.info_frame_11.setMaximumSize(QSize(16777215, 120))
        self.info_frame_11.setStyleSheet(u"QFrame {\n"
"    background-color:#E8F3F2;\n"
"	border: none;\n"
"}")
        self.info_frame_11.setFrameShape(QFrame.StyledPanel)
        self.info_frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.info_frame_11)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(20, 12, 20, 12)
        self.sale_date_label_11 = QLabel(self.info_frame_11)
        self.sale_date_label_11.setObjectName(u"sale_date_label_11")
        self.sale_date_label_11.setFont(font10)

        self.verticalLayout_48.addWidget(self.sale_date_label_11)

        self.mode_label_11 = QLabel(self.info_frame_11)
        self.mode_label_11.setObjectName(u"mode_label_11")
        self.mode_label_11.setFont(font10)

        self.verticalLayout_48.addWidget(self.mode_label_11)

        self.status_label_11 = QLabel(self.info_frame_11)
        self.status_label_11.setObjectName(u"status_label_11")
        self.status_label_11.setFont(font10)

        self.verticalLayout_48.addWidget(self.status_label_11)


        self.verticalLayout_47.addWidget(self.info_frame_11)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setSpacing(14)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_12)

        self.view_product_button_12 = QPushButton(self.collection_box_3)
        self.view_product_button_12.setObjectName(u"view_product_button_12")
        sizePolicy6.setHeightForWidth(self.view_product_button_12.sizePolicy().hasHeightForWidth())
        self.view_product_button_12.setSizePolicy(sizePolicy6)
        self.view_product_button_12.setMinimumSize(QSize(0, 30))
        self.view_product_button_12.setFont(font10)

        self.horizontalLayout_55.addWidget(self.view_product_button_12)


        self.verticalLayout_47.addLayout(self.horizontalLayout_55)


        self.horizontalLayout_53.addLayout(self.verticalLayout_47)


        self.horizontalLayout_52.addLayout(self.horizontalLayout_53)


        self.verticalLayout_39.addWidget(self.collection_box_3)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_22)

        self.collections_scrollArea.setWidget(self.collections_scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.collections_scrollArea)

        self.stackedWidget.addWidget(self.collection)
        self.order = QWidget()
        self.order.setObjectName(u"order")
        self.verticalLayout_4 = QVBoxLayout(self.order)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.order)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy2.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy2)
        self.frame_24.setStyleSheet(u"QPushButton {\n"
"    background-color:#58827E;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #4D7672;\n"
"}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.order_label = QLabel(self.frame_24)
        self.order_label.setObjectName(u"order_label")
        sizePolicy5.setHeightForWidth(self.order_label.sizePolicy().hasHeightForWidth())
        self.order_label.setSizePolicy(sizePolicy5)
        self.order_label.setFont(font4)

        self.horizontalLayout_7.addWidget(self.order_label)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_19)


        self.verticalLayout_4.addWidget(self.frame_24)

        self.history_tabs_4 = QWidget(self.order)
        self.history_tabs_4.setObjectName(u"history_tabs_4")
        sizePolicy5.setHeightForWidth(self.history_tabs_4.sizePolicy().hasHeightForWidth())
        self.history_tabs_4.setSizePolicy(sizePolicy5)
        self.history_tabs_4.setMaximumSize(QSize(16777215, 50))
        self.history_tabs_4.setStyleSheet(u"QPushButton {\n"
"    background-color:#F5F9F9;\n"
"	border-radius: 20px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    background-color: #E8F3F2;\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.history_tabs_4)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.order_page_all_button = QPushButton(self.history_tabs_4)
        self.order_page_all_button.setObjectName(u"order_page_all_button")
        sizePolicy7.setHeightForWidth(self.order_page_all_button.sizePolicy().hasHeightForWidth())
        self.order_page_all_button.setSizePolicy(sizePolicy7)
        self.order_page_all_button.setFont(font10)

        self.horizontalLayout_8.addWidget(self.order_page_all_button)

        self.orders_page_unpaid_button = QPushButton(self.history_tabs_4)
        self.orders_page_unpaid_button.setObjectName(u"orders_page_unpaid_button")
        sizePolicy7.setHeightForWidth(self.orders_page_unpaid_button.sizePolicy().hasHeightForWidth())
        self.orders_page_unpaid_button.setSizePolicy(sizePolicy7)
        self.orders_page_unpaid_button.setFont(font10)

        self.horizontalLayout_8.addWidget(self.orders_page_unpaid_button)

        self.orders_page_shipping_button = QPushButton(self.history_tabs_4)
        self.orders_page_shipping_button.setObjectName(u"orders_page_shipping_button")
        sizePolicy7.setHeightForWidth(self.orders_page_shipping_button.sizePolicy().hasHeightForWidth())
        self.orders_page_shipping_button.setSizePolicy(sizePolicy7)
        self.orders_page_shipping_button.setFont(font10)

        self.horizontalLayout_8.addWidget(self.orders_page_shipping_button)

        self.orders_page_completed_button = QPushButton(self.history_tabs_4)
        self.orders_page_completed_button.setObjectName(u"orders_page_completed_button")
        sizePolicy7.setHeightForWidth(self.orders_page_completed_button.sizePolicy().hasHeightForWidth())
        self.orders_page_completed_button.setSizePolicy(sizePolicy7)
        self.orders_page_completed_button.setFont(font10)

        self.horizontalLayout_8.addWidget(self.orders_page_completed_button)

        self.oders_page_cancelled_button = QPushButton(self.history_tabs_4)
        self.oders_page_cancelled_button.setObjectName(u"oders_page_cancelled_button")
        sizePolicy7.setHeightForWidth(self.oders_page_cancelled_button.sizePolicy().hasHeightForWidth())
        self.oders_page_cancelled_button.setSizePolicy(sizePolicy7)
        self.oders_page_cancelled_button.setFont(font10)

        self.horizontalLayout_8.addWidget(self.oders_page_cancelled_button)


        self.verticalLayout_4.addWidget(self.history_tabs_4)

        self.orders_scrollArea = QScrollArea(self.order)
        self.orders_scrollArea.setObjectName(u"orders_scrollArea")
        sizePolicy5.setHeightForWidth(self.orders_scrollArea.sizePolicy().hasHeightForWidth())
        self.orders_scrollArea.setSizePolicy(sizePolicy5)
        self.orders_scrollArea.setMinimumSize(QSize(0, 0))
        self.orders_scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.orders_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.orders_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.orders_scrollArea.setWidgetResizable(True)
        self.orders_scrollAreaWidgetContents = QWidget()
        self.orders_scrollAreaWidgetContents.setObjectName(u"orders_scrollAreaWidgetContents")
        self.orders_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 851, 510))
        sizePolicy5.setHeightForWidth(self.orders_scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.orders_scrollAreaWidgetContents.setSizePolicy(sizePolicy5)
        self.orders_scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.orders_scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 16777215))
        self.orders_scrollAreaWidgetContents.setAutoFillBackground(False)
        self.orders_scrollAreaWidgetContents.setStyleSheet(u"QWidget {\n"
"	background-color: white;\n"
"}\n"
"\n"
"QFrame {\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color:#58827E;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #4D7672;\n"
"}")
        self.verticalLayout_52 = QVBoxLayout(self.orders_scrollAreaWidgetContents)
        self.verticalLayout_52.setSpacing(20)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.order_box = QFrame(self.orders_scrollAreaWidgetContents)
        self.order_box.setObjectName(u"order_box")
        sizePolicy8.setHeightForWidth(self.order_box.sizePolicy().hasHeightForWidth())
        self.order_box.setSizePolicy(sizePolicy8)
        self.order_box.setMinimumSize(QSize(0, 150))
        self.order_box.setMaximumSize(QSize(16777215, 150))
        self.order_box.setAutoFillBackground(False)
        self.order_box.setFrameShape(QFrame.StyledPanel)
        self.order_box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.order_box)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setSpacing(15)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.product_frame_13 = QFrame(self.order_box)
        self.product_frame_13.setObjectName(u"product_frame_13")
        self.product_frame_13.setMinimumSize(QSize(400, 0))
        self.product_frame_13.setMaximumSize(QSize(500, 16777215))
        self.product_frame_13.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"}")
        self.product_frame_13.setFrameShape(QFrame.StyledPanel)
        self.product_frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.product_frame_13)
        self.horizontalLayout_62.setSpacing(15)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(20, 15, 20, 15)
        self.product_image_label_13 = QLabel(self.product_frame_13)
        self.product_image_label_13.setObjectName(u"product_image_label_13")
        self.product_image_label_13.setMaximumSize(QSize(110, 110))
        self.product_image_label_13.setStyleSheet(u"")
        self.product_image_label_13.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.product_image_label_13.setScaledContents(True)

        self.horizontalLayout_62.addWidget(self.product_image_label_13)

        self.frame_20 = QFrame(self.product_frame_13)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_20)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.product_name_label_9 = QLabel(self.frame_20)
        self.product_name_label_9.setObjectName(u"product_name_label_9")
        sizePolicy2.setHeightForWidth(self.product_name_label_9.sizePolicy().hasHeightForWidth())
        self.product_name_label_9.setSizePolicy(sizePolicy2)
        self.product_name_label_9.setFont(font6)

        self.verticalLayout_53.addWidget(self.product_name_label_9)

        self.buyer_name = QLabel(self.frame_20)
        self.buyer_name.setObjectName(u"buyer_name")
        sizePolicy2.setHeightForWidth(self.buyer_name.sizePolicy().hasHeightForWidth())
        self.buyer_name.setSizePolicy(sizePolicy2)
        self.buyer_name.setFont(font5)

        self.verticalLayout_53.addWidget(self.buyer_name)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_53.addItem(self.verticalSpacer_23)

        self.id_label = QLabel(self.frame_20)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setFont(font10)
        self.id_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_53.addWidget(self.id_label)


        self.horizontalLayout_62.addWidget(self.frame_20)


        self.horizontalLayout_61.addWidget(self.product_frame_13)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setSpacing(10)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.info_frame_13 = QFrame(self.order_box)
        self.info_frame_13.setObjectName(u"info_frame_13")
        self.info_frame_13.setMinimumSize(QSize(0, 0))
        self.info_frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.info_frame_13.setStyleSheet(u"QFrame {\n"
"    background-color:#E8F3F2;\n"
"	border: none;\n"
"}")
        self.info_frame_13.setFrameShape(QFrame.StyledPanel)
        self.info_frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.info_frame_13)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(20, 12, 20, 12)
        self.order_date_label = QLabel(self.info_frame_13)
        self.order_date_label.setObjectName(u"order_date_label")
        self.order_date_label.setFont(font10)

        self.verticalLayout_55.addWidget(self.order_date_label)

        self.mode_label_13 = QLabel(self.info_frame_13)
        self.mode_label_13.setObjectName(u"mode_label_13")
        self.mode_label_13.setFont(font10)

        self.verticalLayout_55.addWidget(self.mode_label_13)

        self.status_label_13 = QLabel(self.info_frame_13)
        self.status_label_13.setObjectName(u"status_label_13")
        self.status_label_13.setFont(font10)

        self.verticalLayout_55.addWidget(self.status_label_13)

        self.price_label_9 = QLabel(self.info_frame_13)
        self.price_label_9.setObjectName(u"price_label_9")
        self.price_label_9.setFont(font10)

        self.verticalLayout_55.addWidget(self.price_label_9)


        self.verticalLayout_54.addWidget(self.info_frame_13)


        self.horizontalLayout_61.addLayout(self.verticalLayout_54)


        self.horizontalLayout_60.addLayout(self.horizontalLayout_61)


        self.verticalLayout_52.addWidget(self.order_box)

        self.order_box_2 = QFrame(self.orders_scrollAreaWidgetContents)
        self.order_box_2.setObjectName(u"order_box_2")
        sizePolicy8.setHeightForWidth(self.order_box_2.sizePolicy().hasHeightForWidth())
        self.order_box_2.setSizePolicy(sizePolicy8)
        self.order_box_2.setMinimumSize(QSize(0, 150))
        self.order_box_2.setMaximumSize(QSize(16777215, 150))
        self.order_box_2.setAutoFillBackground(False)
        self.order_box_2.setFrameShape(QFrame.StyledPanel)
        self.order_box_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.order_box_2)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setSpacing(15)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.product_frame_14 = QFrame(self.order_box_2)
        self.product_frame_14.setObjectName(u"product_frame_14")
        self.product_frame_14.setMinimumSize(QSize(400, 0))
        self.product_frame_14.setMaximumSize(QSize(500, 16777215))
        self.product_frame_14.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"}")
        self.product_frame_14.setFrameShape(QFrame.StyledPanel)
        self.product_frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.product_frame_14)
        self.horizontalLayout_66.setSpacing(15)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(20, 15, 20, 15)
        self.product_image_label_14 = QLabel(self.product_frame_14)
        self.product_image_label_14.setObjectName(u"product_image_label_14")
        self.product_image_label_14.setMaximumSize(QSize(110, 110))
        self.product_image_label_14.setStyleSheet(u"")
        self.product_image_label_14.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.product_image_label_14.setScaledContents(True)

        self.horizontalLayout_66.addWidget(self.product_image_label_14)

        self.frame_21 = QFrame(self.product_frame_14)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_21)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.product_name_label_10 = QLabel(self.frame_21)
        self.product_name_label_10.setObjectName(u"product_name_label_10")
        sizePolicy2.setHeightForWidth(self.product_name_label_10.sizePolicy().hasHeightForWidth())
        self.product_name_label_10.setSizePolicy(sizePolicy2)
        self.product_name_label_10.setFont(font6)

        self.verticalLayout_56.addWidget(self.product_name_label_10)

        self.buyer_name_2 = QLabel(self.frame_21)
        self.buyer_name_2.setObjectName(u"buyer_name_2")
        sizePolicy2.setHeightForWidth(self.buyer_name_2.sizePolicy().hasHeightForWidth())
        self.buyer_name_2.setSizePolicy(sizePolicy2)
        self.buyer_name_2.setFont(font5)

        self.verticalLayout_56.addWidget(self.buyer_name_2)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_56.addItem(self.verticalSpacer_24)

        self.id_label_2 = QLabel(self.frame_21)
        self.id_label_2.setObjectName(u"id_label_2")
        self.id_label_2.setFont(font10)
        self.id_label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_56.addWidget(self.id_label_2)


        self.horizontalLayout_66.addWidget(self.frame_21)


        self.horizontalLayout_65.addWidget(self.product_frame_14)

        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setSpacing(10)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.info_frame_14 = QFrame(self.order_box_2)
        self.info_frame_14.setObjectName(u"info_frame_14")
        self.info_frame_14.setMinimumSize(QSize(0, 0))
        self.info_frame_14.setMaximumSize(QSize(16777215, 16777215))
        self.info_frame_14.setStyleSheet(u"QFrame {\n"
"    background-color:#E8F3F2;\n"
"	border: none;\n"
"}")
        self.info_frame_14.setFrameShape(QFrame.StyledPanel)
        self.info_frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.info_frame_14)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(20, 12, 20, 12)
        self.order_date_label_2 = QLabel(self.info_frame_14)
        self.order_date_label_2.setObjectName(u"order_date_label_2")
        self.order_date_label_2.setFont(font10)

        self.verticalLayout_58.addWidget(self.order_date_label_2)

        self.mode_label_14 = QLabel(self.info_frame_14)
        self.mode_label_14.setObjectName(u"mode_label_14")
        self.mode_label_14.setFont(font10)

        self.verticalLayout_58.addWidget(self.mode_label_14)

        self.status_label_14 = QLabel(self.info_frame_14)
        self.status_label_14.setObjectName(u"status_label_14")
        self.status_label_14.setFont(font10)

        self.verticalLayout_58.addWidget(self.status_label_14)

        self.price_label_10 = QLabel(self.info_frame_14)
        self.price_label_10.setObjectName(u"price_label_10")
        self.price_label_10.setFont(font10)

        self.verticalLayout_58.addWidget(self.price_label_10)


        self.verticalLayout_57.addWidget(self.info_frame_14)


        self.horizontalLayout_65.addLayout(self.verticalLayout_57)


        self.horizontalLayout_64.addLayout(self.horizontalLayout_65)


        self.verticalLayout_52.addWidget(self.order_box_2)

        self.order_box_3 = QFrame(self.orders_scrollAreaWidgetContents)
        self.order_box_3.setObjectName(u"order_box_3")
        sizePolicy8.setHeightForWidth(self.order_box_3.sizePolicy().hasHeightForWidth())
        self.order_box_3.setSizePolicy(sizePolicy8)
        self.order_box_3.setMinimumSize(QSize(0, 150))
        self.order_box_3.setMaximumSize(QSize(16777215, 150))
        self.order_box_3.setAutoFillBackground(False)
        self.order_box_3.setFrameShape(QFrame.StyledPanel)
        self.order_box_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.order_box_3)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setSpacing(15)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.product_frame_15 = QFrame(self.order_box_3)
        self.product_frame_15.setObjectName(u"product_frame_15")
        self.product_frame_15.setMinimumSize(QSize(400, 0))
        self.product_frame_15.setMaximumSize(QSize(500, 16777215))
        self.product_frame_15.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"}")
        self.product_frame_15.setFrameShape(QFrame.StyledPanel)
        self.product_frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.product_frame_15)
        self.horizontalLayout_70.setSpacing(15)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(20, 15, 20, 15)
        self.product_image_label_15 = QLabel(self.product_frame_15)
        self.product_image_label_15.setObjectName(u"product_image_label_15")
        self.product_image_label_15.setMaximumSize(QSize(110, 110))
        self.product_image_label_15.setStyleSheet(u"")
        self.product_image_label_15.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.product_image_label_15.setScaledContents(True)

        self.horizontalLayout_70.addWidget(self.product_image_label_15)

        self.frame_22 = QFrame(self.product_frame_15)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_22)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.product_name_label_11 = QLabel(self.frame_22)
        self.product_name_label_11.setObjectName(u"product_name_label_11")
        sizePolicy2.setHeightForWidth(self.product_name_label_11.sizePolicy().hasHeightForWidth())
        self.product_name_label_11.setSizePolicy(sizePolicy2)
        self.product_name_label_11.setFont(font6)

        self.verticalLayout_59.addWidget(self.product_name_label_11)

        self.buyer_name_3 = QLabel(self.frame_22)
        self.buyer_name_3.setObjectName(u"buyer_name_3")
        sizePolicy2.setHeightForWidth(self.buyer_name_3.sizePolicy().hasHeightForWidth())
        self.buyer_name_3.setSizePolicy(sizePolicy2)
        self.buyer_name_3.setFont(font5)

        self.verticalLayout_59.addWidget(self.buyer_name_3)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_25)

        self.id_label_3 = QLabel(self.frame_22)
        self.id_label_3.setObjectName(u"id_label_3")
        self.id_label_3.setFont(font10)
        self.id_label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_59.addWidget(self.id_label_3)


        self.horizontalLayout_70.addWidget(self.frame_22)


        self.horizontalLayout_69.addWidget(self.product_frame_15)

        self.verticalLayout_60 = QVBoxLayout()
        self.verticalLayout_60.setSpacing(10)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.info_frame_15 = QFrame(self.order_box_3)
        self.info_frame_15.setObjectName(u"info_frame_15")
        self.info_frame_15.setMinimumSize(QSize(0, 0))
        self.info_frame_15.setMaximumSize(QSize(16777215, 16777215))
        self.info_frame_15.setStyleSheet(u"QFrame {\n"
"    background-color:#E8F3F2;\n"
"	border: none;\n"
"}")
        self.info_frame_15.setFrameShape(QFrame.StyledPanel)
        self.info_frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.info_frame_15)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(20, 12, 20, 12)
        self.order_date_label_3 = QLabel(self.info_frame_15)
        self.order_date_label_3.setObjectName(u"order_date_label_3")
        self.order_date_label_3.setFont(font10)

        self.verticalLayout_61.addWidget(self.order_date_label_3)

        self.mode_label_15 = QLabel(self.info_frame_15)
        self.mode_label_15.setObjectName(u"mode_label_15")
        self.mode_label_15.setFont(font10)

        self.verticalLayout_61.addWidget(self.mode_label_15)

        self.status_label_15 = QLabel(self.info_frame_15)
        self.status_label_15.setObjectName(u"status_label_15")
        self.status_label_15.setFont(font10)

        self.verticalLayout_61.addWidget(self.status_label_15)

        self.price_label_11 = QLabel(self.info_frame_15)
        self.price_label_11.setObjectName(u"price_label_11")
        self.price_label_11.setFont(font10)

        self.verticalLayout_61.addWidget(self.price_label_11)


        self.verticalLayout_60.addWidget(self.info_frame_15)


        self.horizontalLayout_69.addLayout(self.verticalLayout_60)


        self.horizontalLayout_68.addLayout(self.horizontalLayout_69)


        self.verticalLayout_52.addWidget(self.order_box_3)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_52.addItem(self.verticalSpacer_27)

        self.orders_scrollArea.setWidget(self.orders_scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.orders_scrollArea)

        self.stackedWidget.addWidget(self.order)
        self.edit_product = QWidget()
        self.edit_product.setObjectName(u"edit_product")
        self.verticalLayout_11 = QVBoxLayout(self.edit_product)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.edit_product)
        self.label_18.setObjectName(u"label_18")
        sizePolicy2.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy2)
        self.label_18.setFont(font4)

        self.verticalLayout_11.addWidget(self.label_18)

        self.frame_23 = QFrame(self.edit_product)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(180, 16777215))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_25)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_11 = QLabel(self.frame_25)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setFont(font6)

        self.verticalLayout_8.addWidget(self.label_11)

        self.label_13 = QLabel(self.frame_25)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setFont(font6)

        self.verticalLayout_8.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_25)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setFont(font6)

        self.verticalLayout_8.addWidget(self.label_14)

        self.label_19 = QLabel(self.frame_25)
        self.label_19.setObjectName(u"label_19")
        sizePolicy2.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy2)
        self.label_19.setFont(font6)

        self.verticalLayout_8.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_25)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        self.label_20.setFont(font6)

        self.verticalLayout_8.addWidget(self.label_20)

        self.label_15 = QLabel(self.frame_25)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setFont(font6)

        self.verticalLayout_8.addWidget(self.label_15)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)


        self.horizontalLayout_12.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_23)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"* {\n"
"	border-radius: 10px;\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_26)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.edit_product_page_name_Edit = QTextEdit(self.frame_26)
        self.edit_product_page_name_Edit.setObjectName(u"edit_product_page_name_Edit")
        sizePolicy3.setHeightForWidth(self.edit_product_page_name_Edit.sizePolicy().hasHeightForWidth())
        self.edit_product_page_name_Edit.setSizePolicy(sizePolicy3)
        self.edit_product_page_name_Edit.setMaximumSize(QSize(16777215, 30))
        self.edit_product_page_name_Edit.setFont(font7)
        self.edit_product_page_name_Edit.setStyleSheet(u"background-color: white")

        self.verticalLayout_9.addWidget(self.edit_product_page_name_Edit)

        self.edit_product_page_price_edit = QTextEdit(self.frame_26)
        self.edit_product_page_price_edit.setObjectName(u"edit_product_page_price_edit")
        sizePolicy3.setHeightForWidth(self.edit_product_page_price_edit.sizePolicy().hasHeightForWidth())
        self.edit_product_page_price_edit.setSizePolicy(sizePolicy3)
        self.edit_product_page_price_edit.setMaximumSize(QSize(16777215, 30))
        self.edit_product_page_price_edit.setFont(font1)
        self.edit_product_page_price_edit.setStyleSheet(u"background-color: white")

        self.verticalLayout_9.addWidget(self.edit_product_page_price_edit)

        self.edit_product__page_tags_edit = QTextEdit(self.frame_26)
        self.edit_product__page_tags_edit.setObjectName(u"edit_product__page_tags_edit")
        sizePolicy3.setHeightForWidth(self.edit_product__page_tags_edit.sizePolicy().hasHeightForWidth())
        self.edit_product__page_tags_edit.setSizePolicy(sizePolicy3)
        self.edit_product__page_tags_edit.setMaximumSize(QSize(16777215, 30))
        self.edit_product__page_tags_edit.setFont(font1)
        self.edit_product__page_tags_edit.setStyleSheet(u"background-color: white")

        self.verticalLayout_9.addWidget(self.edit_product__page_tags_edit)

        self.edit_product_page_mode_combobox = QComboBox(self.frame_26)
        self.edit_product_page_mode_combobox.addItem("")
        self.edit_product_page_mode_combobox.addItem("")
        self.edit_product_page_mode_combobox.setObjectName(u"edit_product_page_mode_combobox")
        font11 = QFont()
        font11.setFamilies([u"Manrope"])
        font11.setPointSize(12)
        font11.setBold(False)
        self.edit_product_page_mode_combobox.setFont(font11)

        self.verticalLayout_9.addWidget(self.edit_product_page_mode_combobox)

        self.edit_product_page_date_edit = QDateEdit(self.frame_26)
        self.edit_product_page_date_edit.setObjectName(u"edit_product_page_date_edit")
        self.edit_product_page_date_edit.setFont(font7)

        self.verticalLayout_9.addWidget(self.edit_product_page_date_edit)

        self.edit_product_page_des_edit = QTextEdit(self.frame_26)
        self.edit_product_page_des_edit.setObjectName(u"edit_product_page_des_edit")
        sizePolicy4.setHeightForWidth(self.edit_product_page_des_edit.sizePolicy().hasHeightForWidth())
        self.edit_product_page_des_edit.setSizePolicy(sizePolicy4)
        self.edit_product_page_des_edit.setFont(font8)
        self.edit_product_page_des_edit.setStyleSheet(u"background-color: white")

        self.verticalLayout_9.addWidget(self.edit_product_page_des_edit)

        self.verticalSpacer_6 = QSpacerItem(253, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_6)


        self.horizontalLayout_12.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_23)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_27)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy2.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy2)
        self.frame_28.setStyleSheet(u"QPushButton {\n"
"    background-color:#58827E;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #4D7672;\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_28)
        self.label_16.setObjectName(u"label_16")
        sizePolicy5.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy5)
        self.label_16.setFont(font6)

        self.horizontalLayout_13.addWidget(self.label_16)

        self.edit_prodcut_page_add_image_button = QPushButton(self.frame_28)
        self.edit_prodcut_page_add_image_button.setObjectName(u"edit_prodcut_page_add_image_button")
        sizePolicy6.setHeightForWidth(self.edit_prodcut_page_add_image_button.sizePolicy().hasHeightForWidth())
        self.edit_prodcut_page_add_image_button.setSizePolicy(sizePolicy6)
        self.edit_prodcut_page_add_image_button.setMinimumSize(QSize(0, 30))
        self.edit_prodcut_page_add_image_button.setMaximumSize(QSize(16777215, 30))
        self.edit_prodcut_page_add_image_button.setFont(font9)

        self.horizontalLayout_13.addWidget(self.edit_prodcut_page_add_image_button)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_16)


        self.verticalLayout_10.addWidget(self.frame_28)

        self.stackedWidget_2 = QStackedWidget(self.frame_27)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMaximumSize(QSize(250, 300))
        self.stackedWidget_2.setStyleSheet(u"QPushButton {\n"
"    background-color:#58827E;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #4D7672;\n"
"}")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_12 = QVBoxLayout(self.page_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.edit_product_page_image_label = QLabel(self.page_3)
        self.edit_product_page_image_label.setObjectName(u"edit_product_page_image_label")
        sizePolicy5.setHeightForWidth(self.edit_product_page_image_label.sizePolicy().hasHeightForWidth())
        self.edit_product_page_image_label.setSizePolicy(sizePolicy5)
        self.edit_product_page_image_label.setMinimumSize(QSize(0, 0))
        self.edit_product_page_image_label.setMaximumSize(QSize(250, 250))
        self.edit_product_page_image_label.setPixmap(QPixmap(u":/post_images/IMG_7107.jpg"))
        self.edit_product_page_image_label.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.edit_product_page_image_label)

        self.edit_product_page_delete_button = QPushButton(self.page_3)
        self.edit_product_page_delete_button.setObjectName(u"edit_product_page_delete_button")
        font12 = QFont()
        font12.setFamilies([u"Manrope"])
        font12.setPointSize(12)
        font12.setBold(True)
        self.edit_product_page_delete_button.setFont(font12)

        self.verticalLayout_12.addWidget(self.edit_product_page_delete_button)

        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_17 = QVBoxLayout(self.page_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.image_label_2 = QLabel(self.page_4)
        self.image_label_2.setObjectName(u"image_label_2")
        sizePolicy5.setHeightForWidth(self.image_label_2.sizePolicy().hasHeightForWidth())
        self.image_label_2.setSizePolicy(sizePolicy5)
        self.image_label_2.setMinimumSize(QSize(0, 0))
        self.image_label_2.setMaximumSize(QSize(250, 250))
        self.image_label_2.setPixmap(QPixmap(u":/post_images/IMG_7105.jpg"))
        self.image_label_2.setScaledContents(True)
        self.image_label_2.setWordWrap(False)

        self.verticalLayout_17.addWidget(self.image_label_2)

        self.delete_button = QPushButton(self.page_4)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setFont(font12)

        self.verticalLayout_17.addWidget(self.delete_button)

        self.stackedWidget_2.addWidget(self.page_4)

        self.verticalLayout_10.addWidget(self.stackedWidget_2)

        self.verticalSpacer_7 = QSpacerItem(20, 205, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_7)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy2.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy2)
        self.frame_29.setStyleSheet(u"QPushButton {\n"
"    background-color:#58827E;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #4D7672;\n"
"}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_14.setSpacing(20)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_17)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)

        self.edit_product_page_save_button = QPushButton(self.frame_29)
        self.edit_product_page_save_button.setObjectName(u"edit_product_page_save_button")
        sizePolicy6.setHeightForWidth(self.edit_product_page_save_button.sizePolicy().hasHeightForWidth())
        self.edit_product_page_save_button.setSizePolicy(sizePolicy6)
        self.edit_product_page_save_button.setMinimumSize(QSize(0, 30))
        self.edit_product_page_save_button.setMaximumSize(QSize(16777215, 30))
        self.edit_product_page_save_button.setFont(font9)

        self.horizontalLayout_14.addWidget(self.edit_product_page_save_button)


        self.verticalLayout_10.addWidget(self.frame_29)


        self.horizontalLayout_12.addWidget(self.frame_27)


        self.verticalLayout_11.addWidget(self.frame_23)

        self.stackedWidget.addWidget(self.edit_product)
        self.edit_collection = QWidget()
        self.edit_collection.setObjectName(u"edit_collection")
        self.verticalLayout_24 = QVBoxLayout(self.edit_collection)
        self.verticalLayout_24.setSpacing(10)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.collection_label_2 = QLabel(self.edit_collection)
        self.collection_label_2.setObjectName(u"collection_label_2")
        sizePolicy2.setHeightForWidth(self.collection_label_2.sizePolicy().hasHeightForWidth())
        self.collection_label_2.setSizePolicy(sizePolicy2)
        self.collection_label_2.setFont(font4)

        self.verticalLayout_24.addWidget(self.collection_label_2)

        self.frame_30 = QFrame(self.edit_collection)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"	border-radius: 25px;\n"
"}")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(180, 16777215))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_31)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_17 = QLabel(self.frame_31)
        self.label_17.setObjectName(u"label_17")
        sizePolicy2.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy2)
        self.label_17.setFont(font6)

        self.verticalLayout_18.addWidget(self.label_17)

        self.label_23 = QLabel(self.frame_31)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)
        self.label_23.setFont(font6)

        self.verticalLayout_18.addWidget(self.label_23)

        self.label_25 = QLabel(self.frame_31)
        self.label_25.setObjectName(u"label_25")
        sizePolicy2.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy2)
        self.label_25.setFont(font6)

        self.verticalLayout_18.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_31)
        self.label_26.setObjectName(u"label_26")
        sizePolicy2.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy2)
        self.label_26.setFont(font6)

        self.verticalLayout_18.addWidget(self.label_26)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_8)

        self.label_28 = QLabel(self.frame_31)
        self.label_28.setObjectName(u"label_28")
        sizePolicy2.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy2)
        self.label_28.setFont(font6)

        self.verticalLayout_18.addWidget(self.label_28)


        self.horizontalLayout_15.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"* {\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color:#58827E;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #4D7672;\n"
"}")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_32)
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.edit_collection_name_edit = QTextEdit(self.frame_32)
        self.edit_collection_name_edit.setObjectName(u"edit_collection_name_edit")
        sizePolicy3.setHeightForWidth(self.edit_collection_name_edit.sizePolicy().hasHeightForWidth())
        self.edit_collection_name_edit.setSizePolicy(sizePolicy3)
        self.edit_collection_name_edit.setMaximumSize(QSize(16777215, 30))
        self.edit_collection_name_edit.setFont(font7)
        self.edit_collection_name_edit.setStyleSheet(u"background-color: white")

        self.verticalLayout_19.addWidget(self.edit_collection_name_edit)

        self.edit_collection_tag_edit = QTextEdit(self.frame_32)
        self.edit_collection_tag_edit.setObjectName(u"edit_collection_tag_edit")
        sizePolicy3.setHeightForWidth(self.edit_collection_tag_edit.sizePolicy().hasHeightForWidth())
        self.edit_collection_tag_edit.setSizePolicy(sizePolicy3)
        self.edit_collection_tag_edit.setMaximumSize(QSize(16777215, 30))
        self.edit_collection_tag_edit.setFont(font1)
        self.edit_collection_tag_edit.setStyleSheet(u"background-color: white")

        self.verticalLayout_19.addWidget(self.edit_collection_tag_edit)

        self.edit_collection_page_date_edit = QDateEdit(self.frame_32)
        self.edit_collection_page_date_edit.setObjectName(u"edit_collection_page_date_edit")
        self.edit_collection_page_date_edit.setFont(font7)

        self.verticalLayout_19.addWidget(self.edit_collection_page_date_edit)

        self.edit_collection_des_edit = QTextEdit(self.frame_32)
        self.edit_collection_des_edit.setObjectName(u"edit_collection_des_edit")
        sizePolicy4.setHeightForWidth(self.edit_collection_des_edit.sizePolicy().hasHeightForWidth())
        self.edit_collection_des_edit.setSizePolicy(sizePolicy4)
        self.edit_collection_des_edit.setFont(font8)
        self.edit_collection_des_edit.setStyleSheet(u"background-color: white")

        self.verticalLayout_19.addWidget(self.edit_collection_des_edit)

        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.spacer)

        self.edit_collection_page_add_product = QPushButton(self.frame_32)
        self.edit_collection_page_add_product.setObjectName(u"edit_collection_page_add_product")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.edit_collection_page_add_product.sizePolicy().hasHeightForWidth())
        self.edit_collection_page_add_product.setSizePolicy(sizePolicy9)
        self.edit_collection_page_add_product.setMinimumSize(QSize(0, 30))
        self.edit_collection_page_add_product.setMaximumSize(QSize(16777215, 30))
        self.edit_collection_page_add_product.setFont(font9)

        self.verticalLayout_19.addWidget(self.edit_collection_page_add_product)


        self.horizontalLayout_15.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_33)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        sizePolicy2.setHeightForWidth(self.frame_34.sizePolicy().hasHeightForWidth())
        self.frame_34.setSizePolicy(sizePolicy2)
        self.frame_34.setStyleSheet(u"QPushButton {\n"
"    background-color:#58827E;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #4D7672;\n"
"}")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_20.setSpacing(20)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_34)
        self.label_27.setObjectName(u"label_27")
        sizePolicy5.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy5)
        self.label_27.setFont(font6)

        self.horizontalLayout_20.addWidget(self.label_27)

        self.edit_collection_add_img_button = QPushButton(self.frame_34)
        self.edit_collection_add_img_button.setObjectName(u"edit_collection_add_img_button")
        sizePolicy6.setHeightForWidth(self.edit_collection_add_img_button.sizePolicy().hasHeightForWidth())
        self.edit_collection_add_img_button.setSizePolicy(sizePolicy6)
        self.edit_collection_add_img_button.setMinimumSize(QSize(0, 30))
        self.edit_collection_add_img_button.setMaximumSize(QSize(16777215, 30))
        self.edit_collection_add_img_button.setFont(font9)

        self.horizontalLayout_20.addWidget(self.edit_collection_add_img_button)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_18)


        self.verticalLayout_20.addWidget(self.frame_34)

        self.stackedWidget_3 = QStackedWidget(self.frame_33)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMaximumSize(QSize(250, 300))
        self.stackedWidget_3.setStyleSheet(u"QPushButton {\n"
"    background-color:#58827E;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #4D7672;\n"
"}")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_21 = QVBoxLayout(self.page_5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.edit_collection_page_pic_label = QLabel(self.page_5)
        self.edit_collection_page_pic_label.setObjectName(u"edit_collection_page_pic_label")
        sizePolicy5.setHeightForWidth(self.edit_collection_page_pic_label.sizePolicy().hasHeightForWidth())
        self.edit_collection_page_pic_label.setSizePolicy(sizePolicy5)
        self.edit_collection_page_pic_label.setMinimumSize(QSize(0, 0))
        self.edit_collection_page_pic_label.setMaximumSize(QSize(250, 250))
        self.edit_collection_page_pic_label.setPixmap(QPixmap(u":/post_images/IMG_7107.jpg"))
        self.edit_collection_page_pic_label.setScaledContents(True)

        self.verticalLayout_21.addWidget(self.edit_collection_page_pic_label)

        self.edit_collection_page_del_button = QPushButton(self.page_5)
        self.edit_collection_page_del_button.setObjectName(u"edit_collection_page_del_button")
        self.edit_collection_page_del_button.setFont(font12)

        self.verticalLayout_21.addWidget(self.edit_collection_page_del_button)

        self.stackedWidget_3.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_22 = QVBoxLayout(self.page_6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.image_label_4 = QLabel(self.page_6)
        self.image_label_4.setObjectName(u"image_label_4")
        sizePolicy5.setHeightForWidth(self.image_label_4.sizePolicy().hasHeightForWidth())
        self.image_label_4.setSizePolicy(sizePolicy5)
        self.image_label_4.setMinimumSize(QSize(0, 0))
        self.image_label_4.setMaximumSize(QSize(250, 250))
        self.image_label_4.setPixmap(QPixmap(u":/post_images/IMG_7105.jpg"))
        self.image_label_4.setScaledContents(True)
        self.image_label_4.setWordWrap(False)

        self.verticalLayout_22.addWidget(self.image_label_4)

        self.delete_button_4 = QPushButton(self.page_6)
        self.delete_button_4.setObjectName(u"delete_button_4")
        self.delete_button_4.setFont(font12)

        self.verticalLayout_22.addWidget(self.delete_button_4)

        self.stackedWidget_3.addWidget(self.page_6)

        self.verticalLayout_20.addWidget(self.stackedWidget_3)

        self.verticalSpacer_11 = QSpacerItem(20, 205, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_11)

        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        sizePolicy2.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy2)
        self.frame_35.setStyleSheet(u"QPushButton {\n"
"    background-color:#58827E;\n"
"	color: white;\n"
"	border-radius: 8px;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #4D7672;\n"
"}")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_21.setSpacing(20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_20)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_4)

        self.edit_collection_page_save_button = QPushButton(self.frame_35)
        self.edit_collection_page_save_button.setObjectName(u"edit_collection_page_save_button")
        sizePolicy6.setHeightForWidth(self.edit_collection_page_save_button.sizePolicy().hasHeightForWidth())
        self.edit_collection_page_save_button.setSizePolicy(sizePolicy6)
        self.edit_collection_page_save_button.setMinimumSize(QSize(0, 30))
        self.edit_collection_page_save_button.setMaximumSize(QSize(16777215, 30))
        self.edit_collection_page_save_button.setFont(font9)

        self.horizontalLayout_21.addWidget(self.edit_collection_page_save_button)


        self.verticalLayout_20.addWidget(self.frame_35)


        self.horizontalLayout_15.addWidget(self.frame_33)


        self.verticalLayout_24.addWidget(self.frame_30)

        self.stackedWidget.addWidget(self.edit_collection)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.search_icon.setText("")
        self.filter_button.setText("")
        self.search_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"tell us what you're looking for...", None))
        self.home_button.setText("")
        self.history_button.setText("")
        self.wishlist_button.setText("")
        self.profile_button.setText("")
        self.page_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">History</span></p></body></html>", None))
        self.curate_label.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"My Store", None))
        self.info_button.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.products_button.setText(QCoreApplication.translate("MainWindow", u"Products", None))
        self.collections_button.setText(QCoreApplication.translate("MainWindow", u"Collections", None))
        self.orders_button.setText(QCoreApplication.translate("MainWindow", u"Orders", None))
        self.reviews_button.setText(QCoreApplication.translate("MainWindow", u"Reviews", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Store Name", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.info_page_name_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Manrope'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sample_name</p></body></html>", None))
        self.info_page_email_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Manrope'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">sample_email</span></p></body></html>", None))
        self.info_page_phone_number_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Manrope'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">sample_phonenumber</span></p></body></html>", None))
        self.info_page_description_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Manrope'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">sample_description</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Store Icon", None))
        self.info_page_edit_button.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.info_page_picture.setText("")
        self.info_page_save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.products_label.setText(QCoreApplication.translate("MainWindow", u"Products", None))
        self.product_page_add_product_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.product_page_all_button.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.product_page_live_button.setText(QCoreApplication.translate("MainWindow", u"Live", None))
        self.product_page_starting_button.setText(QCoreApplication.translate("MainWindow", u"Starting", None))
        self.product_page_completed_button.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.product_image_label.setText("")
        self.product_name_label.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.price_label.setText(QCoreApplication.translate("MainWindow", u"999 B", None))
        self.sale_date_label.setText(QCoreApplication.translate("MainWindow", u"Sale Date: Mon 26 Jan 19:00", None))
        self.mode_label.setText(QCoreApplication.translate("MainWindow", u"Mode:  CF no CC", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Status: Live", None))
        self.view_product_button.setText(QCoreApplication.translate("MainWindow", u"Configure Product", None))
        self.product_image_label_6.setText("")
        self.product_name_label_6.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.price_label_6.setText(QCoreApplication.translate("MainWindow", u"999 B", None))
        self.sale_date_label_6.setText(QCoreApplication.translate("MainWindow", u"Sale Date: Mon 26 Jan 19:00", None))
        self.mode_label_6.setText(QCoreApplication.translate("MainWindow", u"Mode:  CF no CC", None))
        self.status_label_6.setText(QCoreApplication.translate("MainWindow", u"Status: Live", None))
        self.view_product_button_6.setText(QCoreApplication.translate("MainWindow", u"Configure Product", None))
        self.product_image_label_7.setText("")
        self.product_name_label_7.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.price_label_7.setText(QCoreApplication.translate("MainWindow", u"999 B", None))
        self.sale_date_label_7.setText(QCoreApplication.translate("MainWindow", u"Sale Date: Mon 26 Jan 19:00", None))
        self.mode_label_7.setText(QCoreApplication.translate("MainWindow", u"Mode:  CF no CC", None))
        self.status_label_7.setText(QCoreApplication.translate("MainWindow", u"Status: Live", None))
        self.view_product_button_7.setText(QCoreApplication.translate("MainWindow", u"Configure Product", None))
        self.product_image_label_8.setText("")
        self.product_name_label_8.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.price_label_8.setText(QCoreApplication.translate("MainWindow", u"999 B", None))
        self.sale_date_label_8.setText(QCoreApplication.translate("MainWindow", u"Sale Date: Mon 26 Jan 19:00", None))
        self.mode_label_8.setText(QCoreApplication.translate("MainWindow", u"Mode:  CF no CC", None))
        self.status_label_8.setText(QCoreApplication.translate("MainWindow", u"Status: Live", None))
        self.view_product_button_8.setText(QCoreApplication.translate("MainWindow", u"Configure Product", None))
        self.collection_label.setText(QCoreApplication.translate("MainWindow", u"Collections", None))
        self.collection_page_add_collection_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.collection_page_all_button.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.collection_page_live_button.setText(QCoreApplication.translate("MainWindow", u"Live", None))
        self.collection_page_starting_button.setText(QCoreApplication.translate("MainWindow", u"Starting", None))
        self.collection_page_completed_button.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.product_image_label_9.setText("")
        self.collection_name_label.setText(QCoreApplication.translate("MainWindow", u"Collection Name", None))
        self.sale_date_label_9.setText(QCoreApplication.translate("MainWindow", u"Sale Date: Mon 26 Jan 19:00", None))
        self.mode_label_9.setText(QCoreApplication.translate("MainWindow", u"Mode:  CF no CC", None))
        self.status_label_9.setText(QCoreApplication.translate("MainWindow", u"Status: Live", None))
        self.view_product_button_10.setText(QCoreApplication.translate("MainWindow", u"Configure Product", None))
        self.product_image_label_10.setText("")
        self.collection_name_label_2.setText(QCoreApplication.translate("MainWindow", u"Collection Name", None))
        self.sale_date_label_10.setText(QCoreApplication.translate("MainWindow", u"Sale Date: Mon 26 Jan 19:00", None))
        self.mode_label_10.setText(QCoreApplication.translate("MainWindow", u"Mode:  CF no CC", None))
        self.status_label_10.setText(QCoreApplication.translate("MainWindow", u"Status: Live", None))
        self.view_product_button_11.setText(QCoreApplication.translate("MainWindow", u"Configure Product", None))
        self.product_image_label_11.setText("")
        self.collection_name_label_3.setText(QCoreApplication.translate("MainWindow", u"Collection Name", None))
        self.sale_date_label_11.setText(QCoreApplication.translate("MainWindow", u"Sale Date: Mon 26 Jan 19:00", None))
        self.mode_label_11.setText(QCoreApplication.translate("MainWindow", u"Mode:  CF no CC", None))
        self.status_label_11.setText(QCoreApplication.translate("MainWindow", u"Status: Live", None))
        self.view_product_button_12.setText(QCoreApplication.translate("MainWindow", u"Configure Product", None))
        self.order_label.setText(QCoreApplication.translate("MainWindow", u"Orders", None))
        self.order_page_all_button.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.orders_page_unpaid_button.setText(QCoreApplication.translate("MainWindow", u"Unpaid", None))
        self.orders_page_shipping_button.setText(QCoreApplication.translate("MainWindow", u"Shipping", None))
        self.orders_page_completed_button.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.oders_page_cancelled_button.setText(QCoreApplication.translate("MainWindow", u"Cancelled", None))
        self.product_image_label_13.setText("")
        self.product_name_label_9.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.buyer_name.setText(QCoreApplication.translate("MainWindow", u"Buyer: user_name1", None))
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"Order ID: XXXXXXXX", None))
        self.order_date_label.setText(QCoreApplication.translate("MainWindow", u"Order Date: Mon 26 Jan 19:00", None))
        self.mode_label_13.setText(QCoreApplication.translate("MainWindow", u"Mode:  CF no CC", None))
        self.status_label_13.setText(QCoreApplication.translate("MainWindow", u"Status: Unpaid", None))
        self.price_label_9.setText(QCoreApplication.translate("MainWindow", u"Price: 999 B", None))
        self.product_image_label_14.setText("")
        self.product_name_label_10.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.buyer_name_2.setText(QCoreApplication.translate("MainWindow", u"Buyer: user_name1", None))
        self.id_label_2.setText(QCoreApplication.translate("MainWindow", u"Order ID: XXXXXXXX", None))
        self.order_date_label_2.setText(QCoreApplication.translate("MainWindow", u"Order Date: Mon 26 Jan 19:00", None))
        self.mode_label_14.setText(QCoreApplication.translate("MainWindow", u"Mode:  CF no CC", None))
        self.status_label_14.setText(QCoreApplication.translate("MainWindow", u"Status: Unpaid", None))
        self.price_label_10.setText(QCoreApplication.translate("MainWindow", u"Price: 999 B", None))
        self.product_image_label_15.setText("")
        self.product_name_label_11.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.buyer_name_3.setText(QCoreApplication.translate("MainWindow", u"Buyer: user_name1", None))
        self.id_label_3.setText(QCoreApplication.translate("MainWindow", u"Order ID: XXXXXXXX", None))
        self.order_date_label_3.setText(QCoreApplication.translate("MainWindow", u"Order Date: Mon 26 Jan 19:00", None))
        self.mode_label_15.setText(QCoreApplication.translate("MainWindow", u"Mode:  CF no CC", None))
        self.status_label_15.setText(QCoreApplication.translate("MainWindow", u"Status: Unpaid", None))
        self.price_label_11.setText(QCoreApplication.translate("MainWindow", u"Price: 999 B", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Edit Product", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Product Name", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Tags", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Begin Date", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.edit_product_page_name_Edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Manrope'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sample_name</p></body></html>", None))
        self.edit_product_page_price_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Manrope'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">sample_price</span></p></body></html>", None))
        self.edit_product__page_tags_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Manrope'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">sample_tags</span></p></body></html>", None))
        self.edit_product_page_mode_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"cf no cc", None))
        self.edit_product_page_mode_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"bidding", None))

        self.edit_product_page_des_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Manrope'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">sample_description</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Images", None))
        self.edit_prodcut_page_add_image_button.setText(QCoreApplication.translate("MainWindow", u"Add Image", None))
        self.edit_product_page_image_label.setText("")
        self.edit_product_page_delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.image_label_2.setText("")
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.edit_product_page_save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.collection_label_2.setText(QCoreApplication.translate("MainWindow", u"Edit Collection", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Col. Name", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Tags", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Begin Date", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Products", None))
        self.edit_collection_name_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Manrope'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sample_name</p></body></html>", None))
        self.edit_collection_tag_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Manrope'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">sample_tags</span></p></body></html>", None))
        self.edit_collection_des_edit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Manrope'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">sample_description</span></p></body></html>", None))
        self.edit_collection_page_add_product.setText(QCoreApplication.translate("MainWindow", u"Add Products", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Images", None))
        self.edit_collection_add_img_button.setText(QCoreApplication.translate("MainWindow", u"Add Image", None))
        self.edit_collection_page_pic_label.setText("")
        self.edit_collection_page_del_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.image_label_4.setText("")
        self.delete_button_4.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.edit_collection_page_save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

