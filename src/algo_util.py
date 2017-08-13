"""
Some useful functions for the graph algorithmss
"""


from heapq import heappush, heappop
from collections import deque
from bisect import bisect_left
from itertools import islice


def log(logging, ans, start):
    """
    Fills the points.js file and provides
    data visualization with vis.html
    """
    with open(logging, 'w') as file:
        print('var plottedPoints =', ans or [start], ';', file=file)
        # adds start_coords if ans is empty
        print('var centralMarker =', start, ';', file=file)


def meanPoint(time, prev_d, coords_pred, d, coords_s):
    coeff = (time - prev_d) / (d - prev_d)
    return (1 - coeff) * coords_pred + coeff * coords_s


def point(graph, time, prev_d, d, pred, s):
    if graph.coords:
        return meanPoint(time, prev_d, graph.coords[
            pred], d, graph.coords[s])
    else:
        return pred
