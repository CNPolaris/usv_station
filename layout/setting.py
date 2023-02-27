# -*- coding: utf-8 -*-
################################################################################
# Author: tianxin
# Date: 2023-02-26
# 配置界面
################################################################################
import os
from PySide6.QtWidgets import QWidget

from ui.ui_setting import Ui_SettingForm
from utils.config import config

class SettingWidget(QWidget):
  def __init__(self) -> None:
    super().__init__()
    self.setting_form = Ui_SettingForm()
    self.setting_form.setupUi(self)
    self.setWindowTitle("系统配置")
    self.load_setting_cfg()
    # 配置信息复选框选中事件绑定
    self.setting_form.override_server_info.stateChanged.connect(lambda: self.on_check_override_server_info(self.setting_form.override_server_info))
    self.setting_form.override_monitor_code.stateChanged.connect(lambda: self.on_check_override_monitor_code(self.setting_form.override_monitor_code))
    self.setting_form.override_monitor_url.stateChanged.connect(lambda: self.on_check_override_monitor_url(self.setting_form.override_monitor_url))
    self.setting_form.override_access_key.stateChanged.connect(lambda: self.on_check_override_access_key(self.setting_form.override_access_key))
    # 按钮事件绑定
    self.setting_form.reset_cfg_btn.clicked.connect(self.on_reset_btn_clicked)
    self.setting_form.save_cfg_btn.clicked.connect(self.on_save_btn_clicked)
    self.setting_form.cancel_cfg_btn.clicked.connect(self.on_cancel_btn_clicked)
    
  def load_setting_cfg(self):
    """load_setting_cfg 载入setting.cfg配置文件
    """
    cfg = config.get_all_setting_cfg()
    self.setting_form.server_ip_text.setPlainText(cfg['tcp_ip'])
    self.setting_form.server_port_text.setPlainText(cfg['tcp_port'])
    self.setting_form.monitor_url_text.setPlainText(cfg['monitor_url'])
    self.setting_form.monitor_code_text.setPlainText(cfg['monitor_key'])
    self.setting_form.access_key_text.setPlainText(cfg['access_key'])
    self.set_setting_text_no_edit()
    
  def set_setting_text_no_edit(self):
    """设置配置文件不可修改"""
    self.setting_form.server_ip_text.setDisabled(True)
    self.setting_form.server_port_text.setDisabled(True)
    self.setting_form.monitor_url_text.setDisabled(True)
    self.setting_form.monitor_code_text.setDisabled(True)
    self.setting_form.access_key_text.setDisabled(True)
    
  def on_check_override_server_info(self, state):
    """根据选中状态切换可编辑状态"""
    if state.isChecked():
      self.setting_form.server_ip_text.setDisabled(False)
      self.setting_form.server_port_text.setDisabled(False)
    else:
      self.setting_form.server_ip_text.setDisabled(True)
      self.setting_form.server_port_text.setDisabled(True)
  
  def on_check_override_monitor_code(self, state):
    """根据选中状态切换可编辑状态"""
    if state.isChecked():
      self.setting_form.monitor_code_text.setDisabled(False)
    else:
      self.setting_form.monitor_code_text.setDisabled(True)
      
  def on_check_override_monitor_url(self, state):
    """根据选中状态切换可编辑状态"""
    if state.isChecked():
      self.setting_form.monitor_url_text.setDisabled(False)
    else:
      self.setting_form.monitor_url_text.setDisabled(True)

  def on_check_override_access_key(self, state):
    """根据选中状态切换可编辑状态"""
    if state.isChecked():
      self.setting_form.access_key_text.setDisabled(False)
    else:
      self.setting_form.access_key_text.setDisabled(True)

  def on_reset_btn_clicked(self):
    """重置配置文件"""
    config.reset_config_data()
  
  def on_save_btn_clicked(self):
    """保存配置文件"""
    cfg = {}
    cfg['tcp_ip'] = self.setting_form.server_ip_text.toPlainText()
    cfg['tcp_port'] = self.setting_form.server_port_text.toPlainText()
    cfg['monitor_url'] = self.setting_form.monitor_url_text.toPlainText()
    cfg['monitor_key'] = self.setting_form.monitor_code_text.toPlainText()
    cfg['access_key'] = self.setting_form.access_key_text.toPlainText()
    config.save_config_data(cfg)
  
  def on_cancel_btn_clicked(self):
    """退出配置"""
    self.close()
