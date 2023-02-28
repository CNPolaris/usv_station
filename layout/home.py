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
from threads.station_thread import StationThread
from components.CircleProgressBar import CircleProgressBar
from components.PercentProgressBar import PercentProgressBar
from components.SpeedProgressBar import SpeedProgressBar

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
    ###############################
    #主线程向子线程传值信号        #
    ###############################
    # 油门信号传递
    left_signal = QtCore.Signal(int)
    right_signal = QtCore.Signal(int)
    def __init__(self):
        super().__init__()
        self.home_form = Ui_HomeForm()
        self.home_form.setupUi(self)
        self.home_form.MapWebView.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        self.home_form.MapWebView.page().settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.home_form.MapWebView.page().settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        self.load_map()
        ############################
        # 航速姿态等组件
        ############################
        speed_layout  = QHBoxLayout()
        self.speed_bar = SpeedProgressBar(self)
        speed_layout.addWidget(self.speed_bar)
        self.home_form.speed_widget.setLayout(speed_layout)
        ############################
        # 油门进度条
        ############################
        layout = QHBoxLayout(self)
        # 主推进器
        self.left_staticPercentProgressBar = PercentProgressBar(self)
        self.left_staticPercentProgressBar.showFreeArea = True
        self.left_staticPercentProgressBar.ShowSmallCircle = True
        self.right_staticPercentProgressBar = PercentProgressBar(self)
        self.right_staticPercentProgressBar.showFreeArea = True
        self.right_staticPercentProgressBar.ShowSmallCircle = True
        
        # 侧推进器
        self.left_side_percent = PercentProgressBar(self,  styleSheet="""
            qproperty-textColor: rgb(255, 0, 0);
            qproperty-borderColor: rgb(0, 255, 0);
            qproperty-backgroundColor: rgb(240,255,240);
        """)
        self.left_side_percent.showFreeArea = True
        self.left_side_percent.ShowSmallCircle = True
        self.right_side_percent = PercentProgressBar(self,  styleSheet="""
            qproperty-textColor: rgb(255, 0, 0);
            qproperty-borderColor: rgb(0, 255, 0);
            qproperty-backgroundColor: rgb(240,255,240);
        """)
        self.right_side_percent.showFreeArea = True
        self.right_side_percent.ShowSmallCircle = True
        # 加入布局
        layout.addWidget(self.left_side_percent)
        layout.addWidget(self.left_staticPercentProgressBar)
        layout.addWidget(self.right_staticPercentProgressBar)
        layout.addWidget(self.right_side_percent)
        self.home_form.process_layout.addLayout(layout)
        # slider设置最大值最小值，启动时锁死，直到建立连接后解锁
        self.home_form.left_slider.setMinimum(0)
        self.home_form.left_slider.setMaximum(100)
        self.home_form.right_slider.setMaximum(0)
        self.home_form.right_slider.setMaximum(100)
        self.home_form.left_slider.setDisabled(True)
        self.home_form.right_slider.setDisabled(True)
        self.home_form.left_side_slider.setMinimum(0)
        self.home_form.left_side_slider.setMaximum(100)
        self.home_form.left_side_slider.setDisabled(True)
        self.home_form.right_side_slider.setMinimum(0)
        self.home_form.right_side_slider.setMaximum(100)
        self.home_form.right_side_slider.setDisabled(True)
        # slider数据变化事件
        self.home_form.left_slider.valueChanged.connect(self.left_staticPercentProgressBar.setValue)
        self.home_form.right_slider.valueChanged.connect(self.right_staticPercentProgressBar.setValue)
        self.home_form.left_side_slider.valueChanged.connect(self.left_side_percent.setValue)
        self.home_form.right_side_slider.valueChanged.connect(self.right_side_percent.setValue)
        self.home_form.left_slider.valueChanged.connect(self.left_signal.emit)
        self.home_form.right_slider.valueChanged.connect(self.right_signal.emit)
        ############################
        # 连接tcp服务器设置
        ############################
        self.is_connect = True  # 状态变量 False时未连接 True时已经连接
        self.home_form.connect_tcp_btn.setIcon(QIcon(config.get_static_img_abs_path("start")))
        self.home_form.connect_tcp_btn.clicked.connect(self.on_connect_tcp_btn_clicked)
        self.connect_process_widget = ConnectProcessWidget()  # 连接服务器进度条组件
        ##################################
        # 子线程
        ##################################
        self.command_thread = CommandThread()
        self.station_thread = StationThread()
        # 子线程向主线程通信
        self.command_thread.send_connect_flag_signal.connect(self.connect_process_bar)  # 绑定连接状态信号量
        # 主线程向子线程通信
        self.left_signal.connect(self.command_thread.send_left_accelerator_to_dtu)
        self.right_signal.connect(self.command_thread.send_right_accelerator_to_dtu)
        
    def load_map(self):
        """
        载入地图资源
        """
        map_path = config.get_map_abs_path()
        self.home_form.MapWebView.load(QtCore.QUrl(map_path))
        
    def on_connect_tcp_btn_clicked(self):
        """连接TCP服务器"""
        if self.is_connect:
            self.command_thread.start()
            self.station_thread.start()
            # 进度条
            self.connect_process_widget.setWindowModality(QtCore.Qt.ApplicationModal)
            self.connect_process_widget.show()
        else:
            self.is_connect = True
            self.command_thread.destroy()
            self.station_thread.destroy()
            # 断开连接后 锁死 避免出错
            self.home_form.left_slider.setDisabled(True)
            self.home_form.right_slider.setDisabled(True)
            self.home_form.left_side_slider.setDisabled(True)
            self.home_form.right_side_slider.setDisabled(True)
    
    def connect_process_bar(self, flag):
        """连接服务器进度动画"""
        if flag == 1:  # 连接服务器成功
            self.home_form.connect_tcp_btn.setText("结束连接")
            self.home_form.connect_tcp_btn.setIcon(QIcon(config.get_static_img_abs_path("stop")))
            self.is_connect = False
            self.connect_process_widget.close()
            self.home_form.left_slider.setDisabled(False)
            self.home_form.right_slider.setDisabled(False)
            self.home_form.left_side_slider.setDisabled(False)
            self.home_form.right_side_slider.setDisabled(False)
            reply = QMessageBox.information(self, "服务连接", "连接成功", QMessageBox.Yes)
        else:
            self.home_form.connect_tcp_btn.setText("打开连接")
            self.home_form.connect_tcp_btn.setIcon(QIcon(config.get_static_img_abs_path("start")))
            self.connect_process_widget.close()
            reply = QMessageBox.warning(self, "服务连接", "连接失败", QMessageBox.Yes)
            self.command_thread.quit()