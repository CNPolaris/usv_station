# -*- coding: utf-8 -*-
# 状态提示灯自定义控件
__author__ = "tian.xin"

from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QColor, QPainter

class LightTipBar(QWidget):
  TurnOn = False
  
  TurnOnColor = QColor(0, 255, 0)  #状态打开时颜色
  TurnOffColor = QColor(255, 0, 0) #状态关闭时颜色
  
  def __init__(self, parent=None) -> None:
    super(LightTipBar, self).__init__(parent)
  
  def paintEvent(self, event) -> None:
    super(LightTipBar, self).paintEvent(event)
    painter = QPainter(self)
    painter.setRenderHints(QPainter.RenderHint.Antialiasing |
                              QPainter.RenderHint.TextAntialiasing)
    width = self.width()
    height = self.height()
    side = min(width, height)
    painter.translate(width / 2, height / 2)
    painter.scale(side / 100.0, side / 100.0)
    
    self.drawBack(painter)
  
  def drawBack(self, painter):
    
    radius = 50
    painter.save()
    painter.setPen(Qt.PenStyle.NoPen)
    
    if self.TurnOn:
      painter.setBrush(self.TurnOnColor)
      painter.drawEllipse(QRectF(-radius, -radius, radius * 2, radius * 2))
      
    else:
      painter.setPen(Qt.PenStyle.NoPen)
      painter.setBrush(self.TurnOffColor)
      painter.drawEllipse(QRectF(-radius, -radius, radius * 2, radius * 2))
      
    painter.restore()
  
  def setTurnValue(self, value=bool):
    self.TurnOn = value
    