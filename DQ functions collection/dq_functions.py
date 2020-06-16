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

# Extract one column from list to another new list
def dq_list_to_one_column(index, exclude_first_row = True):
    column = []    
    if exclude_first_row:
        first_row = 1
    else:
        first_row = 0
    for row in apps_data[first_row:]:
        value = row[index]
        column.append(value)    
    return column

# Create frequency table (dictionary) from one-column list
def dq_column_to_ft(one_column_list):
    ft = {}
    for key in one_column_list:
        if key in ft:
            ft[key] += 1
        else: 
            ft[key] = 1
    return ft


# Test thest functions:
apps_data = dq_csv_to_list('AppleStore.csv')
genres = dq_list_to_one_column(11, False)
genres_fq = dq_column_to_ft(genres)

print(genres_fq)