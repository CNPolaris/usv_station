# -*- coding: utf-8 -*-
################################################################################
# Author: tianxin
# Date: 2023-03-10
# 地面站视频监控模块线程
################################################################################

from PySide6.QtCore import QThread, Signal
import cv2

from utils.config import config

class MonitorThread(QThread):
  send_img_data = Signal(object)
    
  def __init__(self) -> None:
    super().__init__()
    self.monitor_url = config.get_monitor_url()
    
  def run(self) -> None:
    cap = cv2.VideoCapture(self.monitor_url)
    while cap.isOpened():
      ret, frame = cap.read()
      if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        self.send_img_data.emit(frame)
        
  def destroy(self):
    print("线程终止")
    self.quit()
    self.wait()