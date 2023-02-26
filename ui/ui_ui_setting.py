# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_SettingForm(object):
    def setupUi(self, SettingForm):
        if not SettingForm.objectName():
            SettingForm.setObjectName(u"SettingForm")
        SettingForm.resize(542, 328)
        SettingForm.setMinimumSize(QSize(542, 328))
        SettingForm.setMaximumSize(QSize(542, 328))
        self.verticalLayout = QVBoxLayout(SettingForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.server_setting_box = QGroupBox(SettingForm)
        self.server_setting_box.setObjectName(u"server_setting_box")
        self.server_setting_box.setMaximumSize(QSize(524, 152))
        self.verticalLayout_2 = QVBoxLayout(self.server_setting_box)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.server_ip_label = QLabel(self.server_setting_box)
        self.server_ip_label.setObjectName(u"server_ip_label")
        self.server_ip_label.setMinimumSize(QSize(47, 16))
        self.server_ip_label.setMaximumSize(QSize(47, 16))

        self.horizontalLayout.addWidget(self.server_ip_label)

        self.server_ip_text = QTextEdit(self.server_setting_box)
        self.server_ip_text.setObjectName(u"server_ip_text")
        self.server_ip_text.setMinimumSize(QSize(191, 31))
        self.server_ip_text.setMaximumSize(QSize(191, 31))
        self.server_ip_text.setReadOnly(False)
        self.server_ip_text.setOverwriteMode(False)
        self.server_ip_text.setAcceptRichText(False)

        self.horizontalLayout.addWidget(self.server_ip_text)

        self.server_port_label = QLabel(self.server_setting_box)
        self.server_port_label.setObjectName(u"server_port_label")
        self.server_port_label.setMinimumSize(QSize(31, 16))
        self.server_port_label.setMaximumSize(QSize(31, 16))

        self.horizontalLayout.addWidget(self.server_port_label)

        self.server_port_text = QTextEdit(self.server_setting_box)
        self.server_port_text.setObjectName(u"server_port_text")
        self.server_port_text.setMinimumSize(QSize(81, 31))
        self.server_port_text.setMaximumSize(QSize(81, 31))

        self.horizontalLayout.addWidget(self.server_port_text)

        self.override_server_info = QCheckBox(self.server_setting_box)
        self.override_server_info.setObjectName(u"override_server_info")
        self.override_server_info.setMinimumSize(QSize(80, 20))
        self.override_server_info.setMaximumSize(QSize(80, 20))

        self.horizontalLayout.addWidget(self.override_server_info)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.monitor_push_label = QLabel(self.server_setting_box)
        self.monitor_push_label.setObjectName(u"monitor_push_label")
        self.monitor_push_label.setMaximumSize(QSize(81, 16))

        self.horizontalLayout_2.addWidget(self.monitor_push_label)

        self.monitor_url_text = QTextEdit(self.server_setting_box)
        self.monitor_url_text.setObjectName(u"monitor_url_text")
        self.monitor_url_text.setMinimumSize(QSize(331, 31))
        self.monitor_url_text.setMaximumSize(QSize(331, 31))

        self.horizontalLayout_2.addWidget(self.monitor_url_text)

        self.override_monitor_url = QCheckBox(self.server_setting_box)
        self.override_monitor_url.setObjectName(u"override_monitor_url")
        self.override_monitor_url.setMinimumSize(QSize(80, 20))
        self.override_monitor_url.setMaximumSize(QSize(80, 20))

        self.horizontalLayout_2.addWidget(self.override_monitor_url)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.monitor_code_label = QLabel(self.server_setting_box)
        self.monitor_code_label.setObjectName(u"monitor_code_label")
        self.monitor_code_label.setMinimumSize(QSize(71, 16))
        self.monitor_code_label.setMaximumSize(QSize(71, 16))

        self.horizontalLayout_3.addWidget(self.monitor_code_label)

        self.monitor_code_text = QTextEdit(self.server_setting_box)
        self.monitor_code_text.setObjectName(u"monitor_code_text")
        self.monitor_code_text.setMinimumSize(QSize(331, 31))
        self.monitor_code_text.setMaximumSize(QSize(331, 31))

        self.horizontalLayout_3.addWidget(self.monitor_code_text)

        self.override_monitor_code = QCheckBox(self.server_setting_box)
        self.override_monitor_code.setObjectName(u"override_monitor_code")
        self.override_monitor_code.setMinimumSize(QSize(80, 20))
        self.override_monitor_code.setMaximumSize(QSize(80, 20))

        self.horizontalLayout_3.addWidget(self.override_monitor_code)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.server_setting_box)

        self.dtu_setting_box = QGroupBox(SettingForm)
        self.dtu_setting_box.setObjectName(u"dtu_setting_box")
        self.dtu_setting_box.setMaximumSize(QSize(524, 152))
        self.verticalLayout_3 = QVBoxLayout(self.dtu_setting_box)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.register_label = QLabel(self.dtu_setting_box)
        self.register_label.setObjectName(u"register_label")
        self.register_label.setMinimumSize(QSize(53, 16))
        self.register_label.setMaximumSize(QSize(53, 16))

        self.horizontalLayout_4.addWidget(self.register_label)

        self.access_key_text = QTextEdit(self.dtu_setting_box)
        self.access_key_text.setObjectName(u"access_key_text")
        self.access_key_text.setMinimumSize(QSize(331, 90))
        self.access_key_text.setMaximumSize(QSize(331, 90))

        self.horizontalLayout_4.addWidget(self.access_key_text)

        self.override_access_key = QCheckBox(self.dtu_setting_box)
        self.override_access_key.setObjectName(u"override_access_key")
        self.override_access_key.setMinimumSize(QSize(80, 20))
        self.override_access_key.setMaximumSize(QSize(80, 20))

        self.horizontalLayout_4.addWidget(self.override_access_key)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.dtu_setting_box)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.reset_cfg_btn = QPushButton(SettingForm)
        self.reset_cfg_btn.setObjectName(u"reset_cfg_btn")
        self.reset_cfg_btn.setMinimumSize(QSize(75, 24))
        self.reset_cfg_btn.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_5.addWidget(self.reset_cfg_btn)

        self.save_cfg_btn = QPushButton(SettingForm)
        self.save_cfg_btn.setObjectName(u"save_cfg_btn")
        self.save_cfg_btn.setMinimumSize(QSize(75, 24))
        self.save_cfg_btn.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_5.addWidget(self.save_cfg_btn)

        self.cancel_cfg_btn = QPushButton(SettingForm)
        self.cancel_cfg_btn.setObjectName(u"cancel_cfg_btn")
        self.cancel_cfg_btn.setMinimumSize(QSize(75, 24))
        self.cancel_cfg_btn.setMaximumSize(QSize(75, 24))

        self.horizontalLayout_5.addWidget(self.cancel_cfg_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(SettingForm)

        QMetaObject.connectSlotsByName(SettingForm)
    # setupUi

    def retranslateUi(self, SettingForm):
        SettingForm.setWindowTitle(QCoreApplication.translate("SettingForm", u"Form", None))
        self.server_setting_box.setTitle(QCoreApplication.translate("SettingForm", u"\u670d\u52a1\u5668\u8bbe\u7f6e", None))
        self.server_ip_label.setText(QCoreApplication.translate("SettingForm", u"\u670d\u52a1\u5668IP", None))
        self.server_port_label.setText(QCoreApplication.translate("SettingForm", u"\u7aef\u53e3", None))
        self.override_server_info.setText(QCoreApplication.translate("SettingForm", u"Override", None))
        self.monitor_push_label.setText(QCoreApplication.translate("SettingForm", u"\u89c6\u9891\u63a8\u6d41\u5730\u5740", None))
        self.override_monitor_url.setText(QCoreApplication.translate("SettingForm", u"Override", None))
        self.monitor_code_label.setText(QCoreApplication.translate("SettingForm", u"\u63a8\u6d41\u7801", None))
        self.override_monitor_code.setText(QCoreApplication.translate("SettingForm", u"Override", None))
        self.dtu_setting_box.setTitle(QCoreApplication.translate("SettingForm", u"4G DTU \u8bbe\u7f6e", None))
        self.register_label.setText(QCoreApplication.translate("SettingForm", u"\u6ce8\u518c\u5305", None))
        self.override_access_key.setText(QCoreApplication.translate("SettingForm", u"Override", None))
        self.reset_cfg_btn.setText(QCoreApplication.translate("SettingForm", u"\u91cd\u7f6e", None))
        self.save_cfg_btn.setText(QCoreApplication.translate("SettingForm", u"\u4fdd\u5b58", None))
        self.cancel_cfg_btn.setText(QCoreApplication.translate("SettingForm", u"\u53d6\u6d88", None))
    # retranslateUi

