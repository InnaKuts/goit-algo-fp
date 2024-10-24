from __future__ import annotations
import heapq


def dijkstra(graph: dict[str, dict[str, float]], start) -> tuple[dict[str, float], dict[str, str | None]]:
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    reached_from = {node: None for node in graph}

    min_heap = [(0, start)]
    heapq.heapify(min_heap)

    while len(min_heap) > 0:
        dist, node = heapq.heappop(min_heap)

        if dist > distances[node]:
            continue

        for neighbor, weight in graph[node].items():
            distance = dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                reached_from[neighbor] = node
                heapq.heappush(min_heap, (distance, neighbor))

    return distances, reached_from


def main():
    graph = {
        'A': {'B': 1, 'C': 2},
        'B': {'A': 1, 'C': 2, 'D': 5, 'E': 3},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1, 'E': 3},
        'E': {'D': 1}
    }

    start_node = 'A'
    distances, reached_from = dijkstra(graph, start_node)

    print(f"Shortest distances from `{start_node}`:")
    for node, distance in distances.items():
        path = []
        p = node
        while p:
            path.append(p)
            p = reached_from.get(p)
        path.reverse()
        print(f"to `{node}` is {distance}: {'->'.join(path)}")


if __name__ == "__main__":
    main()
