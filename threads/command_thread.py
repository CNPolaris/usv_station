# -*- coding: utf-8 -*-
################################################################################
# Author: tianxin
# Date: 2023-02-27
# 地面站控制模块线程
################################################################################
import socket
import struct
import json
import subprocess

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
    except:
      print("连接服务器失败")
      self.send_connect_flag_signal.emit(0)  #连接失败
      
  def destroy(self):
    """关闭服务器连接"""
    self.send_msg_tcp_server(bytes("-1", encoding='utf-8'))
    self.command_sock.close()
    self.send_destroy_flag_signal.emit(1)  #关闭成功
    self.quit()
    
  def send_left_accelerator_to_dtu(self, left):
    """发送左油门信号到DTU"""
    # self.command_sock.send(bytes(str(left), encoding='utf8'))
    data = self.to_modbus_rtu(left)
    # 制作报头
    header_dic = {
        'total_size': len(data)  # 总共的大小
    }
    header_json = json.dumps(header_dic) #字符串类型
    header_bytes = header_json.encode('utf-8')  #转成bytes类型(但是长度是可变的)
    # #先发报头的长度
    self.command_sock.send(struct.pack('i',len(header_bytes))) #发送固定长度的报头
    # #再发报头
    self.command_sock.send(header_bytes)
    # #最后发命令的结果
    self.command_sock.send(data)
    
  def send_right_accelerator_to_dtu(self, right):
    """发送右油门信号到DTU"""
    data = self.to_modbus_rtu(right)
    # 制作报头
    header_dic = {
        'total_size': len(data)  # 总共的大小
    }
    header_json = json.dumps(header_dic) #字符串类型
    header_bytes = header_json.encode('utf-8')  #转成bytes类型(但是长度是可变的)
    # #先发报头的长度
    self.command_sock.send(struct.pack('i',len(header_bytes))) #发送固定长度的报头
    # #再发报头
    self.command_sock.send(header_bytes)
    # #最后发命令的结果
    self.command_sock.send(data)
  
  @staticmethod
  def to_modbus_rtu(data):
    return bytes(f"01 04 00 00 00 04 F1 {data}", encoding='utf-8')
  
  def send_msg_tcp_server(self, data):
    # 制作报头
    header_dic = {
        'total_size': len(data)  # 总共的大小
    }
    header_json = json.dumps(header_dic) #字符串类型
    header_bytes = header_json.encode('utf-8')  #转成bytes类型(但是长度是可变的)
    # #先发报头的长度
    self.command_sock.send(struct.pack('i',len(header_bytes))) #发送固定长度的报头
    # #再发报头
    self.command_sock.send(header_bytes)
    # #最后发命令的结果
    self.command_sock.send(data)