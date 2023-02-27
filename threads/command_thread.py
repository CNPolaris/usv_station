# -*- coding: utf-8 -*-
################################################################################
# Author: tianxin
# Date: 2023-02-27
# 地面站控制模块线程
################################################################################
import socket
from PySide6 import QtCore

from utils.config import config

class CommandThread(QtCore.QThread):
  send_connect_flag_signal = QtCore.Signal(int)
  send_destroy_flag_signal = QtCore.Signal(int)

  def __init__(self) -> None:
    super().__init__()
    self.command_sock = None
    self.connect_flag = False
    
  def run(self) -> None:
    try:
      self.command_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.command_sock.connect((config.get_tcp_server_ip(), config.get_tcp_server_port()))
      self.command_sock.send(bytes(config.get_connect_key(), encoding='utf8'))
      self.send_connect_flag_signal.emit(1)  #连接成功
      self.connect_flag = True
    except:
      print("连接服务器失败")
      self.send_connect_flag_signal.emit(0)  #连接失败
      
  def destroy(self):
    """关闭服务器连接"""
    if self.connect_flag:
      self.command_sock.close()
      self.send_destroy_flag_signal.emit(1)  #关闭成功
      self.connect_flag = False