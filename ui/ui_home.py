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
        HomeForm.resize(847, 447)
        HomeForm.setMinimumSize(QSize(555, 400))
        self.verticalLayout = QVBoxLayout(HomeForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.speed_widget = QWidget(HomeForm)
        self.speed_widget.setObjectName(u"speed_widget")
        self.speed_widget.setMinimumSize(QSize(120, 120))
        self.speed_widget.setMaximumSize(QSize(160, 160))

        self.verticalLayout_7.addWidget(self.speed_widget)

        self.post_widget = QWidget(HomeForm)
        self.post_widget.setObjectName(u"post_widget")
        self.post_widget.setMinimumSize(QSize(120, 120))
        self.post_widget.setMaximumSize(QSize(160, 160))

        self.verticalLayout_7.addWidget(self.post_widget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_7)

        self.MapWebView = QWebEngineView(HomeForm)
        self.MapWebView.setObjectName(u"MapWebView")
        self.MapWebView.setMinimumSize(QSize(455, 427))
        self.MapWebView.setUrl(QUrl(u"about:blank"))

        self.horizontalLayout_2.addWidget(self.MapWebView)

        self.control_box = QGroupBox(HomeForm)
        self.control_box.setObjectName(u"control_box")
        self.control_box.setMinimumSize(QSize(200, 0))
        self.control_box.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.control_box)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.connect_tcp_btn = QPushButton(self.control_box)
        self.connect_tcp_btn.setObjectName(u"connect_tcp_btn")
        self.connect_tcp_btn.setMinimumSize(QSize(95, 24))

        self.verticalLayout_6.addWidget(self.connect_tcp_btn)

        self.process_widget = QWidget(self.control_box)
        self.process_widget.setObjectName(u"process_widget")
        self.process_widget.setMinimumSize(QSize(95, 71))
        self.process_layout = QHBoxLayout(self.process_widget)
        self.process_layout.setObjectName(u"process_layout")

        self.verticalLayout_6.addWidget(self.process_widget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.left_side_slider = QSlider(self.control_box)
        self.left_side_slider.setObjectName(u"left_side_slider")
        self.left_side_slider.setMinimumSize(QSize(40, 160))
        self.left_side_slider.setOrientation(Qt.Vertical)

        self.verticalLayout_4.addWidget(self.left_side_slider)

        self.label_3 = QLabel(self.control_box)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(38, 17))
        font = QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.left_slider = QSlider(self.control_box)
        self.left_slider.setObjectName(u"left_slider")
        self.left_slider.setMinimumSize(QSize(40, 160))
        self.left_slider.setOrientation(Qt.Vertical)

        self.verticalLayout_2.addWidget(self.left_slider)

        self.label = QLabel(self.control_box)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(41, 0))
        self.label.setMaximumSize(QSize(41, 17))
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, -1, -1, -1)
        self.right_slider = QSlider(self.control_box)
        self.right_slider.setObjectName(u"right_slider")
        self.right_slider.setMinimumSize(QSize(40, 160))
        self.right_slider.setOrientation(Qt.Vertical)

        self.verticalLayout_3.addWidget(self.right_slider)

        self.label_2 = QLabel(self.control_box)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(41, 0))
        self.label_2.setMaximumSize(QSize(41, 17))
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.right_side_slider = QSlider(self.control_box)
        self.right_side_slider.setObjectName(u"right_side_slider")
        self.right_side_slider.setMinimumSize(QSize(40, 160))
        self.right_side_slider.setOrientation(Qt.Vertical)

        self.verticalLayout_5.addWidget(self.right_side_slider)

        self.label_4 = QLabel(self.control_box)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(38, 17))
        self.label_4.setFont(font)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addWidget(self.control_box)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(HomeForm)

        QMetaObject.connectSlotsByName(HomeForm)
    # setupUi

    def retranslateUi(self, HomeForm):
        HomeForm.setWindowTitle(QCoreApplication.translate("HomeForm", u"Form", None))
        self.control_box.setTitle(QCoreApplication.translate("HomeForm", u"\u63a7\u5236\u6a21\u5757", None))
        self.connect_tcp_btn.setText(QCoreApplication.translate("HomeForm", u"\u6253\u5f00\u8fde\u63a5", None))
        self.label_3.setText(QCoreApplication.translate("HomeForm", u"\u5de6\u4fa7\u63a8", None))
        self.label.setText(QCoreApplication.translate("HomeForm", u"\u5de6\u63a8\u8fdb", None))
        self.label_2.setText(QCoreApplication.translate("HomeForm", u"\u53f3\u63a8\u8fdb", None))
        self.label_4.setText(QCoreApplication.translate("HomeForm", u"\u53f3\u4fa7\u63a8", None))
    # retranslateUi

