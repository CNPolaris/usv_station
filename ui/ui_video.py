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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_VideoForm(object):
    def setupUi(self, VideoForm):
        if not VideoForm.objectName():
            VideoForm.setObjectName(u"VideoForm")
        VideoForm.resize(400, 300)
        self.label = QLabel(VideoForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 150, 54, 16))

        self.retranslateUi(VideoForm)

        QMetaObject.connectSlotsByName(VideoForm)
    # setupUi

    def retranslateUi(self, VideoForm):
        VideoForm.setWindowTitle(QCoreApplication.translate("VideoForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("VideoForm", u"\u76d1\u63a7", None))
    # retranslateUi

