from disjoint_set import DisjointSet
from operator import itemgetter


def kruskal(graph: DisjointSet, edges):
    '''
    Keep edges as a list with
    (source: disjoint_set node, destination: disjoint_set node, weight)
    as items
    and graph is the DisjointSet
    '''
    s_edges = sorted(edges, key=itemgetter(2))
    tree = list()
    for u, v, w in s_edges:
        if graph.find_set(u) is not graph.find_set(v):
            tree.append((u, v, w))
            graph.union(u, v)
    return tree
