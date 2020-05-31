#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 19:25:32 2020

@author: user
"""

# Degree Centrality
# Центральность по степени узлов

from __future__ import division
import pprint


users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


# Создаем список дврузей
for user in users:
    user["friends"] = []

# Добавляем массив друзей к каждому пользователю   
for i, j in friendships:
    users[i]["friends"].append(users[j]["id"])
    users[j]["friends"].append(users[i]["id"])
    
pprint.pprint(users)    

# Число связей одного пользователя
def number_of_friends(user):
    return len(user["friends"])

# Число связей всех пользователей
#total_connections = sum( number_of_friends(user) for user in users)
total_connections = 0
for user in users:
    total_connections += number_of_friends(user)        
print('total_connections: ', total_connections)

# Среднее число связей
num_users = len(users) # Колличество пользователей
print('num_users: ',num_users)
avg_connections = total_connections / num_users
print('avg_conntctions: ', avg_connections)

# Число друзей для каждого пользователя
# Создать список в формате (id пользователя, колличество друзей)\
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print('num_friends_by_id: ', num_friends_by_id)

# Упорядочить список по полю num_friends в убывающем порядке
num_friends_by_id = sorted(num_friends_by_id, key=lambda(user_id, num_friends):
                            num_friends, reverse=True)
print('num_friends_by_id: ', num_friends_by_id)    












