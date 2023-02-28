# -*- coding: utf-8 -*-
# 仪表盘控件
__author__ = "tian.xin"
from PySide6 import QtCore
from PySide6.QtCore import Property as pyqtProperty,  QRectF
from PySide6.QtGui import QColor, QPainter, QFont, QPolygon
from PySide6.QtWidgets import QWidget
import math

class SpeedProgressBar(QWidget):
  MinValue = 0
  MaxValue = 8
  Value = 0
  StartAngle = 45.0  
  EndAngle = 45.0
  PieColor = QColor(0, 191, 255)  # 圆环颜色
  PointerColor = QColor(0, 191,255)  # 指针颜色
  TextColor = QColor(0, 191, 255)  # 刻度值颜色
  LineColor = QColor(28, 28,28)  # 刻度线颜色
  ScaleMajor = 8  # 大刻度数量
  ScaleMinor = 10  # 小刻度数量
  Unit = "knot"  # 单位
  def __int__(self, *args, value=0, minValue=0, maxValue=8,
              scaleMajor=8, scaleMinor=10, unit="knot", pieColor=QColor(0, 191, 255),
              pointerColor=QColor(0, 191, 255), textColor=QColor(0, 191, 255),
              lineColor=QColor(28, 28,28), **kwargs):
    super(SpeedProgressBar, self).__init__(*args, **kwargs)
    self.Value = value
    self.MinValue = minValue
    self.MaxValue = maxValue
    self.ScaleMajor = scaleMajor
    self.ScaleMinor = scaleMinor
    self.Unit = unit
    self.PieColor = pieColor
    self.PointerColor = pointerColor
    self.TextColor = textColor
    self.LineColor = lineColor
    
  def paintEvent(self, event):
    super(SpeedProgressBar, self).paintEvent(event)
    width = self.width()
    height = self.height()
    side = min(width, height)
    
    painter = QPainter(self)
    painter.translate(width / 2, height / 2)
    painter.scale(side / 200.0, side / 200.0)
    painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing) 
    # 绘制圆弧
    self.drawColorPie(painter)
    # 绘制单位
    self.drawUnit(painter)
    # 绘制指针
    self.drawPointerIndicator(painter)
    # 绘制刻度线
    self.drawScale(painter)
    # 绘制刻度值
    self.drawScaleNum(painter)
    # 绘制当前值
    self.drawValue(painter)
    
  def drawColorPie(self, painter):
    """圆环"""
    radius = 98
    painter.save()
    painter.setPen(QtCore.Qt.NoPen)
    painter.setPen(self.PieColor)
    painter.setBrush(QtCore.Qt.NoBrush)
    # 计算总范围角度，当前值范围角度，剩余值范围角度
    angleAll = 360.0 - self.StartAngle - self.EndAngle
    angleCurrent = angleAll * ((self.Value - self.MinValue) / (self.MaxValue - self.MinValue))
    angleOther = angleAll - angleCurrent
    # 绘制外边框圆弧
    rect = QRectF(-radius, -radius, radius* 2, radius * 2)
    painter.drawArc(rect, (270 - self.StartAngle - angleCurrent) * 16, angleCurrent * 16)
    painter.drawArc(rect, (270 - self.StartAngle - angleCurrent - angleOther) * 16, angleOther *16)
    # 绘制里面圆弧
    radius = 90
    rect = QRectF(-radius, -radius, radius* 2, radius * 2)
    painter.drawArc(rect, (270 - self.StartAngle - angleCurrent) * 16, angleCurrent * 16)
    painter.drawArc(rect, (270 - self.StartAngle - angleCurrent - angleOther) * 16, angleOther *16)
    painter.restore()
    
  def drawPointerIndicator(self, painter):
    """绘制指针"""
    painter.save()
    
    radius = 68
    painter.setPen(QtCore.Qt.NoPen)
    painter.setBrush(self.PointerColor)
    
    pts = QPolygon()
    pts.append(QtCore.QPoint(-5, 0))
    pts.append(QtCore.QPoint(0, -8))
    pts.append(QtCore.QPoint(5, 0))
    pts.append(QtCore.QPoint(0, radius))
    
    painter.rotate(self.StartAngle)
    degRotate = (360.0 - self.StartAngle - self.EndAngle) / (self.MaxValue - self.MinValue) * (self.Value - self.MinValue)
    
    painter.rotate(degRotate)
    painter.drawConvexPolygon(pts)
    painter.restore()
  
  def drawScale(self, painter):
    """绘制刻度线"""
    radius = 97
    painter.save()
    painter.rotate(self.StartAngle)
    steps = (self.ScaleMajor * self.ScaleMinor)
    angleStep = (360.0 - self.StartAngle - self.EndAngle) / steps
    painter.setPen(self.LineColor)
    for i in range(steps+1):
      if i % self.ScaleMinor == 0:  # 小刻度
        painter.drawLine(0, radius - 12, 0, radius)
      else:
        painter.drawLine(0, radius - 5, 0, radius)
      painter.rotate(angleStep)
    painter.restore()  #恢复坐标系
    
  def drawScaleNum(self, painter):
    """绘制刻度值"""
    radius = 75
    painter.save()
    painter.setPen(self.TextColor)
    
    startRad = (360 - self.StartAngle - 90) * (math.pi/180)
    deltaRad = (360 - self.StartAngle - self.EndAngle) * (math.pi / 180) / self.ScaleMajor
    
    for i in range(0, self.ScaleMajor + 1):
      sina = math.sin(startRad - i * deltaRad)
      cosa = math.cos(startRad - i * deltaRad)
      value = i * ((self.MaxValue - self.MinValue) / self.ScaleMajor) + self.MinValue
      strValue = str(int(value))
      x = radius * cosa
      y = -radius * sina
      painter.drawText(x, y, strValue)
  
  def drawValue(self, painter):
    """绘制当前值"""
    radius = 100
    painter.save()
    painter.setPen(self.TextColor)
    font = QFont()
    font.setPixelSize(30)
    painter.setFont(font)
    
    rect = QRectF(-radius, radius / 2, radius * 2, radius / 3)
    painter.drawText(rect, QtCore.Qt.AlignmentFlag.AlignCenter, f'{self.Value}')
    painter.restore()
  
  def drawUnit(self, painter):
    """绘制单位"""
    radius = 70
    painter.save()
    painter.setPen(self.TextColor)
    font = QFont()
    font.setPixelSize(12)
    painter.setFont(font)
    
    rect = QRectF(-radius, radius / 2, radius * 2, radius / 3)
    painter.drawText(rect, QtCore.Qt.AlignmentFlag.AlignHCenter, self.Unit)
    painter.restore()
    
  @pyqtProperty(int)
  def value(self) -> int:
      return self.Value
    
  @value.setter
  def value(self, value: int):
    if self.Value != value:
      self.Value = value
      self.update()
      
  def setValue(self, value):
    self.value = value
    