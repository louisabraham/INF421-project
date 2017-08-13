#!/usr/bin/env python3

import random

from Graph import Graph
from Dijkstra import dijkstra
from reach import reach
from util import timeit

####################
data = '/Users/louisabraham/Downloads/RoadNetworks/data/france.in'
timeit.activated = True
tests = []
number_of_random_tests = 50
####################
# sample values for france.in
# 1990653115 (2815477, 5630955)
# 1867465537 (5887521, 11775043)
# 1186530882 (9066736, 18133473)
# 2155775848 (0, 0)
# 3131293889 (0, 0)


g = Graph.from_file(data, converse=True)

for v in tests:
    print(v, reach(g, v))
    dijkstra.clean()

for _ in range(number_of_random_tests):
    v = random.choice(list(g.keys()))
    print(v, reach(g, v))
    dijkstra.clean()
