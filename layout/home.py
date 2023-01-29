# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QWidget

from ui.ui_home import Ui_HomeForm


class HomeWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.home_form = Ui_HomeForm()
        self.home_form.setupUi(self)
