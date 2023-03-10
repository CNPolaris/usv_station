# -*- coding: utf-8 -*-
################################################################################
# Author: tianxin
# Date: 2023-01-29
# 主程序
################################################################################
import sys

from PySide6 import QtCore
from PySide6.QtGui import QAction, QCloseEvent, QIcon, QPixmap, QFont
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QStackedLayout, QPushButton, QMessageBox

from ui.ui_main import Ui_MainWindow
from layout.home import HomeWidget
from layout.video import VideoWidget
from layout.setting import SettingWidget
from threads.command_thread import CommandThread
from utils.config import config
class Window(QMainWindow):
    sys_exit_signal = QtCore.Signal(bool)
    
    def __init__(self):
        super().__init__()
        # 主窗口载入
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        # 添加堆叠布局
        self._qsl = QStackedLayout(self.main_ui.MainWidget)
        self.home_ = HomeWidget()
        self.monitor_widget = VideoWidget()
        self.setting_widget = SettingWidget()
        self._qsl.addWidget(self.home_)
        # self._qsl.addWidget(self.video_)
        # self._qsl.addWidget(self.setting_widget)
        # 工具栏
        self.tb = self.main_ui.toolBar
        self.home_action = QAction('首页', self)  # 0
        self.video_action = QAction('监控', self)  # 1
        self.setting_action = QAction('配置', self)  # 2
        
        # 工具栏动作绑定
        self.home_action.triggered.connect(self.change_qls_to_home)  # 默认首页
        self.video_action.triggered.connect(self.change_qls_to_video)
        self.setting_action.triggered.connect(self.change_qls_to_setting)
        self.tb.addAction(self.home_action)
        self.tb.addAction(self.video_action)
        self.tb.addAction(self.setting_action)
        # 信号量绑定
        self.sys_exit_signal.connect(self.home_.when_sys_exit)
        self.sys_exit_signal.connect(self.monitor_widget.when_sys_exit)
        
    def change_qls_to_home(self):
        """
        切换首页
        :return:
        """
        self._qsl.setCurrentIndex(0)

    def change_qls_to_video(self):
        """
        切换监控
        :return:
        """
        # self._qsl.setCurrentIndex(1)
        self.monitor_widget.when_no_video()
        self.monitor_widget.show()

    def change_qls_to_setting(self):
        """change_qls_to_setting 打开软件配置子窗体
        """
        self.setting_widget.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setting_widget.show()
    
    def closeEvent(self, event: QCloseEvent) -> None:
        reply = QMessageBox.warning(self, '警告', "系统将退出，是否确认?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            self.sys_exit_signal.emit(True)
        else:
            event.ignore()
            
    def changeEvent(self, event) -> None:
        if event.type() == QtCore.QEvent.WindowStateChange:
            if not self.isMaximized():
                self.home_.plane.setMaximumSize(80, 80)
                self.home_.plane.setMinimumSize(80, 80)
                self.home_.speed_bar.setMaximumSize(80, 80)
                self.home_.speed_bar.setMinimumSize(80, 80)

                print("ff")
            elif self.isMaximized():
                self.home_.plane.setMaximumSize(180, 180)
                self.home_.plane.setMinimumSize(180, 180)
                self.home_.speed_bar.setMaximumSize(180, 180)
                self.home_.speed_bar.setMinimumSize(180, 180)
                
def win():
    app = QApplication(sys.argv)

    w = Window()
    w.setWindowTitle("USV地面站软件v0.1")
    w.setWindowIcon(QIcon(config.get_icon_abs_path()))
    # 背景色
    w.setStyleSheet("QMainWindow{background-color: rgb(4,108,149)} QLabel{color: rgb(255, 255, 255)} QDialog{background-color: rgb(214, 77, 84)}")
    w.showMaximized()    
    sys.exit(app.exec())


if __name__ == '__main__':
    win()
