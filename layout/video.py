# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QWidget

from ui.ui_video import Ui_VideoForm


class VideoWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.video_form = Ui_VideoForm()
        self.video_form.setupUi(self)
