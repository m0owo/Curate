# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'collection.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
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
        self.path_label = QLabel(self.centralwidget)
        self.path_label.setObjectName(u"path_label")
        self.path_label.setGeometry(QRect(60, 110, 591, 61))
        font4 = QFont()
        font4.setFamilies([u"Manrope"])
        font4.setPointSize(20)
        font4.setBold(True)
        self.path_label.setFont(font4)
        self.path_label.setStyleSheet(u"QLabel {\n"
"	color: #8C237C;\n"
"}")
        self.path_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.product_frame = QFrame(self.centralwidget)
        self.product_frame.setObjectName(u"product_frame")
        self.product_frame.setGeometry(QRect(60, 170, 1080, 420))
        self.product_frame.setMinimumSize(QSize(1080, 420))
        self.product_frame.setMaximumSize(QSize(16777215, 0))
        self.product_frame.setStyleSheet(u"Line {\n"
"	background-color: #CCCCCC;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.product_frame)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, 0)
        self.stackedWidget = QStackedWidget(self.product_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(550, 16777215))
        self.stackedWidget.setStyleSheet(u"")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_7 = QHBoxLayout(self.page_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.image_label = QLabel(self.page_3)
        self.image_label.setObjectName(u"image_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy1)
        self.image_label.setMinimumSize(QSize(0, 0))
        self.image_label.setMaximumSize(QSize(16777215, 420))
        self.image_label.setPixmap(QPixmap(u":/post_images/IMG_7107.jpg"))
        self.image_label.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.image_label)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_8 = QHBoxLayout(self.page_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.image_label_2 = QLabel(self.page_4)
        self.image_label_2.setObjectName(u"image_label_2")
        sizePolicy1.setHeightForWidth(self.image_label_2.sizePolicy().hasHeightForWidth())
        self.image_label_2.setSizePolicy(sizePolicy1)
        self.image_label_2.setMinimumSize(QSize(0, 0))
        self.image_label_2.setMaximumSize(QSize(16777215, 420))
        self.image_label_2.setPixmap(QPixmap(u":/post_images/IMG_7105.jpg"))
        self.image_label_2.setScaledContents(True)
        self.image_label_2.setWordWrap(False)

        self.horizontalLayout_8.addWidget(self.image_label_2)

        self.stackedWidget.addWidget(self.page_4)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.frame_3 = QFrame(self.product_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, 0, 0)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Manrope"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	color: #8C237C\n"
"}")

        self.verticalLayout.addWidget(self.label_2)

        self.name_label = QLabel(self.frame_3)
        self.name_label.setObjectName(u"name_label")
        sizePolicy2.setHeightForWidth(self.name_label.sizePolicy().hasHeightForWidth())
        self.name_label.setSizePolicy(sizePolicy2)
        self.name_label.setFont(font4)

        self.verticalLayout.addWidget(self.name_label)

        self.line = QFrame(self.frame_3)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 2))
        self.line.setAutoFillBackground(False)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	color: #8C237C\n"
"}")

        self.verticalLayout.addWidget(self.label_4)

        self.tags_frame = QFrame(self.frame_3)
        self.tags_frame.setObjectName(u"tags_frame")
        sizePolicy2.setHeightForWidth(self.tags_frame.sizePolicy().hasHeightForWidth())
        self.tags_frame.setSizePolicy(sizePolicy2)
        self.tags_frame.setMaximumSize(QSize(16777215, 40))
        self.tags_frame.setStyleSheet(u"QPushButton {\n"
"	background-color: #FFFFFF;\n"
"    border-radius: 10px;\n"
"    border: solid;\n"
"    border-width: 1px;\n"
"    border-color:rgb(154, 152, 148);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #CCCCCC;\n"
"}")
        self.tags_frame.setFrameShape(QFrame.StyledPanel)
        self.tags_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.tags_frame)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 5)
        self.pushButton = QPushButton(self.tags_frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(0, 0))
        font6 = QFont()
        font6.setFamilies([u"Manrope"])
        font6.setPointSize(12)
        self.pushButton.setFont(font6)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.tags_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(0, 0))
        self.pushButton_2.setFont(font6)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.tags_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setMinimumSize(QSize(0, 0))
        self.pushButton_3.setFont(font6)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.tags_frame)

        self.line_2 = QFrame(self.frame_3)
        self.line_2.setObjectName(u"line_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy3)
        self.line_2.setMaximumSize(QSize(16777215, 2))
        self.line_2.setAutoFillBackground(False)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"QLabel {\n"
"	color: #8C237C\n"
"}")

        self.verticalLayout.addWidget(self.label_5)

        self.date_label = QLabel(self.frame_3)
        self.date_label.setObjectName(u"date_label")
        sizePolicy2.setHeightForWidth(self.date_label.sizePolicy().hasHeightForWidth())
        self.date_label.setSizePolicy(sizePolicy2)
        self.date_label.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setFamilies([u"Manrope"])
        font7.setPointSize(12)
        font7.setBold(False)
        self.date_label.setFont(font7)

        self.verticalLayout.addWidget(self.date_label)

        self.mode_label = QLabel(self.frame_3)
        self.mode_label.setObjectName(u"mode_label")
        sizePolicy2.setHeightForWidth(self.mode_label.sizePolicy().hasHeightForWidth())
        self.mode_label.setSizePolicy(sizePolicy2)
        self.mode_label.setMaximumSize(QSize(16777215, 16777215))
        self.mode_label.setFont(font7)

        self.verticalLayout.addWidget(self.mode_label)

        self.description_label = QLabel(self.frame_3)
        self.description_label.setObjectName(u"description_label")
        sizePolicy1.setHeightForWidth(self.description_label.sizePolicy().hasHeightForWidth())
        self.description_label.setSizePolicy(sizePolicy1)
        self.description_label.setMaximumSize(QSize(16777215, 16777215))
        self.description_label.setFont(font7)
        self.description_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.description_label)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        self.frame_5.setStyleSheet(u"QPushButton {\n"
"	background-color: #FFFFFF;\n"
"    border-radius: 10px;\n"
"    border: solid;\n"
"    border-width: 1px;\n"
"    border-color:rgb(154, 152, 148);\n"
"}\n"
"\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #CCCCCC;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.wishlist_button_2 = QPushButton(self.frame_5)
        self.wishlist_button_2.setObjectName(u"wishlist_button_2")
        sizePolicy1.setHeightForWidth(self.wishlist_button_2.sizePolicy().hasHeightForWidth())
        self.wishlist_button_2.setSizePolicy(sizePolicy1)
        self.wishlist_button_2.setMinimumSize(QSize(0, 0))
        font8 = QFont()
        font8.setFamilies([u"Manrope"])
        font8.setPointSize(14)
        self.wishlist_button_2.setFont(font8)

        self.horizontalLayout_3.addWidget(self.wishlist_button_2)

        self.products_button = QPushButton(self.frame_5)
        self.products_button.setObjectName(u"products_button")
        sizePolicy1.setHeightForWidth(self.products_button.sizePolicy().hasHeightForWidth())
        self.products_button.setSizePolicy(sizePolicy1)
        self.products_button.setMinimumSize(QSize(0, 0))
        self.products_button.setFont(font8)

        self.horizontalLayout_3.addWidget(self.products_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame_3)

        self.shop_frame = QFrame(self.centralwidget)
        self.shop_frame.setObjectName(u"shop_frame")
        self.shop_frame.setGeometry(QRect(60, 610, 1080, 140))
        self.shop_frame.setMinimumSize(QSize(1080, 140))
        self.shop_frame.setMaximumSize(QSize(16777215, 140))
        font9 = QFont()
        font9.setBold(False)
        self.shop_frame.setFont(font9)
        self.shop_frame.setStyleSheet(u"#shop_frame {\n"
"	border-radius: 10px;\n"
"    border: solid;\n"
"    border-width: 1px;\n"
"    border-color:rgb(154, 152, 148)\n"
"}\n"
"\n"
"Line {\n"
"	background-color: #CCCCCC;\n"
"}")
        self.shop_frame.setFrameShape(QFrame.StyledPanel)
        self.shop_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.shop_frame)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.frame_6 = QFrame(self.shop_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(100, 100))
        self.label_9.setMaximumSize(QSize(100, 100))
        self.label_9.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.store_name_label = QLabel(self.frame_8)
        self.store_name_label.setObjectName(u"store_name_label")
        sizePolicy2.setHeightForWidth(self.store_name_label.sizePolicy().hasHeightForWidth())
        self.store_name_label.setSizePolicy(sizePolicy2)
        self.store_name_label.setMaximumSize(QSize(16777215, 16777215))
        font10 = QFont()
        font10.setFamilies([u"Manrope"])
        font10.setPointSize(18)
        font10.setBold(True)
        self.store_name_label.setFont(font10)
        self.store_name_label.setStyleSheet(u"QLabel {\n"
"	color: #8C237C\n"
"}")
        self.store_name_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.store_name_label)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy2.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy2)
        self.frame_9.setMaximumSize(QSize(16777215, 40))
        self.frame_9.setStyleSheet(u"QPushButton {\n"
"	background-color: #FFFFFF;\n"
"    border-radius: 10px;\n"
"    border: solid;\n"
"    border-width: 1px;\n"
"    border-color:rgb(154, 152, 148)\n"
"}\n"
"\n"
"\n"
"QPushButton::hover {\n"
"	background-color: #CCCCCC;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.contact_button = QPushButton(self.frame_9)
        self.contact_button.setObjectName(u"contact_button")
        sizePolicy1.setHeightForWidth(self.contact_button.sizePolicy().hasHeightForWidth())
        self.contact_button.setSizePolicy(sizePolicy1)
        self.contact_button.setMinimumSize(QSize(0, 0))
        self.contact_button.setFont(font8)

        self.horizontalLayout_6.addWidget(self.contact_button)

        self.visit_shop_button = QPushButton(self.frame_9)
        self.visit_shop_button.setObjectName(u"visit_shop_button")
        sizePolicy1.setHeightForWidth(self.visit_shop_button.sizePolicy().hasHeightForWidth())
        self.visit_shop_button.setSizePolicy(sizePolicy1)
        self.visit_shop_button.setMinimumSize(QSize(0, 0))
        self.visit_shop_button.setFont(font8)

        self.horizontalLayout_6.addWidget(self.visit_shop_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addWidget(self.frame_9)


        self.horizontalLayout_5.addWidget(self.frame_8)


        self.horizontalLayout_4.addWidget(self.frame_6)

        self.line_3 = QFrame(self.shop_frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(2, 0))
        self.line_3.setAutoFillBackground(False)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_3)

        self.frame_7 = QFrame(self.shop_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.jion_date_label = QLabel(self.frame_7)
        self.jion_date_label.setObjectName(u"jion_date_label")
        sizePolicy2.setHeightForWidth(self.jion_date_label.sizePolicy().hasHeightForWidth())
        self.jion_date_label.setSizePolicy(sizePolicy2)
        self.jion_date_label.setMaximumSize(QSize(16777215, 16777215))
        font11 = QFont()
        font11.setFamilies([u"Manrope"])
        font11.setPointSize(14)
        font11.setBold(False)
        self.jion_date_label.setFont(font11)

        self.gridLayout_2.addWidget(self.jion_date_label, 2, 0, 1, 1)

        self.follower_label = QLabel(self.frame_7)
        self.follower_label.setObjectName(u"follower_label")
        sizePolicy2.setHeightForWidth(self.follower_label.sizePolicy().hasHeightForWidth())
        self.follower_label.setSizePolicy(sizePolicy2)
        self.follower_label.setMaximumSize(QSize(16777215, 16777215))
        self.follower_label.setFont(font11)

        self.gridLayout_2.addWidget(self.follower_label, 0, 0, 1, 1)

        self.col_count_label = QLabel(self.frame_7)
        self.col_count_label.setObjectName(u"col_count_label")
        sizePolicy2.setHeightForWidth(self.col_count_label.sizePolicy().hasHeightForWidth())
        self.col_count_label.setSizePolicy(sizePolicy2)
        self.col_count_label.setMaximumSize(QSize(16777215, 16777215))
        self.col_count_label.setFont(font11)

        self.gridLayout_2.addWidget(self.col_count_label, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_7)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


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
        self.path_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">Home &gt; Collection_name</span></p></body></html>", None))
        self.image_label.setText("")
        self.image_label_2.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Collection", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Collection_name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tags", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"tag_1", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"tag_2", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"tag_3", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"Sale Begins: Mon 26 Jan 19:00", None))
        self.mode_label.setText(QCoreApplication.translate("MainWindow", u"Mode: CF NO CC", None))
        self.description_label.setText(QCoreApplication.translate("MainWindow", u"Description: awooooooooooooooo ga", None))
        self.wishlist_button_2.setText(QCoreApplication.translate("MainWindow", u"Add to Wishlist", None))
        self.products_button.setText(QCoreApplication.translate("MainWindow", u"View All Products", None))
        self.label_9.setText("")
        self.store_name_label.setText(QCoreApplication.translate("MainWindow", u"store_name", None))
        self.contact_button.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.visit_shop_button.setText(QCoreApplication.translate("MainWindow", u"Visit Shop", None))
        self.jion_date_label.setText(QCoreApplication.translate("MainWindow", u"Joined:  20/03/24", None))
        self.follower_label.setText(QCoreApplication.translate("MainWindow", u"Followers:  2", None))
        self.col_count_label.setText(QCoreApplication.translate("MainWindow", u"Collections:  71", None))
    # retranslateUi

