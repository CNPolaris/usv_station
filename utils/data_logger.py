# -*- coding: utf-8 -*-
################################################################################
# Author: tianxin
# Date: 2023-03-10
# 数据记录工具
################################################################################

import logging
from logging.handlers import RotatingFileHandler

from datetime import datetime
import os

# 文件目录
__now_time = datetime.now().strftime('%Y-%m-%d') 
cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))  # 当前项目路径
cache_path = os.path.join(cur_path, 'cache', __now_time)
if not os.path.exists(cache_path): os.mkdir(cache_path)


logger_gps = logging.getLogger('gps')
logger_gps.setLevel(logging.INFO)

handler_stream = logging.StreamHandler()

def set_logger():
  # gps数据记录
  gps_data_path = os.path.join(cache_path, __now_time + "-gps" + ".txt")
  handler_gps = RotatingFileHandler(filename=gps_data_path, maxBytes=30 * 1024 * 1024, backupCount=3,
                                        encoding='utf-8')
  handler_gps.setLevel(logging.INFO)
  logger_gps.addHandler(handler_gps)
  logger_gps.addHandler(handler_stream)
  
set_logger()

