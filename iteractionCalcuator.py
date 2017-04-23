# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 13:43:09 2017

@author: JLane
"""

import pandas as pd


pathname = "C:\\Users\\JLane\\..."
file = "model-parameter-list.csv"
filepath = pathname + file
parameters = pd.read_csv(filepath)


total = 0
lp = len(parameters)
for i in range(0,lp):
    m1 = parameters['Min'][i]
    m2 = parameters['Max'][i]
    ms = parameters['Step'][i]
    if ms == 0:
        continue
    mfull = (m2 - m1) / ms
    if i == 0:
        total = mfull
    if i > 0:
        total = total * mfull

print(total)