# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2021/10/14 10:15
Author : Dufy
Email : 813540660@qq.com
File : engine.py

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
from cruise import CruiseControl
from ignition import IgnitionControl


class Engine:
    IgnitionControl = IgnitionControl()
    CruiseControl = CruiseControl(IgnitionControl)

    def __init__(self):
        pass

    def __get_ignition_control(self):
        return self.IgnitionControl

    # def __get_control(self):
    #     self.CruiseControl
    #     IgnitionControl.set_RPM(10)

