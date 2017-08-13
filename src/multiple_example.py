"""
Simple example that tests all methods
on an example with multiple shortest paths

The output should be:
2
2
1

2
2
1
1

1
1
1

1
1
1
1

0
0
0
0
"""

from Graph import Graph
from algo import *
from unused import *

g = Graph()
g.addNode(0)
g.addNode(1)
g.addNode(2)
g.addNode(3)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 6)
g.addEdge(1, 3, 3)
g.addEdge(2, 3, 2)

print(number_of_possible_locations(g, 0, 7))
print(number_of_possible_locations_with_mindist_dijkstra(g, 0, 7, 0))
print(number_of_possible_locations_with_mindist_dijkstra_simple(g, 0, 7, 0))
print()
print(number_of_possible_locations_with_mindist(g, 0, 6, 8))
print(number_of_possible_locations_with_mindist_dijkstra(g, 0, 6, 8))
print(number_of_possible_locations_with_mindist_dijkstra_simple(g, 0, 6, 8))
print(number_of_possible_locations_with_mindist_simple(g, 0, 6, 8))
print()
print(number_of_possible_locations(g, 0, 8))
print(number_of_possible_locations_with_mindist_dijkstra(g, 0, 8, 0))
print(number_of_possible_locations_with_mindist_dijkstra_simple(g, 0, 8, 0))
print()
print(number_of_possible_locations_with_mindist(g, 0, 3, 8))
print(number_of_possible_locations_with_mindist_dijkstra(g, 0, 3, 8))
print(number_of_possible_locations_with_mindist_dijkstra_simple(g, 0, 3, 8))
print(number_of_possible_locations_with_mindist_simple(g, 0, 3, 8))
print()
print(number_of_possible_locations_with_mindist(g, 0, 3, 9))
print(number_of_possible_locations_with_mindist_dijkstra(g, 0, 3, 9))
print(number_of_possible_locations_with_mindist_dijkstra_simple(g, 0, 3, 9))
print(number_of_possible_locations_with_mindist_simple(g, 0, 3, 9))
