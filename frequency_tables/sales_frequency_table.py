#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Sales frequency table
Created on Tue Jun 16 02:29:26 2020

@author: user
"""

from csv import reader
opened_file = open('sales.csv')
read_file = reader(opened_file)
sales_list = list(read_file)
opened_file.close()

sales = {}
for key_list in sales_list[1:]:
    key = key_list[0]
    if key in sales:
        sales[key] += 1
    else:
        sales[key] = 1

for name in sales:
    print(name + ': ' + str(sales[name]))
