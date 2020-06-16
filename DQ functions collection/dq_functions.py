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



# Test these functions:
apps_data = dq_csv_to_list('AppleStore.csv')
ratings_ft = dq_list_to_freq_table(apps_data, 7)

#print(genres_fq)
print(ratings_ft)