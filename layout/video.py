# -*- coding: utf-8 -*-
################################################################################
# Author: tianxin
# Date: 2023-01-29
# 船载监控视频界面模块
################################################################################
from PySide6.QtGui import QPixmap, QImage, QIcon, QCloseEvent
from PySide6.QtWidgets import QWidget
import cv2

from ui.ui_video import Ui_VideoForm
from threads.monitor_thread import MonitorThread

from utils.config import config
from utils.logger import logger
class VideoWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.video_form = Ui_VideoForm()
        self.video_form.setupUi(self)
        
        self.setWindowTitle("船载监控视频")
        self.setWindowIcon(QIcon(config.get_icon_abs_path()))

        ##################################
        # 监控视频子线程线程
        ##################################
        self.monitor_thread = MonitorThread()
        # self.monitor_thread.start()
        # self.monitor_thread.send_img_data.connect(self.recv_img)
    def when_no_video(self):
        self.video_form.VideoLabel.setStyleSheet("background-color:block;")

    def when_sys_exit(self, flag):
        """监听软件退出信号
            如果退出，终止线程, 关闭页面
        """
        if flag:
            try:
                self.monitor_thread.destroy()
                self.close()
            except:
                logger.error("[地面站-监控视频]->线程退出失败")
                
    def recv_img(self, array):
        """接收监控线程传递的视频帧数组
        """
        show = cv2.resize(array, (self.video_form.VideoLabel.width(), self.video_form.VideoLabel.height()))
        show_image = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        self.video_form.VideoLabel.setPixmap(QPixmap.fromImage(show_image))
        
    def closeEvent(self, event: QCloseEvent) -> None:
        """如果单独关闭监控页面 终止线程"""
        self.monitor_thread.destroy()
        self.close()