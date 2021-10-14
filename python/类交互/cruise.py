# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2021/10/14 10:17
Author : Dufy
Email : 813540660@qq.com
File : cruise.py

...
==============================================================================      
"""


class CruiseControl:
    def __init__(self, ignition):
        self.__ignition = ignition

    def set_cruise_speed(self, veloty):
        """
        注意，这里CruiseControl 对象需要调用 IgnitionControl的方法，参考 '类结构图.png'
        :param veloty:
        :return:
        """
        print(f'cruise speed now is : {veloty}')
        self.__ignition.get_RPM()
        self.__ignition.set_RPM(10)
        self.__ignition.get_RPM()



