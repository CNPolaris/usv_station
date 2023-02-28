# -*- coding: utf-8 -*-
# 姿态仪表盘
__author__ = "tian.xin"

from PySide6 import QtCore
from PySide6.QtCore import Property as pyqtProperty, QSize, Qt, QRectF, QTimer, QRect
from PySide6.QtGui import QColor, QPainter, QFont, QIcon, QLinearGradient
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QSlider, QLabel

class PostPlane(QWidget):
  BorderOutColorStart = QColor(131, 139, 131)  # 外边框渐变开始颜色
  BorderOutColorEnd = QColor(131, 139, 131)    # 外边框渐变结束颜色
  BorderInColorStart = QColor(131, 139, 131)   # 内边框渐变开始颜色
  BorderInColorEnd = QColor(131, 139, 131)     # 内边框渐变结束颜色
  
  BackColor = QColor(135, 206, 250)   # 背景颜色
  PlaneColor = QColor(32, 178, 170)   # 姿态仪背景颜色
  ScaleColor = QColor(255, 255, 255)  # 刻度尺颜色
  LineColor = QColor(0, 0, 128)       # 线条颜色
  TextColor = QColor(224, 255, 255)   # 文字颜色
  PointerColor = QColor(255, 106, 106) # 指针颜色
  HandleColor = QColor(255, 193, 37)  # 手柄颜色
  
  DegValue = 0    # 旋转角度
  RollValue = 0   # 滚动值
  
  def paintEvent(self, event) -> None:
    super(PostPlane, self).paintEvent(event)
    width = self.width()
    height = self.height()
    side = min(width, height)
    
    # 绘制准备工作,启用反锯齿,平移坐标轴中心,等比例缩放
    painter = QPainter(self)
    painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
    painter.translate(width / 2, height / 2)
    painter.scale(side / 200.0, side / 200.0)
    # 绘制外边框
    self.drawBorderOut(painter)
    # 绘制内边框
    self.drawBorderIn(painter)
    # 绘制背景
    self.drawBack(painter)
    # 绘制姿势仪背景
    self.drawPlane(painter)
    # # 绘制刻度尺
    self.drawScale(painter)
    self.drawMinScale(painter)
    # # 绘制线条
    # self.drawLine(painter)
    # # 绘制指针
    # self.drawPointer(painter)
    # # 绘制手柄
    self.drawHandle(painter)
  
  def drawBorderOut(self, painter):
    """绘制外边框"""
    radius = 99
    painter.save()
    painter.setPen(Qt.PenStyle.NoPen)
    borderGradient = QLinearGradient(0, -radius, 0, radius)
    borderGradient.setColorAt(0, self.BorderOutColorStart)
    borderGradient.setColorAt(1, self.BorderOutColorEnd)
    painter.setBrush(borderGradient)
    painter.drawEllipse(-radius, -radius, radius * 2, radius * 2)
    painter.restore()
    
  def drawBorderIn(self, painter):
    """绘制内边框"""
    radius = 93
    painter.save()
    painter.setPen(Qt.PenStyle.NoPen)
    borderGradient = QLinearGradient(0, -radius, 0, radius)
    borderGradient.setColorAt(0, self.BorderInColorStart)
    borderGradient.setColorAt(1, self.BorderInColorEnd)
    painter.setBrush(borderGradient)
    painter.drawEllipse(-radius, -radius, radius * 2, radius * 2)
    painter.restore()
    
  def drawBack(self, painter):
    """绘制背景"""
    radius = 98
    painter.save()
    painter.setPen(Qt.PenStyle.NoPen)
    borderGradient = QLinearGradient(0, -radius, 0, radius)
    self.BackColor.setAlpha(255)
    borderGradient.setColorAt(0, self.BackColor)
    self.BackColor.setAlpha(150)
    borderGradient.setColorAt(1, self.BackColor)
    painter.setBrush(borderGradient)
    painter.drawEllipse(-radius, -radius, radius * 2, radius * 2)
    painter.restore()

  def drawPlane(self, painter):
    """绘制姿势仪背景"""
    radius = 90
    painter.save()
    painter.rotate(self.DegValue)
    painter.setPen(Qt.PenStyle.NoPen)
    painter.setBrush(self.PlaneColor)
    rect = QRect(-radius, -radius, radius * 2, radius * 2)
    
    offset = -(self.RollValue * radius / 100)
    startAngle = 180 + offset
    endAngle = offset
    span = endAngle + startAngle
    painter.drawChord(rect, -16 * startAngle, 16 * span)
    painter.restore()

  def drawScale(self, painter):
    """绘制刻度尺"""
    radius = 93
    startAngle = 90.0
    endAngle = 90.0
    painter.save()
    painter.rotate(startAngle)  # 从水平九十度开始
    angleStep = (360.0 - startAngle - endAngle) / 6
    painter.setPen(Qt.PenStyle.NoPen)
    painter.setPen(self.ScaleColor)
    font = QFont()
    font.setPixelSize(12)
    font.setBold(True)
    painter.setFont(font)
    for i in range(7):
      painter.drawLine(0, radius - 10, 0, radius)
      painter.rotate(angleStep)
    painter.restore()  #恢复坐标系
    
  def drawMinScale(self, painter):
    """小刻度"""
    radius = 93
    painter.save()
    painter.setPen(Qt.PenStyle.NoPen)
    painter.setPen(self.ScaleColor)
    painter.rotate(160)
    angleStep = (360.0 - 160.0 - 170.0) / 3
    for i in range(2):
      painter.drawLine(0, radius - 5, 0, radius)
      painter.rotate(angleStep)
    painter.rotate(10)
    angleStep = (360.0 - 160.0 - 170.0) / 3
    for i in range(2):
      painter.drawLine(0, radius - 5, 0, radius)
      painter.rotate(angleStep)
    painter.restore()
    
  def drawHandle(self, painter):
    """绘制手柄"""
    painter.save()
    painter.setPen(Qt.PenStyle.NoPen)
    painter.setBrush(self.HandleColor)
    # 先绘制中心
    radius = 6
    painter.drawEllipse(0, -radius/2, radius, radius)
    painter.restore()
    # 绘制水平弧
    # radius = 20
    # painter.setPen(Qt.PenStyle.NoPen)
    # painter.setPen(self.HandleColor)
    # painter.drawLine(0, 0, 0, 20)
    # rect = QRect(-18, -20, radius * 2, radius * 2)
    # painter.drawArc(rect, 0 * 16, -180 * 16)
    # painter.restore()
    
    # painter.setPen(Qt.PenStyle.NoPen)
    # painter.setPen(self.HandleColor)
    # painter.drawLine(-18, 0, -30, 0)
    # painter.drawLine(22, 0, 38, 0)
    # painter.restore()
  def setRollValue(self, value):
    self.RollValue = float(value)
  
  def setDegValue(self, value):
    self.DegValue = float(value)
