# -*- coding: utf-8 -*-
################################################################################
# Author: tianxin
# Date: 2023-01-29
# 配置读取
################################################################################
import os
import datetime

# -*- encoding=utf8 -*-
__author__ = "tian.xin"

import os
import operator
from configparser import RawConfigParser

BASE_DIR = os.path.abspath(os.path.dirname(__file__)).split('utils')[0]


class Config(object):
    """
    读取配置文件
    """

    def __init__(self) -> None:
        # 工程文件路径
        self.project_path = BASE_DIR
        # 配置文件路径
        self._config_path = self.project_path + "setup.cfg"
        self._config_copy_path = self.project_path + "setup_copy.cfg"
        print(self._config_path)
        self.config_parser = RawConfigParser()
        self.config_parser.read(self._config_path, 'utf-8')  # 读取配置文件所有信息

    def get_config_data(self, option='', section='common_info'):
        """get_config_data 按条件返回某条 setup.cfg 值

        Parameters
        ----------
        section: str
            橙色标题名
        option: str
            参数名

        Returns
        -------
        value: str
            按条件返回某条 setup.cfg 值
        """
        return self.config_parser.get(section, option)
    
    def set_config_data(self, section='', option='',  data=''):
        """set_config_data 修改某一项的值

        Parameters
        ----------
        section : str, optional
            _description_, by default ''
        option : str, optional
            _description_, by default ''
        data : str, optional
            _description_, by default ''
        """
        self.config_parser.set(section=section, option=option, value=data)
        
    def reset_config_data(self):
        """重置配置文件到初始状态"""
        with open(self._config_copy_path, 'r') as f1:
            with open(self._config_path, 'w') as f2:
                    for line in f1:
                        f2.write(line)
        
    def join_absolute_path(self, relative_path) -> str:
        """join_absolute_path 拼接全局路径

        Parameters
        ----------
        relative_path : str
            相对路径

        Returns
        ----------
        absolute_path: str
            拼接后的绝对路径
        """
        absolute_path = self.project_path + relative_path
        return absolute_path

    @staticmethod
    def get_tcp_server_ip() -> str:
        """get_server_ip 获取配置文件中的监听ip
        """
        ip = config.get_config_data("tcp_ip", section="system-config")
        return ip

    @staticmethod
    def get_tcp_server_port() -> int:
        """get_server_ip 获取配置文件中的监听port
        """
        port = config.get_config_data("tcp_port", section="system-config")
        return int(port)

    @staticmethod
    def get_monitor_url():
        """get_monitor_url 获取推流地址

        Returns
        -------
        _type_
            _description_
        """
        monitor_url = config.get_config_data("monitor_url", section="system-config")
        return monitor_url
    
    @staticmethod
    def get_monitor_flv():
        """get_monitor_flv 获取监控拉流地址

        Returns
        -------
        _type_
            _description_
        """
        monitor_flv = config.get_config_data("monitor_flv", section="system-config")
        return monitor_flv
    
    @staticmethod
    def get_access_key():
        """获取注册包

        Returns
        -------
        _type_
            _description_
        """
        access_key = config.get_config_data("access_key", section="device")
        return access_key
    
    @staticmethod
    def get_monitor_key():
        """获取推流码"""
        monitor_code = config.get_config_data("monitor_key", section="device")
        return monitor_code
    
    @staticmethod
    def get_log_status():
        status = config.get_config_data("open", section="log")
        if status == "true":
            return True
        else:
            return False
        
    @staticmethod
    def get_all_setting_cfg() -> dict:
        """get_all_setting_cfg 获取所有的配置信息

        Returns
        -------
        dict
            获取所有的配置信息
        """
        cfg = {}
        cfg['tcp_ip'] = config.get_tcp_server_ip()
        cfg['tcp_port'] = str(config.get_tcp_server_port())
        cfg['monitor_url'] = config.get_monitor_url()
        cfg['monitor_flv'] = config.get_monitor_flv()
        cfg['monitor_key'] = config.get_monitor_key()
        cfg['access_key'] = config.get_access_key()
        return cfg
    
    def save_config_data(self, cfg):
        """保存修改后的配置文件"""
        config.set_config_data("system-config", "tcp_ip", cfg['tcp_ip'])
        config.set_config_data("system-config", "tcp_port", cfg['tcp_port'])
        config.set_config_data("system-config", "monitor_url", cfg['monitor_url'])
        config.set_config_data("system-config", "monitor_key", cfg['monitor_key'])
        config.set_config_data("device", "access_key", cfg['access_key'])
        with open(self._config_path, 'w') as config_file: self.config_parser.write(config_file)

config = Config()

if __name__ == "__main__":
    print(BASE_DIR)
    print(config.get_all_setting_cfg())
    config.set_config_data("device", "monitor_key", "test")

