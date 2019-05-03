from __future__ import division
import operator
import pandas as pd
import numpy as np


# all available users
users = [
    {"id":0, "name":"Hero"},
    {"id":1, "name":"Dunn"},
    {"id":2, "name":"Sue"},
    {"id":3, "name":"Chi"},
    {"id":4, "name":"Thor"},
    {"id":5, "name":"Clive"},
    {"id":6, "name":"Hicks"},
    {"id":7, "name":"Devin"},
    {"id":8, "name":"Kate"},
    {"id":9, "name":"Klein"}
]

# friendship network
friendships = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),
               (4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

for user in users:
    user["friends"] = []

for i,j in friendships:
    users[i]["friends"].append(users[j]) # add j as a friend of i
    users[j]["friends"].append(users[i]) # add i as a friend of j

def number_of_friends(user):
    '''
    how many friends does an user have.
    '''
    return len(user["friends"])

total_connections = sum([number_of_friends(user) for user in users])
print(total_connections)


num_users = len(users)
avg_connections = total_connections / num_users

# create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

# sort the list of tuples(num_friends_by_id) in descending order based on 2nd element
# num_friends_by_id.sort(key=operator.itemgetter(1), reverse=True)
# print(num_friends_by_id)

# network metric degree centrality
sorted(num_friends_by_id, key=operator.itemgetter(1), reverse=True)


















