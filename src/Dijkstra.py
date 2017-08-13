"""
AWESOME ONLINE MEMOISED DIJKSTRA WITH SORTED OUTPUT
This particularly elegant implementations of dijkstra
use generators to limit their computations and
memoize the state of the program.
"""

__all__ = ['dijkstra', 'dijkstra_with_target']

from heapq import heappush, heappop

from util import memoize_generator


@memoize_generator
def dijkstra(graph, start):
    """
    Online Dijkstra, memoized to optimize
    multiple calls requests of possible locations
    functions with same (graph, start).
    We also give a sorted list of (dist[v], v)
    to optimize other functions.
    """

    dist = {}
    distindex = []
    Q = [(0, start, start)]

    limit = yield

    while Q:
        d, s, pred = heappop(Q)

        while limit <= d:
            yld = yield dist, distindex
            limit = limit if yld is None else yld

        if s in dist and d == dist[s][0]:
            # special case for multiple shortest paths
            dist[s][1].append(pred)

        elif not s in dist:
            dist[s] = (d, [pred])
            distindex.append((d, s))
            for v in graph[s]:
                new_dist = d + graph[s][v]
                if not v in dist:
                    heappush(Q, (new_dist, v, s))
    while True:
        yield dist, distindex


@memoize_generator
def dijkstra_with_target(graph, start):
    """
    Quick Dijkstra that stops
    when it finds its target
    """

    target = yield
    dist = {}
    ans = None

    Q = [(0, start)]

    while Q:

        while ans is not None:
            target = yield ans
            ans = None
            if target in dist:
                ans = dist[target]

        d, s = heappop(Q)

        if not s in dist:
            dist[s] = d
            if s == target:
                ans = d
            for v in graph[s]:
                if not v in dist:
                    # facultative condition for optimisation
                    heappush(Q, (d + graph[s][v], v))

    while True:
        target = yield dist[target]
