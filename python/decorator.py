# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2022/1/2 1:25 下午
Author : Dufy
Email : 813540660@qq.com
File : decorator.py


==============================================================================
"""
import traceback
from utils import *


@cal_time
def binary_search(li, val):
    left = 0
    right = len(li)-1
    while left <= right:  # 候选区有值
        pass
        mid = (left+right)//2
        if li[mid]==val:
            return mid
        elif li[mid]>val:  # 待查找的值在 mid 左侧
            right = mid-1
        else: # 待查找的值在 mid 右侧
            left = mid+1
    return None


li = list(range(1,10))
print(li)
print(binary_search(li, 3))