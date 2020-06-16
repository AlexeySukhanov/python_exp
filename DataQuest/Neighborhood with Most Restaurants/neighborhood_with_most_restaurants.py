#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Neighborhood with Most Restaurants
Created on Tue Jun 16 03:08:38 2020

@author: user
"""

# Get data
from csv import reader
opened_file = open('restaurants.csv')
read_file = reader(opened_file)
restaurants_list = list(read_file)
opened_file.close()

# Find neighborhood with most restaurants count
restaurants_ft = {}
most_restaurants_count = 0
most_restaurants = ''
for row in restaurants_list[1:]:
    neighborhood = row[1]
    if neighborhood in restaurants_ft:
        restaurants_ft[neighborhood] += 1
    else:
        restaurants_ft[neighborhood] = 1
    if restaurants_ft[neighborhood] > most_restaurants_count:
        most_restaurants_count = restaurants_ft[neighborhood]
        most_restaurants = neighborhood;
        
print('neighborhood with most restaurants count: ' + most_restaurants)