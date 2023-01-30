# -*- coding: utf-8 -*-
################################################################################
# Author: tianxin
# Date: 2023-01-29
# 主程序
################################################################################
import sys

from PySide6.QtGui import QAction
from PySide6.QtWebChannel import QWebChannel
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QStackedLayout, QPushButton

from ui.ui_main import Ui_MainWindow
from layout.home import HomeWidget
from layout.video import VideoWidget


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        # 主窗口载入
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        # 添加堆叠布局
        self._qsl = QStackedLayout(self.main_ui.MainWidget)
        self.home_ = HomeWidget()
        self.video_ = VideoWidget()

        self._qsl.addWidget(self.home_)
        self._qsl.addWidget(self.video_)
        # 工具栏
        self.tb = self.main_ui.toolBar
        self.home_action = QAction('首页', self)  # 0
        self.video_action = QAction('监控', self)  # 1
        # 工具栏动作绑定
        self.home_action.triggered.connect(self.change_qls_to_home)  # 默认首页
        self.video_action.triggered.connect(self.change_qls_to_video)
        self.tb.addAction(self.home_action)
        self.tb.addAction(self.video_action)

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
        self._qsl.setCurrentIndex(1)
        self.video_.when_no_video()


def win():
    app = QApplication(sys.argv)
    channel = QWebChannel()

    w = Window()
    w.setWindowTitle("USV地面站v0.1")
    channel.registerObject('py', w)
    w.home_.home_form.MapWebView.page().setWebChannel(channel)
    w.home_.home_form.MapWebView.show()
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    win()
