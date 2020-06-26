#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test matplotlib
Created on Thu Jun 18 01:16:21 2020

@author: user
"""
from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010] # годы
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3] #ВВП
gdp_2 = [500.2, 543.3, 1075.9, 2862.5, 5979.6, 8289.7, 14958.3] #ВВП

# Создать ленейную диаграмму: годы по оси X, ВВП по оси Y
plt.plot(years, gdp, color='red', marker='o', linestyle='solid')
plt.plot(years, gdp_2, color='green', marker='o', linestyle=':')

# Добавить название диаграммы
plt.title("Номинальны ВВП")

# Добавить подпись к осям Y, X
plt.ylabel("Млрд $")
plt.xlabel('Годы')

# Показать диаграмму
#plt.show()

# Сохранить диаграмму 
plt.savefig('lol')



