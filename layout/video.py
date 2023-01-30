# -*- coding: utf-8 -*-
################################################################################
# Author: tianxin
# Date: 2023-01-29
# 船载监控视频界面模块
################################################################################
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

from ui.ui_video import Ui_VideoForm


class VideoWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.video_form = Ui_VideoForm()
        self.video_form.setupUi(self)

    def when_no_video(self):
        self.video_form.VideoLabel.setStyleSheet("background-color:block;")

