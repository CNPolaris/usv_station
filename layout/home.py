# -*- coding: utf-8 -*-
################################################################################
# Author: tianxin
# Date: 2023-01-29
# 首页界面
################################################################################
import os

from PySide6 import QtCore
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtCore import Property as pyqtProperty, QSize, Qt, QRectF, QTimer
from PySide6.QtGui import QColor, QPainter, QFont, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QSlider, QLabel, QMessageBox

from ui.ui_home import Ui_HomeForm
from utils.config import config
from threads.command_thread import CommandThread
from components.CircleProgressBar import CircleProgressBar
from components.PercentProgressBar import PercentProgressBar

showMessage = QMessageBox.question

class ConnectProcessWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("服务器连接")
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setMaximumSize(300, 200)
        self.resize(300, 200)
        layout = QVBoxLayout()
        label = QLabel("")
        label.setText("正在连接服务器....")
        layout.addWidget(label)
        process = CircleProgressBar(color=QColor(255, 0, 0), clockwise=False)
        layout.addWidget(process)
        self.setLayout(layout)

class HomeWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.home_form = Ui_HomeForm()
        self.home_form.setupUi(self)
        self.home_form.MapWebView.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.home_form.MapWebView.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.home_form.MapWebView.page().settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        self.load_map()
        # 油门进度条
        layout = QHBoxLayout(self)
        self.left_staticPercentProgressBar = PercentProgressBar(self)
        self.left_staticPercentProgressBar.showFreeArea = True
        self.left_staticPercentProgressBar.ShowSmallCircle = True
        layout.addWidget(self.left_staticPercentProgressBar)
        self.right_staticPercentProgressBar = PercentProgressBar(self)
        self.right_staticPercentProgressBar.showFreeArea = True
        self.right_staticPercentProgressBar.ShowSmallCircle = True
        layout.addWidget(self.right_staticPercentProgressBar)
        self.home_form.process_layout.addLayout(layout)
        # slider设置最大值最小值
        self.home_form.left_slider.setMinimum(0)
        self.home_form.left_slider.setMaximum(100)
        self.home_form.right_slider.setMaximum(0)
        self.home_form.right_slider.setMaximum(100)
        self.home_form.left_slider.valueChanged.connect(self.left_staticPercentProgressBar.setValue)
        self.home_form.right_slider.valueChanged.connect(self.right_staticPercentProgressBar.setValue)
        # 连接tcp服务器设置
        self.is_connect = True  # 状态变量 False时未连接 True时已经连接
        self.home_form.connect_tcp_btn.setIcon(QIcon(config.get_static_img_abs_path("start")))
        self.home_form.connect_tcp_btn.clicked.connect(self.on_connect_tcp_btn_clicked)
        # 连接服务器进度条组件
        self.connect_process_widget = ConnectProcessWidget()
        # 子线程初始化
        self.command_thread = CommandThread()
        
        # 子线程向主线程通信
        self.command_thread.send_connect_flag_signal.connect(self.connect_process_bar)  # 绑定连接状态信号量
        
    def load_map(self):
        """
        载入地图资源
        """
        map_path = config.get_map_abs_path()
        self.home_form.MapWebView.load(QtCore.QUrl(map_path))
        
    def on_connect_tcp_btn_clicked(self):
        """连接TCP服务器"""
        if self.is_connect:
            self.home_form.connect_tcp_btn.setText("结束连接")
            self.home_form.connect_tcp_btn.setIcon(QIcon(config.get_static_img_abs_path("stop")))
            self.is_connect = False
            self.command_thread.start()
            # 进度条
            self.connect_process_widget.setWindowModality(QtCore.Qt.ApplicationModal)
            self.connect_process_widget.show()
        else:
            self.home_form.connect_tcp_btn.setText("打开连接")
            self.home_form.connect_tcp_btn.setIcon(QIcon(config.get_static_img_abs_path("start")))
            self.is_connect = True
            self.command_thread.quit()
    
    def connect_process_bar(self, flag):
        """连接服务器进度动画"""
        if flag == 1:
            self.connect_process_widget.close()
            reply = QMessageBox.information(self, "服务连接", "连接成功", QMessageBox.Yes)
        else:
            reply = showMessage(self, "服务连接", "连接失败", QMessageBox.Yes)
            self.command_thread.quit()