# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_home.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_HomeForm(object):
    def setupUi(self, HomeForm):
        if not HomeForm.objectName():
            HomeForm.setObjectName(u"HomeForm")
        HomeForm.resize(544, 329)
        HomeForm.setMinimumSize(QSize(544, 329))
        self.verticalLayout = QVBoxLayout(HomeForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.wind = QLabel(HomeForm)
        self.wind.setObjectName(u"wind")
        self.wind.setMaximumSize(QSize(129, 50))

        self.horizontalLayout.addWidget(self.wind)

        self.speed = QLabel(HomeForm)
        self.speed.setObjectName(u"speed")
        self.speed.setMaximumSize(QSize(129, 50))

        self.horizontalLayout.addWidget(self.speed)

        self.post = QLabel(HomeForm)
        self.post.setObjectName(u"post")
        self.post.setMaximumSize(QSize(129, 50))

        self.horizontalLayout.addWidget(self.post)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.MapWebView = QWebEngineView(HomeForm)
        self.MapWebView.setObjectName(u"MapWebView")
        self.MapWebView.setMinimumSize(QSize(401, 281))
        self.MapWebView.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout_2.addWidget(self.MapWebView)

        self.control_box = QGroupBox(HomeForm)
        self.control_box.setObjectName(u"control_box")
        self.control_box.setMinimumSize(QSize(113, 285))
        self.control_box.setMaximumSize(QSize(113, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.control_box)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSlider = QSlider(self.control_box)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMinimumSize(QSize(22, 197))
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_2.addWidget(self.verticalSlider)

        self.label = QLabel(self.control_box)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSlider_2 = QSlider(self.control_box)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setMinimumSize(QSize(22, 197))
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.verticalLayout_3.addWidget(self.verticalSlider_2)

        self.label_2 = QLabel(self.control_box)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.horizontalLayout_2.addWidget(self.control_box)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(HomeForm)

        QMetaObject.connectSlotsByName(HomeForm)
    # setupUi

    def retranslateUi(self, HomeForm):
        HomeForm.setWindowTitle(QCoreApplication.translate("HomeForm", u"Form", None))
        self.wind.setText(QCoreApplication.translate("HomeForm", u"\u73af\u5883\u98ce", None))
        self.speed.setText(QCoreApplication.translate("HomeForm", u"\u822a\u901f", None))
        self.post.setText(QCoreApplication.translate("HomeForm", u"\u59ff\u6001", None))
        self.control_box.setTitle(QCoreApplication.translate("HomeForm", u"\u63a7\u5236\u6a21\u5757", None))
        self.label.setText(QCoreApplication.translate("HomeForm", u"\u5de6\u6cb9\u95e8", None))
        self.label_2.setText(QCoreApplication.translate("HomeForm", u"\u53f3\u6cb9\u95e8", None))
    # retranslateUi

