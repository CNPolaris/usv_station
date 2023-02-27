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
    QPushButton, QSizePolicy, QSlider, QVBoxLayout,
    QWidget)

class Ui_HomeForm(object):
    def setupUi(self, HomeForm):
        if not HomeForm.objectName():
            HomeForm.setObjectName(u"HomeForm")
        HomeForm.resize(558, 377)
        HomeForm.setMinimumSize(QSize(530, 300))
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
        self.MapWebView.setMinimumSize(QSize(393, 281))
        self.MapWebView.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout_2.addWidget(self.MapWebView)

        self.control_box = QGroupBox(HomeForm)
        self.control_box.setObjectName(u"control_box")
        self.control_box.setMinimumSize(QSize(113, 285))
        self.control_box.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.control_box)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.connect_tcp_btn = QPushButton(self.control_box)
        self.connect_tcp_btn.setObjectName(u"connect_tcp_btn")
        self.connect_tcp_btn.setMinimumSize(QSize(95, 24))

        self.verticalLayout_4.addWidget(self.connect_tcp_btn)

        self.process_widget = QWidget(self.control_box)
        self.process_widget.setObjectName(u"process_widget")
        self.process_widget.setMinimumSize(QSize(95, 71))
        self.process_layout = QHBoxLayout(self.process_widget)
        self.process_layout.setObjectName(u"process_layout")

        self.verticalLayout_4.addWidget(self.process_widget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.left_slider = QSlider(self.control_box)
        self.left_slider.setObjectName(u"left_slider")
        self.left_slider.setMinimumSize(QSize(41, 160))
        self.left_slider.setOrientation(Qt.Vertical)

        self.verticalLayout_2.addWidget(self.left_slider)

        self.label = QLabel(self.control_box)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(41, 0))

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.right_slider = QSlider(self.control_box)
        self.right_slider.setObjectName(u"right_slider")
        self.right_slider.setMinimumSize(QSize(41, 160))
        self.right_slider.setOrientation(Qt.Vertical)

        self.verticalLayout_3.addWidget(self.right_slider)

        self.label_2 = QLabel(self.control_box)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(41, 0))

        self.verticalLayout_3.addWidget(self.label_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


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
        self.connect_tcp_btn.setText(QCoreApplication.translate("HomeForm", u"\u6253\u5f00\u8fde\u63a5", None))
        self.label.setText(QCoreApplication.translate("HomeForm", u"\u5de6\u6cb9\u95e8", None))
        self.label_2.setText(QCoreApplication.translate("HomeForm", u"\u53f3\u6cb9\u95e8", None))
    # retranslateUi

