#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:51:32 2020
Custom function collection for data proccessing
@author: user
"""

# Create list from CSV file
def dq_csv_to_list(csv_file_name):
    from csv import reader
    opened_file = open(csv_file_name)
    read_file = reader(opened_file)
    apps_data = list(read_file)
    opened_file.close
    return apps_data

# Create frequency table (dictionary) from list
def dq_list_to_freq_table(data_set, index = 0, exclude_first_row = True):
    freq_table = {}  
    if exclude_first_row:
        first_row = 1
    else:
        first_row = 0    
    for row in data_set[first_row:]:
        key = row[index]
        if key in freq_table:
            freq_table[key] += 1
        else:
            freq_table[key] = 1         
    return freq_table

# Find the distance between two points
def dq_two_points_dist(x_1, y_1, x_2, y_2):
    from math import sqrt
    return sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)

# Finds the closest point from the CSV list
# dependencies: dq_csv_to_list(), dq_two_points_dist()    
def dq_find_closest_point(x1, y1, x2_index, y2_index, csv_file_name, exclude_first_row = True):
    coordinates_list = dq_csv_to_list(csv_file_name)
    
    for row in coordinates_list[1:]:
        x2 = float(row[x2_index])
        y2 = float(row[y2_index])
        if 'dist' in locals():
            current_distance = dq_two_points_dist(x1, y1, x2, y2)
            if current_distance < distance:
                distance = current_distance
                result = row
        else:
            distance = dq_two_points_dist(x1, y1, x2, y2) 
            result = row
    return result



#### Test these functions ####
    
#apps_data = dq_csv_to_list('AppleStore.csv')
#ratings_ft = dq_list_to_freq_table(apps_data, 7)

#print(genres_fq)
#print(ratings_ft)

# provided coordinates input

    
closest_restaurant = dq_find_closest_point(100, 100, 4, 5, 'FastFoodRestaurants.csv')
print(closest_restaurant)