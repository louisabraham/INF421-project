#!/usr/bin/env python3

"""
Special notes :
This implementation supports MULTIPLE shortest path.
(except for the number_of_possible_locations_with_mindist_simple function)
"""

import random

from Graph import Graph
from algo import *
from unused import *
from Dijkstra import *
from util import timeit
from reach import reach

####################
data = '/Users/louisabraham/Downloads/RoadNetworks/data/idf.in'
logging = '/Users/louisabraham/Downloads/RoadNetworks/vis/points.js'
hour = 3600000

# We can control the display of chronos using timeit.activated
timeit.activated = True
####################

# graph importation
g = Graph.from_file(data)

# we chose a random starting point
v = random.choice(list(g.keys()))

# Question 1.1
print(number_of_possible_locations(g, v, 1 * hour))

# the same result is computed
print(number_of_possible_locations_with_mindist_dijkstra(
    g, v, 1 * hour, 0))
print(number_of_possible_locations_with_mindist_dijkstra(
    g, v, 1 * hour, 0))

print(number_of_possible_locations_with_mindist_dijkstra(
    g, v, 1 * hour, 2 * hour, logging=logging))

g.generate_converse()
print(reach(g, v))

# We can free memory like this
dijkstra.clean()
