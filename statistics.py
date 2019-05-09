# Statistics
import random
from collections import Counter
import matplotlib.pyplot as plt

num_friends = [random.randrange(10, 100, 1) for _ in range(10000)]
friend_counts = Counter(num_friends)
plt.bar(friend_counts.keys(), friend_counts.values())
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.title("Histogram of Friend Counts")

sorted_values = sorted(num_friends)
sorted_values[-1]

# Central Tendencies
def mean(x):
    return sum(x)/len(x)

mean(num_friends)

def kar_median(v):
    n = len(v)
    sorted_v = sorted(v)
    if n % 2 == 0:
        # vector with even number of elements
        hi = int(n/2)
        return ((sorted_v[hi] + sorted_v[hi - 1])/2)
    else:
        # vector with odd number of elements
        return sorted_v[int((n - 1)/2)]

def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return(sorted_v[lo] + sorted_v[hi]) / 2

vec = [4, 1, 6, 8, 3, 2, 0, 12, 5, 17]
kar_median(vec)
median(vec)

def quantile(v, p):
    '''returns the pth-percentile value in x'''
    p_index = int(len(v)  * p)
    return sorted(v)[p_index]

vec = [4, 1, 6, 8, 3, 2, 0, 12, 5, 17]
quantile(vec, 0.8)

from collections import Counter
def mode(v):
    dict = Counter(v)
    max_freq = max(dict.values())
    return [key for key, value in dict.items() if value == max_freq]

vec = [4, 1, 6, 8, 3, 2, 0, 12, 5, 17, 1, 8]
mode(vec)

# Dispersion

def data_range(v):
    return max(v) - min(v)

vec = [4, 1, 6, 8, 3, 2, 0, 12, 5, 17, 1, 8]
print(data_range(vec))

# Calculation of variance
def mean(x):
    return sum(x)/len(x)

def dot(v, w):
    return sum([v_i * w_i for v_i, w_i in zip(v, w)])

def sum_of_squares(v):
    return dot(v, v)

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations)/(n - 1)

import numpy as np
def standard_deviation(x):
    return np.sqrt(variance(x))

def quantile(v, p):
    '''returns the pth-percentile value in x'''
    p_index = int(len(v)  * p)
    return sorted(v)[p_index]

def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)


vec = [4, 1, 6, 8, 3, 2, 0, 12, 5, 17, 1, 8]
variance(vec)
standard_deviation(vec)
interquartile_range(vec)


# Correlation
# Covariance - It is a paired analogue of variance

def covariance(x, y):
    # to find out covariance between x and y,
    # the length of vectors x and y must be of the same length.
    n = len(x)
    return dot(de_mean(x), de_mean(y))/(n - 1)

# Since covariance is a hard number to intrepret
# we often use correlation.

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)

    if (stdev_x > 0) and (stdev_y > 0):
        return covariance(x, y)/(stdev_x * stdev_y)
    else:
        return 0

































