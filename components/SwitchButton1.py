# -*- coding: utf-8 -*-
# 自定义开关按钮
__author__ = "tian.xin"

from PySide6 import QtCore
from PySide6.QtCore import Property as pyqtProperty,  QRectF, QTimer, QRect
from PySide6.QtGui import QColor, QPainter, QFont, QPolygon, QPainterPath, QPen, QRadialGradient
from PySide6.QtWidgets import QWidget, QApplication

class SwitchButton(QWidget):
  ButtonStyle_Rect = 0      #圆角矩形
  ButtonStyle_CircleIn = 1  #内圆形
  ButtonStyle_CircleOut = 2 #外圆形
  
  Space = 5           #滑块离背景间隔
  RectRadius = 3.0    #圆角角度
  Checked = False     #是否选中
  ShowText = True     #显示文字
  ShowCircle = False  #显示小圆
  Animation = True    #动画过渡
  
  ButtonStyle = 1  #开关按钮样式
  
  BgColorOff = QColor(105, 105, 105)     #关闭时背景颜色
  BgColorOn = QColor(139, 101, 8)        #打开时背景颜色
  SliderColorOff = QColor(255, 255, 255) #关闭时滑块颜色
  SliderColorOn = QColor(255, 255, 255)  #打开时滑块颜色
  TextColorOff = QColor(0, 0, 0)         #关闭时文字颜色
  TextColorOn = QColor(0, 0, 0)          #打开时文字颜色
  
  TextOn = "停止"     #打开时显示文字
  TextOff = "启用"   #关闭时显示文字
  
  Step = 10         #每次移动的步长
  StartX = 0        #滑块开始x轴坐标
  
  def paintEvent(self, event):
    super(SwitchButton, self).paintEvent(event)
    painter = QPainter(self)
    painter.setRenderHints(QPainter.RenderHint.Antialiasing | QPainter.RenderHint.TextAntialiasing) 
    self.drawBg(painter)
    self.drawSlider(painter)

  def drawBg(self, painter):
    """绘制背景"""
    painter.save()
    painter.setPen(QtCore.Qt.PenStyle.NoPen)
    bgColor = self.BgColorOn if self.Checked else self.BgColorOff
    
    if not self.isEnabled():
      bgColor.setAlpha(60)
    
    painter.setBrush(bgColor)
    
    if self.ButtonStyle == self.ButtonStyle_Rect:
      painter.drawRoundedRect(QRect(), self.RectRadius, self.RectRadius)
    elif self.ButtonStyle == self.ButtonStyle_CircleIn:
      rect = QRect(0, 0, self.width(), self.height())
      side = min(rect.width(), rect.height())
      
      path_1 = QPainterPath()
      path_1.addEllipse(rect.x(), rect.y(), side, side)
      
      path_2 = QPainterPath()
      path_2.addEllipse(rect.width() - side, rect.y(), side, side)
      
      path_3 = QPainterPath()
      path_3.addRect(rect.x() + side / 2, rect.y(), rect.width() - side, rect.height())
      
      path = QPainterPath()
      path = path_1 + path_2 + path_3
      painter.drawPath(path)
    elif self.ButtonStyle == self.ButtonStyle_CircleOut:
      rect = QRect(self.height() / 2, self.Space, self.width() - self.height(), self.height() - self.Space * 2)
      painter.drawRoundedRect(rect, self.RectRadius, self.RectRadius)
      
    if self.ButtonStyle == self.ButtonStyle_Rect or self.ButtonStyle == self.ButtonStyle_CircleIn:
      if self.ShowText:
        sliderWidth = min(self.width(), self.height()) - self.Space * 2
        if self.ButtonStyle == self.ButtonStyle_Rect:
          sliderWidth = self.width() / 2 - 5
        elif self.ButtonStyle == self.ButtonStyle_CircleIn:
          sliderWidth -= 5

        if self.Checked:
          textRect = QRect(0, 0, self.width() - sliderWidth, self.height())
          painter.setPen(self.TextColorOn)
          painter.drawText(textRect, QtCore.Qt.AlignmentFlag.AlignCenter, self.TextOn)
        else:
          textRect = QRect(sliderWidth, 0, self.width() - sliderWidth, self.height())
          painter.setPen(self.TextColorOff)
          painter.drawText(textRect, QtCore.Qt.AlignmentFlag.AlignCenter, self.TextOff)
      elif self.ShowCircle:
        side = min(self.width(), self.height()) / 2
        y = (self.height() - side) / 2
        
        if self.Checked:
          circleRect = QRect(side / 2, y, side, side)
          pen = QPen(self.TextColorOn, 2)
          painter.setPen(pen)
          painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
          painter.drawEllipse(circleRect)
        else:
          circleRect = QRect(self.width() - (side * 1.5), y, side, side)
          pen = QPen(self.TextColorOff, 2)
          painter.setPen(pen)
          painter.setBrush(QtCore.Qt.BrushStyle.NoBrush)
          painter.drawEllipse(circleRect)
          
    painter.restore()
    
  def drawSlider(self, painter):
    painter.save()
    painter.setPen(QtCore.Qt.PenStyle.NoPen)
    
    if not self.Checked:
      painter.setBrush(self.SliderColorOff)
    else:
      painter.setBrush(self.SliderColorOn)
      
    if self.ButtonStyle == self.ButtonStyle_Rect:
      sliderWidth = self.width() / 2 - self.Space * 2
      sliderHeight = self.height() - self.Space * 2
      sliderRect = QRect(self.StartX + self.Space, self.Space, sliderWidth, sliderHeight)
      painter.drawRoundedRect(sliderRect, self.RectRadius, self.RectRadius)
    elif self.ButtonStyle == self.ButtonStyle_CircleIn:
      rect = QRect(0 ,0 ,self.width(), self.height())
      sliderWidth = min(rect.width(), rect.height()) - self.Space * 2
      sliderRect = QRect(self.StartX + self.Space, self.Space, sliderWidth, sliderWidth)
      painter.drawEllipse(sliderRect)
    elif self.ButtonStyle == self.ButtonStyle_CircleOut:
      sliderWidth = self.height()
      sliderRect = QRect(self.StartX, 0, sliderWidth, sliderWidth)
      
      color_1 = QtCore.Qt.GlobalColor.white if self.Checked else self.BgColorOff
      color_2 = self.SliderColorOn if self.Checked else self.SliderColorOff
      
      radialGradient = QRadialGradient(sliderRect.center(), sliderWidth / 2)
      radialGradient.setColorAt(0, color_1 if self.Checked else color_2)
      radialGradient.setColorAt(0.5, color_1 if self.Checked else color_2)
      radialGradient.setColorAt(0.6, color_2 if self.Checked else color_1)
      radialGradient.setColorAt(1.0, color_2 if self.Checked else color_1)
      painter.setBrush(radialGradient)
      painter.drawEllipse(sliderRect)
    painter.restore()    
  def mouseReleaseEvent(self, event) -> None:
    super(SwitchButton, self).mouseReleaseEvent(event)
    self.Checked = False if self.Checked else True

import sys
app = QApplication(sys.argv)
w = SwitchButton()

w.show()

sys.exit(app.exec())