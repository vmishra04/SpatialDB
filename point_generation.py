#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 20:34:00 2018

@author: vivekmishra
"""

#34.021273, -118.289154

import math
import os
os.chdir('/Users/vivekmishra/Desktop/')

path = 'cords.txt'
writer = open(path,'w')

R = 8 
r = 1
a = 4
t = 0.0
nRev = 16
while t < math.pi * nRev:
    x = ((R + r) * math.cos((r / R) * t) - a * math.cos((1 + r / R) * t))/1000
    x += 34.021273;
    y = ((R + r) * math.sin((r / R) * t) - a * math.sin((1 + r / R) * t))/1000
    y += -118.289154;
    print(str(y)+","+str(x)+",0")
    writer.write(str(y)+","+str(x)+",0\n")
    t += 0.01
    
writer.close()
