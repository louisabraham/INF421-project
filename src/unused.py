"""
Here are all the other codes we made.

possible_locations_with_mindist is faster than
possible_locations_with_mindist_dijkstra because
it does not compute the dijkstra paths, but makes
only one scan of the graph and uses minimal memory.

The functions whose name ends with '_simple' ignore
multiple shortest paths, but are slightly faster.
They all work similarly to their alternatives,
but since they were written at a less advanced
stage of development, they may contain some bugs
(for example reach_simple returns 1 when the answer is 0)

We made the choice to use exact functions even for reach,
even if that implies having slower codes.
We quickly tested on france.in and found multiple
shortest paths for the first starting vertex we chose.
"""


__all__ = ['possible_locations_with_mindist',
           'possible_locations_with_mindist_simple',
           'possible_locations_with_mindist_dijkstra_simple']
__all__ += ['number_of_' + name for name in __all__]
__all__ += ['dijkstra_simple', 'oracle_simple', 'reach_simple']

from math import sqrt, ceil
from collections import defaultdict

from util import *
from algo_util import *
from Dijkstra import *


@timeit
def possible_locations_with_mindist(graph, start, time, mindist, logging=None):
    """
    We use a single dijkstra with propagation.
    This version doesn't work with time > mindist.
    TODO: add coords option support, remove defaultdict
    """
    assert time <= mindist

    ans = set()
    dist = {None: 0}
    ancestors_at_time = defaultdict(lambda: set())

    Q = [(0, start, None)]

    while Q:
        d, s, pred = heappop(Q)
        if time <= d:
            # reduces memory usage
            points = ancestors_at_time[s]
        prev_d = dist[pred]

        if s in dist and mindist <= d == dist[s]:
            # special case for multiple shortest paths
            points.update(ancestors_at_time[pred])
            ans.update(points)
        elif s in dist and prev_d < time < d == dist[s]:
            # special case for multiple shortest paths
            # note time < d because we don't want to count
            # multiple times a vertex
            points.add(point(graph, time, prev_d, d, pred, s))
            if mindist <= d:
                ans.update(points)
        elif not s in dist:
            dist[s] = d
            if prev_d < time <= d:
                points.add(point(graph, time, prev_d, d, pred, s))
            elif time <= d:
                points.update(ancestors_at_time[pred])
            if mindist <= d:
                ans.update(points)
            for v in graph[s]:
                new_dist = d + graph[s][v]
                if not v in dist and new_dist < mindist + graph.maxedge:
                    # facultative condition for optimisation
                    heappush(Q, (new_dist, v, s))
    ans = list(ans)

    if logging is not None:
        log(logging, ans, graph.coords[start])

    return ans


def number_of_possible_locations_with_mindist(*args, **kwargs):
    return len(possible_locations_with_mindist(*args, **kwargs))


@timeit
def possible_locations_with_mindist_simple(graph, start, time, mindist, logging=None, coords=None):
    """Number of points at distance time of start that
    are in a shortest path to a vertex that is at least at
    mindist of start.
    We use a single dijkstra with propagation.
    We optimize in memory (an thus a bit in time)
    by propagating only one ancestor and ignoring
    multiple shortest paths
    If coords = False, it ignores the coords and
    gives the last vertices at distance <= time"""

    assert time <= mindist

    if coords is None:
        coords = bool(graph.coords)

    ans = set()
    dist = {None: 0}

    start_point = graph.coords[start] if graph.coords else start
    Q = [(0, start, None, start_point)]

    while Q:
        d, s, pred, ancestor_at_time = heappop(Q)
        prev_d = dist[pred]

        if mindist <= d:
            ans.add(ancestor_at_time)
        elif not s in dist:
            dist[s] = d
            if prev_d < time <= d:
                assert ancestor_at_time == start_point
                if coords:
                    ancestor_at_time = point(graph, time, prev_d, d, pred, s)
                else:
                    ancestor_at_time = pred
            for v in graph[s]:
                new_dist = d + graph[s][v]
                if not v in dist and new_dist < mindist + graph.maxedge:
                    # facultative condition for optimisation
                    heappush(Q, (new_dist, v, s, ancestor_at_time))
    ans = list(ans)

    if logging is not None:
        log(logging, ans, graph.coords[start])

    return ans


def number_of_possible_locations_with_mindist_simple(*args, **kwargs):
    return len(possible_locations_with_mindist_simple(*args, **kwargs))


@memoize_generator
def dijkstra_simple(graph, start):

    dist = {}
    distindex = []
    Q = [(0, start, start)]

    limit = yield

    while Q:
        d, s, pred = heappop(Q)

        while limit <= d:
            yld = yield dist, distindex
            limit = limit if yld is None else yld

        if not s in dist:
            dist[s] = (d, pred)
            distindex.append((d, s))
            for v in graph[s]:
                new_dist = d + graph[s][v]
                if not v in dist:
                    # facultative condition for optimisation
                    # note the < even if we count multiple
                    # because of the heap
                    heappush(Q, (new_dist, v, s))
    while True:
        yield dist, distindex


@timeit
def possible_locations_with_mindist_dijkstra_simple(graph, start, time, mindist, logging=None, coords=None):

    if coords is None or coords:
        coords = graph.coords

    # there are some differences whether
    # you use the coords or not
    ans = [] if coords else set()

    limit = max(mindist, time) + graph.maxedge
    dist, distindex = dijkstra_simple(graph, start).send(limit)

    visited = set()

    startindex = bisect_left(distindex, (mindist,))
    stopindex = bisect_left(distindex, (limit,))

    for _, s in islice(distindex, startindex, stopindex):
        d, pred = dist[s]
        while not (s in visited or dist[pred][0] < time <= d):
            visited.add(s)
            s = pred
            d, pred = dist[s]
        if not s in visited:
            visited.add(s)
            if d == time:
                # special case or else we will count
                # multiple times this vertex
                if coords:
                    ans.append(coords[s])
                else:
                    ans.add(s)
            elif dist[pred][0] < time < d:
                if coords:
                    ans.append(meanPoint
                               (time, dist[pred][0], coords[pred], d, coords[s]))
                else:
                    ans.add(pred)

    if logging is not None:
        log(logging, ans, coords[start])

    return ans


def number_of_possible_locations_with_mindist_dijkstra_simple(*args, **kwargs):
    return len(possible_locations_with_mindist_dijkstra_simple(*args, **kwargs))


def oracle_simple(graph, v, r):

    if graph.converse is None:
        graph.generate_converse()

    time = r
    mindist = 2 * r
    start = v

    S_in = possible_locations_with_mindist_dijkstra_simple(
        graph.converse, start, time, mindist, coords=False)
    T_out = possible_locations_with_mindist_dijkstra_simple(
        graph, start, time, mindist, coords=False)

    dijcon = next(dijkstra_simple(graph.converse, v))[0]
    dij = next(dijkstra_simple(graph, v))[0]

    for s in S_in:
        for t in T_out:
            d = dijkstra_with_target(graph, s).send(t)
            # d(s, t) = d(s, v) + d(v, t)
            if d == dijcon[s][0] + dij[t][0]:
                return True
    return False


@timeit
def reach_simple(graph, v):

    default_timeit = timeit.activated
    timeit.activated = False

    y = 1
    while oracle_simple(graph, v, 2 * y):
        y <<= 1
    # we have a 4-factor approximation
    a, b = y, 4 * y

    while (b - 1) / a > 2:
        c = sqrt(a * b / 2)
        if oracle_simple(graph, v, c):
            a = ceil(c)
        else:
            b = ceil(2 * c)

    timeit.activated = default_timeit
    dijkstra_with_target.clean()

    return (a, b)
