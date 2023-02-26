# -*- coding: utf-8 -*-
################################################################################
# Author: tianxin
# Date: 2023-01-29
# 首页界面
################################################################################
import os

from PySide6 import QtCore
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtWidgets import QWidget

from ui.ui_home import Ui_HomeForm
from utils.config import config

class HomeWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.home_form = Ui_HomeForm()
        self.home_form.setupUi(self)
        self.home_form.MapWebView.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.home_form.MapWebView.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.home_form.MapWebView.page().settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        self.load_map()

    def load_map(self):
        """
        载入地图资源
        """
        map_path = config.get_map_abs_path()
        print(config.get_map_abs_path())
        self.home_form.MapWebView.load(QtCore.QUrl(map_path))
