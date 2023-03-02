# -*- coding: utf-8 -*-
################################################################################
# Author: tianxin
# Date: 2023-02-27
# 地面站数据接收模块线程
################################################################################
import socket
import struct
import json

from PySide6.QtCore import QThread, Signal

from utils.config import config
from utils.logger import logger

class StationThread(QThread):
  send_connect_flag_signal = Signal(int)  # 1:成功 0: 失败
  def __init__(self) -> None:
    super().__init__()
    self.station_sock = None
  
  def run(self) -> None:
    try:
      self.station_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.station_sock.connect((config.get_tcp_server_ip(), config.get_tcp_server_port()))
      self.station_sock.send(bytes(config.get_connect_key(s="station"), encoding='utf-8'))
      # self.send_connect_flag_signal.emit(1)
      while True:
        recv_data = self.station_sock.recv(256)
        print(recv_data)
    except:
      logger.error("[地面站-数据接收]连接TCP服务器失败")
      self.send_connect_flag_signal.emit(0)
      
  def destroy(self):
    self.send_msg_tcp_server(bytes("-1", encoding='utf-8'))
    self.station_sock.close()
    self.quit()
  
  def send_msg_tcp_server(self, data):
    # 制作报头
    header_dic = {
        'total_size': len(data)  # 总共的大小
    }
    header_json = json.dumps(header_dic) #字符串类型
    header_bytes = header_json.encode('utf-8')  #转成bytes类型(但是长度是可变的)
    # #先发报头的长度
    self.station_sock.send(struct.pack('i',len(header_bytes))) #发送固定长度的报头
    # #再发报头
    self.station_sock.send(header_bytes)
    # #最后发命令的结果
    self.station_sock.send(data)