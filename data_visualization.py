# Data Visualization
''' There are 2 primary uses for data visualization
1) To explore data
2) To communicate data
'''

import matplotlib.pyplot as plt

# line chart
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color="green", marker="o", linestyle="solid")
plt.title("Nominal GDP")
plt.ylabel("Billions of $")

# Bar chart
import matplotlib.pyplot as plt
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# plt.bar(movies, num_oscars)  # Joel has a different idea
xs = [i for i,_  in enumerate(movies)]
plt.bar(xs, num_oscars)
plt.ylabel("# of Academy Awards")
plt.title("My Favorite Movies")

# Used to mark the ticks and the labels associated with them.
plt.xticks([i for i,_ in enumerate(movies)], movies)

# Bar chart for bucketed numerical values (essentially plotting histograms)
import matplotlib.pyplot as plt
import numpy as np
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
# Assigning a lambda function to a variable
decile = lambda grade: (grade // 10) * 10
from collections import Counter
histogram = Counter(decile(grade) for grade in grades)
# The third argument of plt.bar specifies the bar width
plt.bar(histogram.keys(), histogram.values(), 8)
plt.title("Distribution of Exam 1 Grades")
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.xticks(list(np.arange(0, 110, 10)), list(np.arange(0, 110, 10)))
plt.yticks([x for x in range(6)], [x for x in range(6)])
# Determines the size of the axis in the x and y axes
plt.axis([-5, 105, 0, 5])

# y axis in the plot should always begin with zero. Otherwise it could mislead the viewer
# one misleading example
import matplotlib.pyplot as plt
mentions = [500, 505]
years = [2013, 2014]
plt.bar(years, mentions, 0.8)
plt.ylabel("# of times I heard someone say 'data science'")
plt.title("Look at the 'Huge' Increase!")
plt.xticks([2013, 2014], [2013, 2014])
plt.axis([2012.5, 2014.5, 499, 506])
plt.ticklabel_format(useOffset=False)

# Line Charts
import matplotlib.pyplot as plt
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias_squared, 'r-', label='bias^2')
plt.plot(xs, total_error, 'b:', label='total_error')

plt.legend(loc = 9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")

# Scatterplots
# Right choice to visualize relationship between two paired sets of data.
import matplotlib.pyplot as plt
friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label, xy=(friend_count, minute_count), xytext=(5, -5), textcoords = 'offset points')

plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.title("Daily Minutes vs. Number of Friends")

# If you're scattering comparable variables, you might get a misleading picture if you
# let matplotlib choose the scale

test_l_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]

plt.scatter(test_l_grades, test_2_grades)
plt.title("Axes Aren't Comparable")
plt.xlabel('test 1 grade')
plt.ylabel('test 2 grade')
plt.axis('equal')





























