#encoding:utf-8

'''
读取excel 中的文件
将excelo中的两个数据合并到一起
课程， 人数，学习时间
pip install openpyxl
Looking in indexes: http://pypi.douban.com/simple
Collecting openpyxl
  Downloading http://pypi.doubanio.com/packages/f4/5f/fb8706fba43b46716e252fdd3ffdfe801a63a0f4663b80b6f3421d85ab70/openpyxl-3.0.2.tar.gz (172kB)
     |████████████████████████████████| 174kB 1.1MB/s
ERROR: Package 'openpyxl' requires a different Python: 3.5.3 not in '>=3.6,
python -V
Python 3.5.3

'''

from openpyxl import load_workbook # 可以用来载入已有数据表格
from openpyxl import Workbook # 可以用来处理新的数据表格
import datetime # 可以用来处理时间相关的数据

def combine():
    '''
    该函数可以用来处理原数据文件：
    1. 合并表格并写入的 combine 表中
    2. 保存原数据文件
    '''
    TODO

def split():
    '''
    该函数可以用来分割文件：
    1. 读取 combine 表中的数据
    2. 将数据按时间分割
    3. 写入不同的数据表中
    '''
    TODO

# 执行
if __name__ == '__main__':
    combine()
    split()