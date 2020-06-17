#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Find The Closest Restaurant
Created on Wed Jun 17 16:07:49 2020

@author: user
"""

# provided coordinates input
x = 100
y = 100 

def distance(x_1, y_1, x_2, y_2):
    from math import sqrt
    return sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)

def closest_restaurant(x_1, y_1):
    from csv import reader
    opened_file = open('FastFoodRestaurants.csv')
    read_file = reader(opened_file)
    restaurants_list = list(read_file)
    opened_file.close()
    for row in restaurants_list[1:]:
        x_2 = float(row[4])
        y_2 = float(row[5])
        if 'dist' in locals():
            current_dist = distance(x_1, y_1, x_2, y_2)
            if current_dist < dist:
                dist = current_dist
                result = row[0]
        else:
            dist = distance(x_1, y_1, x_2, y_2) 
            result = row[0]
    return result
    
closest_restaurant_name = closest_restaurant(100, 100)
print(closest_restaurant_name)