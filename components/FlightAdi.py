# -*- coding: utf-8 -*-
# 姿态控件
__author__ = "tian.xin"

from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QWidget
from PySide6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtCore import QPointF, Qt, QSize
from PySide6.QtGui import QTransform

import math
import os
FILE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + 'static' + os.sep + 'svg' + os.sep

class FlightAdi(QGraphicsView):
  m_originalHeight = 0
  m_originalWidth = 0

  m_originalPixPerDeg = 0.0
  m_originalAdiCtr = None
  
  m_backZ = 0
  m_faceZ = 0
  m_ringZ = 0
  m_caseZ = 0
  
  m_roll = 0.0    #滚动值
  m_pitch = 0.0   #俯仰值
  
  m_faceDeltaX_new = 0.0
  m_faceDeltaX_old = 0.0
  m_faceDeltaY_new = 0.0
  m_faceDeltaY_old = 0.0
  
  m_scaleX = 0.0
  m_scaleY = 0.0  
  
  # 背景
  m_scene = None
  # Svg素材
  m_itemBack = None
  m_itemFace = None
  m_itemRing = None
  m_itemCase = None
  
  def __init__(self) -> None:
    super(FlightAdi, self).__init__()

    self.m_originalHeight = 240
    self.m_originalWidth = 240
    self.m_originalPixPerDeg = 1.7
    self.m_originalAdiCtr = QPointF(120.0, 120.0)
    
    self.m_backZ = -30
    self.m_faceZ = -20
    self.m_ringZ = -10
    self.m_caseZ = 10
    
    self.reset()
    
    self.m_scene = QGraphicsScene(self)
    self.setScene(self.m_scene)
    self.m_scene.clear()
    
    self.init()
    
    self.setStyleSheet("background:transparent;border:0px")
    self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    
    
  
  def init(self):
    self.m_scaleX = self.width() / self.m_originalWidth
    self.m_scaleY = self.height() / self.m_originalHeight
    self.reset()
    
    self.m_itemBack = QGraphicsSvgItem(FILE_PATH + 'adi_back.svg')
    self.m_itemBack.setCacheMode(QGraphicsSvgItem.CacheMode.NoCache)
    self.m_itemBack.setZValue(self.m_backZ)
    self.m_itemBack.setTransform(QTransform.fromScale(self.m_scaleX, self.m_scaleY), True)
    self.m_itemBack.setTransformOriginPoint(self.m_originalAdiCtr)
    self.m_scene.addItem(self.m_itemBack)
    
    self.m_itemFace = QGraphicsSvgItem(FILE_PATH + 'adi_face.svg')
    self.m_itemFace.setCacheMode(QGraphicsSvgItem.CacheMode.NoCache)
    self.m_itemFace.setZValue(self.m_faceZ)
    self.m_itemFace.setTransform(QTransform.fromScale(self.m_scaleX, self.m_scaleY), True)
    self.m_itemFace.setTransformOriginPoint(self.m_originalAdiCtr)
    self.m_scene.addItem(self.m_itemFace)
    
    self.m_itemRing = QGraphicsSvgItem(FILE_PATH + 'adi_ring.svg')
    self.m_itemRing.setCacheMode(QGraphicsSvgItem.CacheMode.NoCache)
    self.m_itemRing.setZValue(self.m_ringZ)
    self.m_itemRing.setTransform(QTransform.fromScale(self.m_scaleX, self.m_scaleY), True)
    self.m_itemRing.setTransformOriginPoint(self.m_originalAdiCtr)
    self.m_scene.addItem(self.m_itemRing)
    
    self.m_itemCase = QGraphicsSvgItem(FILE_PATH + 'adi_case.svg')
    self.m_itemCase.setCacheMode(QGraphicsSvgItem.CacheMode.NoCache)
    self.m_itemCase.setZValue(self.m_caseZ)
    self.m_itemCase.setTransform(QTransform.fromScale(self.m_scaleX, self.m_scaleY), True)
    self.m_scene.addItem(self.m_itemCase)
  
    self.centerOn(self.width() / 2.0 , self.height() / 2.0)
    self.updateView()

  def reset(self):
    self.m_itemBack = 0
    self.m_itemFace = 0
    self.m_itemRing = 0
    self.m_itemCase = 0
    
    self.m_roll = 0.0
    self.m_pitch = 0.0
    
    self.m_faceDeltaX_new = 0.0
    self.m_faceDeltaX_old = 0.0
    self.m_faceDeltaY_new = 0.0
    self.m_faceDeltaY_old = 0.0
    
  def updateView(self):
    self.m_scaleX = self.width() / self.m_originalWidth
    self.m_scaleY = self.height() / self.m_originalHeight
    
    self.m_itemBack.setRotation(-self.m_roll)
    self.m_itemFace.setRotation(-self.m_roll)
    self.m_itemRing.setRotation(-self.m_roll)
    
    roll_rad = math.pi * self.m_roll / 180.0
    delta = self.m_originalPixPerDeg * self.m_pitch
    
    self.m_faceDeltaX_new = self.m_scaleX * delta * math.sin(roll_rad)
    self.m_faceDeltaY_new = self.m_scaleY * delta * math.cos(roll_rad)
    
    self.m_itemFace.moveBy(self.m_faceDeltaX_new - self.m_faceDeltaX_old, self.m_faceDeltaY_new - self.m_faceDeltaY_old)
    self.m_scene.update()
    
  def update(self):
    self.updateView()
    self.m_faceDeltaX_old = self.m_faceDeltaX_new
    self.m_faceDeltaY_old = self.m_faceDeltaY_new
  
  def setRoll(self, roll):
    self.m_roll = roll
    if self.m_roll < -180.0:
      self.m_roll = -180.0
    if self.m_roll > 180.0:
      self.m_roll = 180
    self.update()
  
  def get_roll(self):
    return self.m_roll
  
  def setPitch(self, pitch):
    self.m_pitch = pitch
    if self.m_pitch < -25.0:
      self.m_pitch = -25.0
    if self.m_pitch > 25.0:
      self.m_pitch = 25.0
    self.update()
    
  def getPitch(self):
    return self.m_pitch
    
  def sizeHint(self):
    super().sizeHint()
    return QSize(200, 200)
  
  def minimumSizeHint(self):
    return QSize(30, 30)
  
  def resizeEvent(self, event) -> None:
    super().resizeEvent(event)
    self.reInit()
    
  def reInit(self):
    if self.m_scene is not None:
      self.m_scene.clear()
      self.init()