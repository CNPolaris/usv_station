# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_speed.ui'
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

class Ui_FormSpeed(object):
    def setupUi(self, FormSpeed):
        if not FormSpeed.objectName():
            FormSpeed.setObjectName(u"FormSpeed")
        FormSpeed.resize(400, 300)
        self.SpeedLabel = QLabel(FormSpeed)
        self.SpeedLabel.setObjectName(u"SpeedLabel")
        self.SpeedLabel.setGeometry(QRect(10, 10, 381, 281))

        self.retranslateUi(FormSpeed)

        QMetaObject.connectSlotsByName(FormSpeed)
    # setupUi

    def retranslateUi(self, FormSpeed):
        FormSpeed.setWindowTitle(QCoreApplication.translate("FormSpeed", u"Form", None))
        self.SpeedLabel.setText(QCoreApplication.translate("FormSpeed", u"TextLabel", None))
    # retranslateUi

