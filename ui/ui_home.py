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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

class Ui_HomeForm(object):
    def setupUi(self, HomeForm):
        if not HomeForm.objectName():
            HomeForm.setObjectName(u"HomeForm")
        HomeForm.resize(965, 447)
        HomeForm.setMinimumSize(QSize(918, 447))
        self.verticalLayout = QVBoxLayout(HomeForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(HomeForm)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(276, 16777215))
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetFixedSize)
        self.post_widget = QWidget(self.groupBox)
        self.post_widget.setObjectName(u"post_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.post_widget.sizePolicy().hasHeightForWidth())
        self.post_widget.setSizePolicy(sizePolicy)
        self.post_widget.setMinimumSize(QSize(200, 100))
        self.post_widget.setMaximumSize(QSize(200, 200))

        self.verticalLayout_8.addWidget(self.post_widget, 0, Qt.AlignHCenter)

        self.speed_widget = QWidget(self.groupBox)
        self.speed_widget.setObjectName(u"speed_widget")
        sizePolicy.setHeightForWidth(self.speed_widget.sizePolicy().hasHeightForWidth())
        self.speed_widget.setSizePolicy(sizePolicy)
        self.speed_widget.setMinimumSize(QSize(200, 100))
        self.speed_widget.setMaximumSize(QSize(200, 200))

        self.verticalLayout_8.addWidget(self.speed_widget, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        font = QFont()
        font.setPointSize(20)
        self.label_12.setFont(font)

        self.gridLayout.addWidget(self.label_12, 5, 2, 1, 1, Qt.AlignHCenter)

        self.lat_value_label = QLabel(self.groupBox)
        self.lat_value_label.setObjectName(u"lat_value_label")

        self.gridLayout.addWidget(self.lat_value_label, 4, 2, 1, 1, Qt.AlignHCenter)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1, Qt.AlignHCenter)

        self.lng_value_label = QLabel(self.groupBox)
        self.lng_value_label.setObjectName(u"lng_value_label")

        self.gridLayout.addWidget(self.lng_value_label, 4, 0, 1, 1, Qt.AlignHCenter)

        self.deg_value_label = QLabel(self.groupBox)
        self.deg_value_label.setObjectName(u"deg_value_label")

        self.gridLayout.addWidget(self.deg_value_label, 2, 2, 1, 1, Qt.AlignHCenter)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 3, 2, 1, 1, Qt.AlignHCenter)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1, Qt.AlignHCenter)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMaximumSize(QSize(200, 200))
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1, Qt.AlignHCenter)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1, Qt.AlignHCenter)

        self.roll_value_label = QLabel(self.groupBox)
        self.roll_value_label.setObjectName(u"roll_value_label")

        self.gridLayout.addWidget(self.roll_value_label, 2, 0, 1, 1, Qt.AlignHCenter)

        self.speed_value_label = QLabel(self.groupBox)
        self.speed_value_label.setObjectName(u"speed_value_label")

        self.gridLayout.addWidget(self.speed_value_label, 6, 0, 1, 1, Qt.AlignHCenter)

        self.direct_value_label = QLabel(self.groupBox)
        self.direct_value_label.setObjectName(u"direct_value_label")

        self.gridLayout.addWidget(self.direct_value_label, 6, 2, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_7.addLayout(self.gridLayout)


        self.horizontalLayout_2.addWidget(self.groupBox)

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
        self.connect_tcp_btn.setStyleSheet(u"color: rgb(255, 255, 255)")

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
        font1 = QFont()
        font1.setPointSize(10)
        self.label_3.setFont(font1)

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
        self.label.setFont(font1)

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
        self.label_2.setFont(font1)

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
        self.label_4.setFont(font1)

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
        self.groupBox.setTitle(QCoreApplication.translate("HomeForm", u"\u822a\u884c\u6570\u636e", None))
        self.label_12.setText(QCoreApplication.translate("HomeForm", u"\u5730\u9762\u822a\u5411", None))
        self.lat_value_label.setText(QCoreApplication.translate("HomeForm", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("HomeForm", u"\u7ecf\u5ea6", None))
        self.lng_value_label.setText(QCoreApplication.translate("HomeForm", u"TextLabel", None))
        self.deg_value_label.setText(QCoreApplication.translate("HomeForm", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("HomeForm", u"\u7eac\u5ea6", None))
        self.label_8.setText(QCoreApplication.translate("HomeForm", u"\u4fef\u4ef0\u89d2", None))
        self.label_5.setText(QCoreApplication.translate("HomeForm", u"\u6a2a\u6eda\u89d2", None))
        self.label_11.setText(QCoreApplication.translate("HomeForm", u"\u5730\u9762\u901f\u7387", None))
        self.roll_value_label.setText(QCoreApplication.translate("HomeForm", u"TextLabel", None))
        self.speed_value_label.setText(QCoreApplication.translate("HomeForm", u"TextLabel", None))
        self.direct_value_label.setText(QCoreApplication.translate("HomeForm", u"TextLabel", None))
        self.control_box.setTitle(QCoreApplication.translate("HomeForm", u"\u63a7\u5236\u6a21\u5757", None))
        self.connect_tcp_btn.setText(QCoreApplication.translate("HomeForm", u"\u6253\u5f00\u8fde\u63a5", None))
        self.label_3.setText(QCoreApplication.translate("HomeForm", u"\u5de6\u4fa7\u63a8", None))
        self.label.setText(QCoreApplication.translate("HomeForm", u"\u5de6\u63a8\u8fdb", None))
        self.label_2.setText(QCoreApplication.translate("HomeForm", u"\u53f3\u63a8\u8fdb", None))
        self.label_4.setText(QCoreApplication.translate("HomeForm", u"\u53f3\u4fa7\u63a8", None))
    # retranslateUi

