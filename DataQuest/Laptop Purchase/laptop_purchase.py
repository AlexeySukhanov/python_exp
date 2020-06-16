#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Laptop Purchase
Created on Tue Jun 16 04:24:30 2020

@author: user
"""

# Get data
from csv import reader
opened_file = open('laptops.csv')
read_file = reader(opened_file)
laptops_list = list(read_file)
opened_file.close()

# Create dictionary
price_to_name = {}
for row in laptops_list[1:]:
    price = int(row[2])
    name = row[1]
    if price not in price_to_name:
        price_to_name[price] = [name]
    else:
        price_to_name[price].append(name)

# Find pair with 5000 total costs
for price1 in price_to_name:
    for price2 in price_to_name:
        if  price1 + price2 == 5000:
            laptop1 = price_to_name[price1][0]
            if price1 != price2:
                laptop2 = price_to_name[price2][0]
            else:
                 laptop2 = price_to_name[price2][1]

print(laptop1)
print(laptop2)