# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2021/10/14 10:16
Author : Dufy
Email : 813540660@qq.com
File : ignition.py

...
==============================================================================      
"""

import traceback
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import time


class IgnitionControl:
    pass
    def __init__(self):
        self.rpm = 0

    def set_RPM(self, rpm):
        self.rpm = rpm

    def get_RPM(self):
        print(f'当前 RPM 值为：{self.rpm}')
        return self.rpm

    def __print(self):
        print('ssss')

