# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_box.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from .icons_rc import *
from .delivery_rc import *
from .logo_rc import *
from .posts_images_rc import *

class Ui_HistoryBox(object):
    def setupUi(self, HistoryBox):
        if not HistoryBox.objectName():
            HistoryBox.setObjectName(u"HistoryBox")
        HistoryBox.resize(925, 260)
        self.horizontalLayout = QHBoxLayout(HistoryBox)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.product_frame = QFrame(HistoryBox)
        self.product_frame.setObjectName(u"product_frame")
        self.product_frame.setMinimumSize(QSize(500, 0))
        self.product_frame.setMaximumSize(QSize(500, 16777215))
        self.product_frame.setStyleSheet(u"QFrame {\n"
"    background-color:#DFF1EE;\n"
"	border: none;\n"
"}")
        self.product_frame.setFrameShape(QFrame.StyledPanel)
        self.product_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.product_frame)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.product_image_label = QLabel(self.product_frame)
        self.product_image_label.setObjectName(u"product_image_label")
        self.product_image_label.setMaximumSize(QSize(200, 200))
        self.product_image_label.setStyleSheet(u"")
        self.product_image_label.setPixmap(QPixmap(u":/post_images/IMG_7102.jpg"))
        self.product_image_label.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.product_image_label)

        self.frame_5 = QFrame(self.product_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.product_name_label = QLabel(self.frame_5)
        self.product_name_label.setObjectName(u"product_name_label")
        font = QFont()
        font.setFamilies([u"Manrope"])
        font.setPointSize(16)
        font.setBold(True)
        self.product_name_label.setFont(font)

        self.verticalLayout.addWidget(self.product_name_label)

        self.order_id_label = QLabel(self.frame_5)
        self.order_id_label.setObjectName(u"order_id_label")
        font1 = QFont()
        font1.setFamilies([u"Manrope"])
        font1.setPointSize(12)
        self.order_id_label.setFont(font1)

        self.verticalLayout.addWidget(self.order_id_label)

        self.verticalSpacer_3 = QSpacerItem(20, 92, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.price_label = QLabel(self.frame_5)
        self.price_label.setObjectName(u"price_label")
        font2 = QFont()
        font2.setFamilies([u"Manrope"])
        font2.setPointSize(24)
        font2.setBold(True)
        self.price_label.setFont(font2)
        self.price_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.price_label)


        self.horizontalLayout_7.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.product_frame)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.status_frame = QFrame(HistoryBox)
        self.status_frame.setObjectName(u"status_frame")
        self.status_frame.setMinimumSize(QSize(0, 120))
        self.status_frame.setMaximumSize(QSize(16777215, 120))
        self.status_frame.setStyleSheet(u"QFrame {\n"
"    background-color:#E8F3F2;\n"
"	border: none;\n"
"}")
        self.status_frame.setFrameShape(QFrame.StyledPanel)
        self.status_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.status_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pay_label = QLabel(self.status_frame)
        self.pay_label.setObjectName(u"pay_label")
        self.pay_label.setMaximumSize(QSize(80, 80))
        self.pay_label.setPixmap(QPixmap(u":/delivery_icons/pay.png"))
        self.pay_label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.pay_label)

        self.deliver_label = QLabel(self.status_frame)
        self.deliver_label.setObjectName(u"deliver_label")
        self.deliver_label.setMaximumSize(QSize(85, 85))
        self.deliver_label.setPixmap(QPixmap(u":/delivery_icons/delivery.png"))
        self.deliver_label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.deliver_label)

        self.arrived_label = QLabel(self.status_frame)
        self.arrived_label.setObjectName(u"arrived_label")
        self.arrived_label.setMinimumSize(QSize(0, 0))
        self.arrived_label.setMaximumSize(QSize(65, 65))
        self.arrived_label.setPixmap(QPixmap(u":/delivery_icons/arrived.png"))
        self.arrived_label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.arrived_label)

        self.cancelled_label = QLabel(self.status_frame)
        self.cancelled_label.setObjectName(u"cancelled_label")
        self.cancelled_label.setMaximumSize(QSize(60, 60))
        self.cancelled_label.setPixmap(QPixmap(u":/delivery_icons/cancelled.png"))
        self.cancelled_label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.cancelled_label)


        self.verticalLayout_2.addWidget(self.status_frame)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.status_label = QLabel(HistoryBox)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setFont(font)
        self.status_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.status_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.view_order_button = QPushButton(HistoryBox)
        self.view_order_button.setObjectName(u"view_order_button")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_order_button.sizePolicy().hasHeightForWidth())
        self.view_order_button.setSizePolicy(sizePolicy)
        self.view_order_button.setMinimumSize(QSize(0, 40))
        font3 = QFont()
        font3.setFamilies([u"Manrope"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.view_order_button.setFont(font3)

        self.horizontalLayout_6.addWidget(self.view_order_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(HistoryBox)

        QMetaObject.connectSlotsByName(HistoryBox)
    # setupUi

    def retranslateUi(self, HistoryBox):
        HistoryBox.setWindowTitle(QCoreApplication.translate("HistoryBox", u"Form", None))
        self.product_image_label.setText("")
        self.product_name_label.setText(QCoreApplication.translate("HistoryBox", u"Product Name", None))
        self.order_id_label.setText(QCoreApplication.translate("HistoryBox", u"Order ID: xxxxxxxxxxxx", None))
        self.price_label.setText(QCoreApplication.translate("HistoryBox", u"999 B", None))
        self.pay_label.setText("")
        self.deliver_label.setText("")
        self.arrived_label.setText("")
        self.cancelled_label.setText("")
        self.status_label.setText(QCoreApplication.translate("HistoryBox", u"Status: To Pay", None))
        self.view_order_button.setText(QCoreApplication.translate("HistoryBox", u"View Order", None))
    # retranslateUi

