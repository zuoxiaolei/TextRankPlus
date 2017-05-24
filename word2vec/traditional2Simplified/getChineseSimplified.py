# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 12:13:18 2016

@author: zuoxiaolei
"""

from langconv import *

def getSimple(line,fileWrite):
    line = Converter('zh-hans').convert(line.decode('utf-8'))
    line = line.encode('utf-8')
    fileWrite.write(line+'\n')

