"""
These two data classes are very useful.
"""


__all__ = ['Point', 'Graph']

from collections import namedtuple

from util import *

# namedtuples have minimal impact on memory usage
# we add some methods to facilitate calculations and logging.
Point = namedtuple('Point', ['x', 'y'])
Point.__add__ = lambda a, b: Point(a.x + b.x, a.y + b.y)
Point.__mul__ = Point.__rmul__ = lambda p, t: Point(p.x * t, p.y * t)
Point.__repr__ = lambda p: '[%.06f, %.06f]' % (p * 1e-6)[::-1]


class Graph(dict):

    def __init__(self):
        self.maxedge = 0
        self.coords = {}
        self.converse = None
        super().__init__()

    def addNode(self, nodeName, longitude=None, latitude=None):
        assert not nodeName in self
        if longitude is not None and latitude is not None:
            self.coords[nodeName] = Point(longitude, latitude)
        self[nodeName] = {}

    def addEdge(self, start, finish, length):
        self[start][finish] = length
        self.maxedge = max(self.maxedge, length)

    @staticmethod
    def from_file(path, converse=False):
        graph = Graph()
        line_count = sum(1 for _ in open(path))
        print('Begin graph importation')
        with open(path) as file:
            for line in progress_bar(file, total=line_count):
                ins, *args = line.split()
                *args, = map(int, args)
                if ins == 'v':
                    graph.addNode(*args)
                else:
                    graph.addEdge(*args)
        if converse:
            graph.generate_converse()
        return graph

    def generate_converse(self):
        print('Begin converse graph generation')
        self.converse = Graph()
        for a in progress_bar(self):
            # else we might have missing nodes
            if not a in self.converse:
                self.converse[a] = {}
            for b in self[a]:
                if not b in self.converse:
                    self.converse[b] = {}
                self.converse[b][a] = self[a][b]
        self.converse.maxedge = self.maxedge
        self.converse.coords = self.coords
        self.converse.converse = self
