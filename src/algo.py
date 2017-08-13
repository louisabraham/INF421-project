"""
The main algorithms are provided here.

Implementation notes :
    We support the multiple shortest paths case.

    Although number_of_possible_locations is very efficient,
    in practice, if you launch the algorithm several times
    for the same graph and the same start, it is faster to
    use number_of_possible_locations_with_mindist_dijkstra
    with mindist=0 because it uses the memoized dijkstra.

    It is advised to delete the cache after use with
    `dijkstra.clean()` if you work on huge data
"""


__all__ = ['possible_locations',
           'possible_locations_with_mindist_dijkstra']

__all__ += ['number_of_' + name for name in __all__]


from util import timeit
from Dijkstra import *
from algo_util import *


@timeit
def possible_locations(graph, start, time, logging=None):
    """
    Points at distance time of start that
    are in a shortest path.
    This algorithm is based on Dijkstra.
    """

    ans = []
    dist = {None: 0}
    Q = [(0, start, None)]

    while Q:
        d, s, pred = heappop(Q)
        prev_d = dist[pred]

        if s in dist and prev_d < time < d == dist[s]:
            # special case for multiple shortest paths
            # note time < d because we don't want to count
            # multiple times a vertex
            ans.append(point(graph, time, prev_d, d, pred, s))

        elif not s in dist:
            dist[s] = d
            if prev_d < time <= d:
                ans.append(point(graph, time, prev_d, d, pred, s))
            for v in graph[s]:
                new_dist = d + graph[s][v]
                if not v in dist and new_dist <= time + graph.maxedge:
                    # facultative condition for optimisation
                    heappush(Q, (new_dist, v, s))

    if logging is not None:
        log(logging, ans, graph.coords[start])

    return ans


def number_of_possible_locations(*args, **kwargs):
    return len(possible_locations(*args, **kwargs))


@timeit
def possible_locations_with_mindist_dijkstra(graph, start, time, mindist, logging=None, coords=None):
    """
    Number of points at distance time of start that
    are in a shortest path to a vertex that is at least at
    mindist of start.
    We use a dijkstra and then backtrack.
    Since dijkstra is memoised, it is very fast.
    We use binary search and 
    dynamic programming to optimize,
    and a FIFO to handle multiple shortest paths.
    It works even with mindist < time, but in this situation,
    even with a memoised dijkstra, possible_locations may be faster
    If coords = False, it ignores the coords and
    gives the last vertices at distance <= time
    """

    if coords is None or coords:
        coords = graph.coords

    # there are some differences whether
    # you use the coords or not
    ans = [] if coords else set()

    limit = max(mindist, time) + graph.maxedge
    dist, distindex = dijkstra(graph, start).send(limit)

    visited = set()

    # This allows us to take only interesting
    # starting vertices
    startindex = bisect_left(distindex, (mindist,))
    stopindex = bisect_left(distindex, (limit,))

    for _, s in islice(distindex, startindex, stopindex):
        Q = deque([s])
        while Q:
            s = Q.popleft()
            if not s in visited:
                visited.add(s)
                d, lpred = dist[s]
                if d == time:
                    # special case or else we will count
                    # multiple times this vertex
                    if coords:
                        ans.append(coords[s])
                    else:
                        ans.add(s)
                else:
                    for v in lpred:
                        d_v = dist[v][0]
                        if d_v < time < d:
                            if coords:
                                ans.append(meanPoint
                                           (time, d_v, coords[v], d, coords[s]))
                            else:
                                ans.add(v)
                        else:
                            Q.append(v)

    if logging is not None:
        log(logging, ans, coords[start])

    return ans


def number_of_possible_locations_with_mindist_dijkstra(*args, **kwargs):
    return len(possible_locations_with_mindist_dijkstra(*args, **kwargs))
