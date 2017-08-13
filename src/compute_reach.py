#!/usr/bin/env python3

"""
Question B.5

This code can be launched from the command line.
It outputs to reach.log.
We make sure that we don't compute the same
value twice.
The file interactions are a bit slow, but they
allow us to launch several instances of this
program without conflict.
"""

import sys

import random

from Graph import Graph
from reach import reach
from Dijkstra import dijkstra
from util import *

####################
data = '/users/eleves-b/2015/louis.abraham/inf421/data/france.in'
log = '/users/eleves-b/2015/louis.abraham/inf421/reach.log'
timeit.activated = True
####################

try:
    n = int(sys.argv[1])
except IndexError:
    n = int(input('n = '))


def seen():
    ans = set()
    with open(log) as file:
        for l in file:
            v, _ = map(int, l.split(', '))
            ans.add(v)
    return ans


g = Graph.from_file(data, converse=True)


for _ in range(n):

    v = random.choice(list(g.keys()))
    while v in seen():
        v = random.choice(list(g.keys()))

    r = reach(g, v)[0]
    dijkstra.clean()
    with open(log, 'a') as file:
        file.write('%s, %s\n' % (v, r))
