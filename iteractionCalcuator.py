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

number_of_replications = 1

total = total * number_of_replications

# Now calculate the amount of time

avg_time_seconds = 1

avg_time_minutes = avg_time_seconds / 60

avg_time_hours = avg_time_minutes / 60

time_hours = avg_time_hours * total

time_days = time_hours / 24

time_years = time_days / 365

print("Overall there are %d simulations" % total)
print("Assuming 1s per simulation, this will take %d hours" % time_hours)
print("Assuming 1s per simulation, this will take %d days" % time_days)
print("Assuming 1s per simulation, this will take %d years" % time_years)
