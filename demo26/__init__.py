# -*- coding:utf-8 -*-
# Author: 李泽军
# Date: 2020/1/26 9:26 PM
# Project: flask-demo

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
print(curPath)
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)