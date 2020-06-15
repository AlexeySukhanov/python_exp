#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Most Popular Apps
Created on Mon Jun 15 03:21:38 2020

@author: user
"""

# Prepare dataset
from csv import reader
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

# Find min & max
rating_count_tot = []
for row in apps_data[1:]:
    rating_count = float(row[5])
    rating_count_tot.append(rating_count)
ratings_min = min(rating_count_tot)
ratings_max = max(rating_count_tot)

# Create intervals points list
ratings_interval_list = []
step = ratings_max // 5
for i in range(1,5):
    ratings_interval_list.append(int(step * i))

# Create keys intervals dictionary
ratings_interval_dic = {}
for i in range(len(ratings_interval_list) + 1):
    if i == 0:
        key = str(int(ratings_min)) + ' - ' + str(ratings_interval_list[i])
    elif i == len(ratings_interval_list):
        key = str(ratings_interval_list[-1]) + ' +'
    else:
        key = str(ratings_interval_list[i-1]) + ' - ' + str(ratings_interval_list[i])   
    ratings_interval_dic[key] = 0

#Count the frequency of each intervals
for rating in rating_count_tot:
    if rating <= 594935:
        ratings_interval_dic['0 - 594935'] += 1
    elif 594935 < rating <= 1189870:
        ratings_interval_dic['594935 - 1189870'] += 1
    elif 1189870 < rating <= 1784805:
        ratings_interval_dic['1189870 - 1784805'] += 1
    elif 1784805 < rating <= 2379740:
        ratings_interval_dic['1784805 - 2379740'] += 1
    elif rating > 2379740:
        ratings_interval_dic['2379740 +'] += 1
        
print(ratings_interval_dic)

#Create most popular apps list
most_popular = apps_data[:1]
for row in apps_data[1:]:
    rating_count = float(row[5])
    if rating_count >= 594935:
        most_popular.append(row)

for row in most_popular:
    print(row)