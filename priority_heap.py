from heapq import heapify, heappush, heappop
from dataclasses import dataclass, field
from typing import Any
from itertools import count


@dataclass(order=True)
class Node:
    priority: Any = field(compare=True)
    task: Any = field(compare=False)


class PriorityHeap:
    def __init__(self, lst):
        self.counter = count()
        self.size = 0
        self.entry_finder = {}
        self.heap = list()
        for task, pri in lst.items():
            node = self.create_node(task, pri)
            self.entry_finder[task] = node
            self.heap.append(node)
        heapify(self.heap)
        self.size = len(self.heap)

    def create_node(self, task, priority):
        return Node((priority, next(self.counter)), task)

    def add_task(self, task, priority):
        if task in self.entry_finder:
            self.remove_task(task)
        node = self.create_node(task, priority)
        self.entry_finder[task] = node
        heappush(self.heap, node)
        self.size += 1

    def remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry.item = None
        self.size -= 1

    def pop_task(self):
        while self.size > 0:
            node = heappop(self.heap)
            if node.task is not None:
                del self.entry_finder[node.task]
                self.size -= 1
                return node.task
        self.heap = list()
        raise KeyError('pop from an empty priority queue')

    def __len__(self):
        return self.size
