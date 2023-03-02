# -*- coding: utf-8 -*-
# 自定义开关按钮2
__author__ = "tian.xin"

from PySide6 import QtCore
from PySide6.QtCore import QRectF, QTimer
from PySide6.QtGui import QColor, QPainter, QPainterPath
from PySide6.QtWidgets import QWidget, QApplication

class SwitchButton2(QWidget):
  
  Checked = False
  BgColor =  QColor(0, 0, 0)
  CheckedColor =QColor(0, 150, 136) 
  DisabledColor =  QColor(190, 190, 190) 
  ThumbColor = QColor(255, 255, 255)
  radius = 8.0
  n_x = 0.0
  n_y = 0.0
  n_height = 16.0
  margin = 3.0
  timer = QTimer()
  
  def paintEvent(self, event) -> None:
    super(SwitchButton2, self).paintEvent(event)
    
    painter = QPainter(self)
    painter.setPen(QtCore.Qt.PenStyle.NoPen)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    
    path = QPainterPath()
    back = QColor()
    thumbColor = QColor()
    opacity=0
    if self.isEnabled():
      if self.Checked:
        back = self.CheckedColor
        thumbColor = self.CheckedColor
        opacity = 0.6
      else:
        back = self.BgColor
        thumbColor = self.ThumbColor
        opacity = 0.8
    else:
      back = self.BgColor
      opacity = 0.26
      thumbColor = self.DisabledColor
    
    painter.setBrush(back)
    painter.setOpacity(opacity)
    path.addRoundedRect(QRectF(self.margin, self.margin, self.width() - 2 * self.margin, self.height() - 2 * self.margin), self.radius, self.radius)
    painter.drawPath(path.simplified())
    
    painter.setBrush(thumbColor)
    painter.setOpacity(1.0)
    painter.drawEllipse(QRectF(self.n_x - (self.n_height / 2), self.n_y - (self.n_height / 2), self.height(), self.height()))
    
  def mousePressEvent(self, event) -> None:
    super(SwitchButton2, self).mousePressEvent(event)
    if self.isEnabled():
      if event.buttons() & QtCore.Qt.MouseButton.LeftButton:
        event.accept()
      else:
        event.ignore()
  
  def mouseReleaseEvent(self, event) -> None:
    super(SwitchButton2, self).mouseReleaseEvent(event)
    if self.isEnabled():
      if (event.type() == QtCore.QEvent.Type.MouseButtonRelease) and (event.button() == QtCore.Qt.MouseButton.LeftButton):
        event.accept()
        self.Checked = not self.Checked
        # 发射信号
        self.timer.start(10)
      else:
        event.ignore()

  def resizeEvent(self, event) -> None:
    self.n_x = self.n_height / 2
    self.n_y = self.n_height / 2
    super(SwitchButton2, self).resizeEvent(event)
    
  @QtCore.Slot()
  def onTimeout(self):
    if self.Checked:
      self.n_x += 1
      if self.n_x >= (self.width() - self.n_height):
        self.timer.stop()
    else:
      self.n_x -= 1
      if self.n_x <= self.n_height / 2:
        self.timer.stop()
    self.update()
  
  def isToggled(self):
    return self.Checked

  def setToggle(self,checked: bool):
    self.Checked = checked
    self.timer.start(10)
    
import sys
app = QApplication(sys.argv)
w = SwitchButton2()  
w.show()
w.setToggle(True)
sys.exit(app.exec())