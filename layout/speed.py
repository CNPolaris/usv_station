# -*- coding: utf-8 -*-
# 速度仪表盘组件

import sys

from PySide6.QtWidgets import QWidget, QApplication

from ui.ui_speed import Ui_FormSpeed


class SpeedWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.speed_ui = Ui_FormSpeed()
        self.speed_ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = SpeedWindow()

    w.show()

    sys.exit(app.exec())
