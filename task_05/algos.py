from collections import deque
from node import Node


def dfs_traverse(root: Node) -> list:
    return traverse(root, lambda stack: stack.pop())


def bfs_traverse(root: Node) -> list:
    return traverse(root, lambda queue: queue.popleft())


def traverse(root: Node, pop_func) -> list:
    queue = deque([(root, [root])])
    visited = []

    while queue:
        current, path = pop_func(queue)
        visited.append(current)

        for child in [current.left, current.right]:
            if child is None:
                continue
            queue.append((child, path + [child]))

    return visited
