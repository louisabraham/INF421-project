"""
Question B.4

Notes:
    A dichotomy for the 4-factor approximation
    reduces the number of calls to the oracle
    to O(log(log(r))) for this stage.

    But it would also call it with bigger inputs
    and more inputs that evaluate to False
    thus taking a bit more time.

    If we are not lucky, it could call oracle with
    a huge value, so it is not a good idea in practice
    because oracle is optimised for small values.
"""


from math import sqrt, ceil

from algo import *
from Dijkstra import *
from util import *


def oracle(graph, v, r):

    if graph.converse is None:
        graph.generate_converse()

    time = r
    mindist = 2 * r
    start = v

    S_in = possible_locations_with_mindist_dijkstra(
        graph.converse, start, time, mindist, coords=False)
    T_out = possible_locations_with_mindist_dijkstra(
        graph, start, time, mindist, coords=False)

    dijcon = next(dijkstra(graph.converse, v))[0]
    dij = next(dijkstra(graph, v))[0]

    for s in S_in:
        for t in T_out:
            d = dijkstra_with_target(graph, s).send(t)
            # d(s, t) = d(s, v) + d(v, t)
            if d == dijcon[s][0] + dij[t][0]:
                return True

    return False


@timeit
def reach(graph, v):
    """
    The implementation of the reach function.
    """

    # We disable timeit for intermediate
    # functions
    default_timeit = timeit.activated
    timeit.activated = False

    if not oracle(graph, v, 0.5):
        # Special case
        timeit.activated = default_timeit
        return (0, 0)

    y = 1
    while oracle(graph, v, 2 * y):
        y <<= 1
    # we have a 4-factor approximation
    a, b = y, 4 * y

    while (b - 1) / a > 2:
        c = sqrt(a * b / 2)
        if oracle(graph, v, c):
            a = ceil(c)
        else:
            b = ceil(2 * c)

    dijkstra_with_target.clean()

    timeit.activated = default_timeit
    return (a, b)
