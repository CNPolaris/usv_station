# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_video.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_VideoForm(object):
    def setupUi(self, VideoForm):
        if not VideoForm.objectName():
            VideoForm.setObjectName(u"VideoForm")
        VideoForm.resize(538, 326)
        self.horizontalLayout = QHBoxLayout(VideoForm)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.VideoLabel = QLabel(VideoForm)
        self.VideoLabel.setObjectName(u"VideoLabel")
        self.VideoLabel.setMinimumSize(QSize(361, 311))

        self.horizontalLayout.addWidget(self.VideoLabel)

        self.groupBoxVideo = QGroupBox(VideoForm)
        self.groupBoxVideo.setObjectName(u"groupBoxVideo")
        self.groupBoxVideo.setMinimumSize(QSize(161, 121))
        self.groupBoxVideo.setMaximumSize(QSize(161, 121))
        self.gridLayout = QGridLayout(self.groupBoxVideo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.DownButton = QPushButton(self.groupBoxVideo)
        self.DownButton.setObjectName(u"DownButton")

        self.gridLayout.addWidget(self.DownButton, 1, 1, 1, 1)

        self.UpButton = QPushButton(self.groupBoxVideo)
        self.UpButton.setObjectName(u"UpButton")

        self.gridLayout.addWidget(self.UpButton, 1, 0, 1, 1, Qt.AlignVCenter)

        self.LeftButton = QPushButton(self.groupBoxVideo)
        self.LeftButton.setObjectName(u"LeftButton")

        self.gridLayout.addWidget(self.LeftButton, 2, 0, 1, 1)

        self.RightButton = QPushButton(self.groupBoxVideo)
        self.RightButton.setObjectName(u"RightButton")

        self.gridLayout.addWidget(self.RightButton, 2, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBoxVideo)


        self.retranslateUi(VideoForm)

        QMetaObject.connectSlotsByName(VideoForm)
    # setupUi

    def retranslateUi(self, VideoForm):
        VideoForm.setWindowTitle(QCoreApplication.translate("VideoForm", u"Form", None))
        self.VideoLabel.setText(QCoreApplication.translate("VideoForm", u"\u76d1\u63a7", None))
        self.groupBoxVideo.setTitle(QCoreApplication.translate("VideoForm", u"\u4e91\u53f0", None))
        self.DownButton.setText(QCoreApplication.translate("VideoForm", u"down", None))
        self.UpButton.setText(QCoreApplication.translate("VideoForm", u"up", None))
        self.LeftButton.setText(QCoreApplication.translate("VideoForm", u"left", None))
        self.RightButton.setText(QCoreApplication.translate("VideoForm", u"right", None))
    # retranslateUi

