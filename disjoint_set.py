from dataclasses import dataclass, field
from typing import Any


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
