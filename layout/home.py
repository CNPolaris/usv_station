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
from PySide6.QtWebChannel import QWebChannel

from ui.ui_home import Ui_HomeForm
from utils.config import config
from utils.logger import logger
from threads.command_thread import CommandThread
from threads.station_thread import StationThread
from components.CircleProgressBar import CircleProgressBar
from components.PercentProgressBar import PercentProgressBar
from components.SpeedProgressBar import SpeedProgressBar
from components.FlightAdi import FlightAdi
from components.SwitchButton import SwitchButton
from components.LightTipBar import LightTipBar


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
        self.home_form.MapWebView.page().settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        self.home_form.MapWebView.page().settings().setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        self.home_form.MapWebView.page().settings().setAttribute(QWebEngineSettings.WebAttribute.LocalStorageEnabled, True)
        self.webPage = self.home_form.MapWebView.page()
        self.channel = QWebChannel(self)
        self.channel.registerObject('py', self)
        self.webPage.setWebChannel(self.channel)
        self.initWebSetting()
        self.load_map()
        ############################
        # 航速姿态等组件
        ############################
        speed_layout  = QHBoxLayout()
        self.speed_bar = SpeedProgressBar(self)
        speed_layout.addWidget(self.speed_bar)
        self.home_form.speed_widget.setLayout(speed_layout)
        plane_layout = QHBoxLayout()
        self.plane = FlightAdi()
        self.plane.setMinimumSize(100, 100)
        self.plane.setMaximumSize(100, 100)
        plane_layout.addWidget(self.plane)
        self.home_form.post_widget.setLayout(plane_layout)
        ############################
        # 横滚角、俯仰角、经度、纬度、速率、航向等数据
        ############################
        self.roll_value = 0.0   #横滚角
        self.deg_value = 0.0    #俯仰角
        self.lng_value = 0.0    #经度
        self.lat_value = 0.0    #纬度
        self.speed_value = 0.0  #地面速率
        self.direct_value = 0.0 #当前航向
        self.init_drive_data_label()
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
        self.home_form.left_slider.setMinimum(-100)
        self.home_form.left_slider.setMaximum(100)
        self.home_form.right_slider.setMinimum(-100)
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
        # 控制按钮
        ############################
        self.server_switch_btn = SwitchButton()         #地面站控制开关
        self.server_switch_btn.setMinimumSize(70, 30)
        self.server_switch_btn.setMaximumSize(70, 30)
        self.server_switch_btn.toggled.connect(self.on_server_switch_btn_click)
        
        self.sideLight = LightTipBar()          # 车舵操作模拟指示灯
        self.sideLight.setMinimumSize(25, 25)
        self.sideLight.setMaximumSize(25, 25)
        self.differenceLight = LightTipBar()    # 差分开关状态指示灯
        self.differenceLight.setMinimumSize(25, 25)
        self.differenceLight.setMaximumSize(25, 25)
        
        self.init_control_btn_layout()
        ############################
        # 连接tcp服务器设置
        ############################
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
        
    def initWebSetting(self):
        """初始化Web相关设置"""
        settings = self.home_form.MapWebView.settings()
        WebAttribute = QWebEngineSettings.WebAttribute
        settings.setAttribute(WebAttribute.LocalContentCanAccessRemoteUrls, True)
        settings.setDefaultTextEncoding("utf-8")
        settings.setAttribute(WebAttribute.XSSAuditingEnabled, True)
        
    def load_map(self):
        """
        载入地图资源
        """
        map_path = config.get_map_abs_path()
        self.home_form.MapWebView.load(QtCore.QUrl(map_path))
        
    def init_control_btn_layout(self):
        """初始化控制按钮组
        """
        control_vLayout = QVBoxLayout()
        # 服务器连接开关模块
        btn_layout = QHBoxLayout()
        btn_label = QLabel("服务器连接")
        font = QFont()
        font.setPointSize(12)
        btn_label.setFont(font)
        btn_layout.addWidget(btn_label)
        btn_layout.addWidget(self.server_switch_btn)
        control_vLayout.addLayout(btn_layout)
        # 状态灯模块
        side_layout = QHBoxLayout()
        side_light_label = QLabel("车舵模拟状态灯")
        side_light_label.setFont(font)
        
        side_layout.addWidget(side_light_label)
        side_layout.addWidget(self.sideLight)
        control_vLayout.addLayout(side_layout)
        
        diff_layout = QHBoxLayout()
        diff_light_label = QLabel("差分开关状态灯")
        diff_light_label.setFont(font)
        diff_layout.addWidget(diff_light_label)
        diff_layout.addWidget(self.differenceLight)
        control_vLayout.addLayout(diff_layout)
        self.home_form.control_btn_widget.setLayout(control_vLayout)

    def on_server_switch_btn_click(self, toggle):
        """服务器连接切换按钮

        Parameters
        ----------
        toggle : bool
            连接开关 True: 开关打开 False: 关闭
        """
        if toggle:
            # 进度条
            self.connect_process_widget.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
            self.connect_process_widget.show()
            self.command_thread.start()
            self.station_thread.start()
        else:
            self.command_thread.destroy()
            self.station_thread.destroy()
            # 断开连接后 锁死 避免出错
            self.home_form.left_slider.setDisabled(True)
            self.home_form.right_slider.setDisabled(True)
            self.home_form.left_side_slider.setDisabled(True)
            self.home_form.right_side_slider.setDisabled(True)
            
    def init_drive_data_label(self):
        """初始化航行数据label显示"""
        font = QFont()
        font.setPointSize(18)
        self.home_form.roll_value_label.setText(str(self.roll_value))
        self.home_form.roll_value_label.setFont(font)
        self.home_form.roll_value_label.setStyleSheet("QLabel{color: rgb(255, 147, 38)}")
        self.home_form.deg_value_label.setText(str(self.deg_value))
        self.home_form.deg_value_label.setFont(font)
        self.home_form.deg_value_label.setStyleSheet("QLabel{color: rgb(255, 147, 38)}")
        self.home_form.lng_value_label.setText(str(self.lng_value))
        self.home_form.lng_value_label.setFont(font)
        self.home_form.lng_value_label.setStyleSheet("QLabel{color: rgb(255, 147, 38)}")
        self.home_form.lat_value_label.setText(str(self.lat_value))
        self.home_form.lat_value_label.setFont(font)
        self.home_form.lat_value_label.setStyleSheet("QLabel{color: rgb(255, 147, 38)}")
        self.home_form.speed_value_label.setText(str(self.speed_value)) 
        self.home_form.speed_value_label.setFont(font)
        self.home_form.speed_value_label.setStyleSheet("QLabel{color: rgb(255, 147, 38)}")
        self.home_form.direct_value_label.setText(str(self.direct_value))
        self.home_form.direct_value_label.setFont(font)
        self.home_form.direct_value_label.setStyleSheet("QLabel{color: rgb(255, 147, 38)}")
        
    def connect_process_bar(self, flag):
        """连接服务器进度动画"""
        if flag == 1:  # 连接服务器成功
            self.is_connect = False
            self.connect_process_widget.close()
            self.home_form.left_slider.setDisabled(False)
            self.home_form.right_slider.setDisabled(False)
            self.home_form.left_side_slider.setDisabled(False)
            self.home_form.right_side_slider.setDisabled(False)
            # 地图添加船体标注
            info = {'gatewayKey': config.get_access_key()}
            self.add_ship_marker_in_map(info)
            reply = QMessageBox.information(self, "服务连接", "连接成功", QMessageBox.Yes)
        else:
            self.connect_process_widget.close()
            reply = QMessageBox.warning(self, "服务连接", "连接失败", QMessageBox.Yes)
            self.server_switch_btn.state = False
            self.command_thread.destroy()
            self.station_thread.destroy()
    
    def when_sys_exit(self, flag):
        """系统退出时 关闭线程"""
        if flag:
            try:
                self.command_thread.destroy()
                self.station_thread.destroy()
            except:
                pass
    
    def add_ship_marker_in_map(self, info):
        """add_ship_marker_in_map 在地图上添加船体标注

        Parameters
        ----------
        info : dict
            连接时船体相关信息
        """
        logger.info(f"[添加船体]-->{info}")
        self.webPage.runJavaScript(f'addNewShipMarker({info})')
