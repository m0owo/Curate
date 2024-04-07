# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'paying.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from .posts_images_rc import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(503, 540)
        Dialog.setLayoutDirection(Qt.LeftToRight)
        Dialog.setStyleSheet(u"QDialog{\n"
"	background-color: white;\n"
"}")
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 20, 391, 441))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.queue_label = QLabel(self.verticalLayoutWidget)
        self.queue_label.setObjectName(u"queue_label")
        font = QFont()
        font.setFamilies([u"Manrope"])
        font.setPointSize(14)
        font.setBold(True)
        self.queue_label.setFont(font)
        self.queue_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.queue_label)

        self.queue_label_2 = QLabel(self.verticalLayoutWidget)
        self.queue_label_2.setObjectName(u"queue_label_2")
        font1 = QFont()
        font1.setFamilies([u"Manrope"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.queue_label_2.setFont(font1)
        self.queue_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.queue_label_2)

        self.qr_label = QLabel(self.verticalLayoutWidget)
        self.qr_label.setObjectName(u"qr_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qr_label.sizePolicy().hasHeightForWidth())
        self.qr_label.setSizePolicy(sizePolicy)
        self.qr_label.setMinimumSize(QSize(0, 0))
        self.qr_label.setMaximumSize(QSize(16777215, 420))
        self.qr_label.setPixmap(QPixmap(u":/post_images/IMG_7107.jpg"))
        self.qr_label.setScaledContents(True)

        self.verticalLayout.addWidget(self.qr_label)

        self.add_silp_button = QPushButton(Dialog)
        self.add_silp_button.setObjectName(u"add_silp_button")
        self.add_silp_button.setGeometry(QRect(180, 470, 141, 41))
        font2 = QFont()
        font2.setFamilies([u"Manrope"])
        font2.setPointSize(12)
        self.add_silp_button.setFont(font2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.queue_label.setText(QCoreApplication.translate("Dialog", u"You are in the queue", None))
        self.queue_label_2.setText(QCoreApplication.translate("Dialog", u"Please pay within 1 hour making order", None))
        self.qr_label.setText("")
        self.add_silp_button.setText(QCoreApplication.translate("Dialog", u"Add photo", None))
    # retranslateUi

