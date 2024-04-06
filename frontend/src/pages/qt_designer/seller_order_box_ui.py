# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'seller_order_box.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import post_images_rc
import post_images_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(869, 150)
        Form.setMinimumSize(QSize(0, 150))
        Form.setMaximumSize(QSize(16777215, 150))
        Form.setStyleSheet(u"QWidget {\n"
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
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.product_frame_13 = QFrame(Form)
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
        self.product_image_label = QLabel(self.product_frame_13)
        self.product_image_label.setObjectName(u"product_image_label")
        self.product_image_label.setMaximumSize(QSize(110, 110))
        self.product_image_label.setStyleSheet(u"")
        self.product_image_label.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.product_image_label.setScaledContents(True)

        self.horizontalLayout_62.addWidget(self.product_image_label)

        self.frame_20 = QFrame(self.product_frame_13)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_20)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.product_name = QLabel(self.frame_20)
        self.product_name.setObjectName(u"product_name")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.product_name.sizePolicy().hasHeightForWidth())
        self.product_name.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Manrope"])
        font.setPointSize(16)
        font.setBold(True)
        self.product_name.setFont(font)

        self.verticalLayout_53.addWidget(self.product_name)

        self.buyer_name = QLabel(self.frame_20)
        self.buyer_name.setObjectName(u"buyer_name")
        sizePolicy.setHeightForWidth(self.buyer_name.sizePolicy().hasHeightForWidth())
        self.buyer_name.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Manrope"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.buyer_name.setFont(font1)

        self.verticalLayout_53.addWidget(self.buyer_name)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_53.addItem(self.verticalSpacer_23)

        self.order_id_label = QLabel(self.frame_20)
        self.order_id_label.setObjectName(u"order_id_label")
        font2 = QFont()
        font2.setFamilies([u"Manrope"])
        font2.setPointSize(13)
        font2.setBold(True)
        self.order_id_label.setFont(font2)
        self.order_id_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_53.addWidget(self.order_id_label)


        self.horizontalLayout_62.addWidget(self.frame_20)


        self.horizontalLayout.addWidget(self.product_frame_13)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setSpacing(10)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.info_frame_13 = QFrame(Form)
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
        self.order_date_label.setFont(font2)

        self.verticalLayout_55.addWidget(self.order_date_label)

        self.mode_label = QLabel(self.info_frame_13)
        self.mode_label.setObjectName(u"mode_label")
        self.mode_label.setFont(font2)

        self.verticalLayout_55.addWidget(self.mode_label)

        self.status_label = QLabel(self.info_frame_13)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setFont(font2)

        self.verticalLayout_55.addWidget(self.status_label)

        self.price_label = QLabel(self.info_frame_13)
        self.price_label.setObjectName(u"price_label")
        self.price_label.setFont(font2)

        self.verticalLayout_55.addWidget(self.price_label)


        self.verticalLayout_54.addWidget(self.info_frame_13)


        self.horizontalLayout.addLayout(self.verticalLayout_54)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.product_image_label.setText("")
        self.product_name.setText(QCoreApplication.translate("Form", u"Product Name", None))
        self.buyer_name.setText(QCoreApplication.translate("Form", u"Buyer: user_name1", None))
        self.order_id_label.setText(QCoreApplication.translate("Form", u"Order ID: XXXXXXXX", None))
        self.order_date_label.setText(QCoreApplication.translate("Form", u"Order Date: Mon 26 Jan 19:00", None))
        self.mode_label.setText(QCoreApplication.translate("Form", u"Mode:  CF no CC", None))
        self.status_label.setText(QCoreApplication.translate("Form", u"Status: Unpaid", None))
        self.price_label.setText(QCoreApplication.translate("Form", u"Price: 999 B", None))
    # retranslateUi

