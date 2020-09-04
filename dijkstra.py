from priority_heap import PriorityHeap


def dijkstra(graph, vertices, source):
    distance = {source: 0}
    ph = PriorityHeap(distance)
    parent = dict()
    while len(ph) != 0:
        vertex = ph.pop_task()
        for v, w in graph[vertex]:
            if distance.get(v, float('inf')) > distance[vertex] + w:
                distance[v] = distance[vertex] + w
                ph.add_task(v, distance[v])
                parent[v] = vertex
    return distance, parent
