from dataclasses import dataclass, field
from typing import Any
from operator import itemgetter


@dataclass(order=True)
class Node:
    name: Any = field(hash=True, compare=False)
    parent: Any = field(hash=False, compare=False)
    rank: int = 0

    def __hash__(self):
        return hash(self.name)


class DisjointSet:
    def __init__(self, lst):
        self.nodes = [self.create_node(name, name, 0) for name in lst]
        for x in self.nodes:
            x.parent = x

    def __getitem__(self, index):
        return self.nodes[index]

    def create_node(self, name, parent, rank):
        return Node(name, parent, rank)

    def make_set(self, name):
        node = self.create_node(name, name, 0)
        node.parent = node
        if name not in self.nodes:
            self.nodes.append(node)

    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))

    def link(self, x, y):
        if x > y:
            y.parent = x
        else:
            x.parent = y
            if x == y:
                y.rank += 1

    def find_set(self, x):
        if x != x.parent:
            x.parent = self.find_set(x.parent)
        return x.parent


def kruskal(graph: DisjointSet, edges, tree):
    '''
    Keep edges as a list with
    (source: disjoint_set node, destination: disjoint_set node, weight)
    as items
    and graph is the DisjointSet
    '''
    s_edges = sorted(edges, key=itemgetter(2))
    for u, v, w, i in s_edges:
        if graph.find_set(u) is not graph.find_set(v):
            tree.append((u, v, w, i))
            graph.union(u, v)
    return tree


def kruskal1(graph: DisjointSet, edges, tree, k):
    '''
    Keep edges as a list with
    (source: disjoint_set node, destination: disjoint_set node, weight)
    as items
    and graph is the DisjointSet
    '''
    s_edges = sorted(edges, key=itemgetter(2))
    for u, v, w, i in s_edges:
        if graph.find_set(u) is not graph.find_set(v):
            tree.append((u, v, w, i))
            graph.union(u, v)
            k -= 1
        if k <= 0:
            return tree, k
    return tree, k


n, m, k = (int(x) for x in input().split())
vertices = range(1, n+1)
ds = DisjointSet(vertices)
capital_roads = []
roads = []
for i in range(m):
    a, b, w = (int(x) for x in input().split())
    if a == 1 or b == 1:
        capital_roads.append((ds.nodes[a-1], ds.nodes[b-1], w, i))
    else:
        roads.append((ds.nodes[a-1], ds.nodes[b-1], w, i))

tree, k = kruskal1(ds, capital_roads, list(), k)
if k == 0:
    tree = kruskal(ds, roads, tree)
    print(n-1)
    for _, _, _, i in tree:
        print(str(i+1)+" ", end="")
    print()
else:
    print(-1)
