# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 278)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(800, 278))
        Widget.setMaximumSize(QSize(800, 278))
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 30, 691, 101))
        self.lineEdit_InputFileLocation = QLineEdit(self.groupBox)
        self.lineEdit_InputFileLocation.setObjectName(u"lineEdit_InputFileLocation")
        self.lineEdit_InputFileLocation.setGeometry(QRect(10, 30, 571, 61))
        self.pushButtonInputImageFile = QPushButton(self.groupBox)
        self.pushButtonInputImageFile.setObjectName(u"pushButtonInputImageFile")
        self.pushButtonInputImageFile.setGeometry(QRect(600, 30, 80, 61))
        self.pushButtonStartConversion = QPushButton(Widget)
        self.pushButtonStartConversion.setObjectName(u"pushButtonStartConversion")
        self.pushButtonStartConversion.setGeometry(QRect(30, 150, 691, 101))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"BMP to STR converter", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Locate the input image file", None))
        self.pushButtonInputImageFile.setText(QCoreApplication.translate("Widget", u"...", None))
        self.pushButtonStartConversion.setText(QCoreApplication.translate("Widget", u"Start conversion!", None))
    # retranslateUi

