# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2021/10/14 10:14
Author : Dufy
Email : 813540660@qq.com
File : Car.py
验证对象之间的交互
...
==============================================================================      
"""
from engine import Engine


class Car:
    Engine = Engine()


car = Car()
car.Engine.CruiseControl.set_cruise_speed(15)