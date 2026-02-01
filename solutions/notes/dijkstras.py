import heapq


# O(E * log E) time, O(V + E) space
def dijkstra(graph, start):
    dist = {}
    costs = []  # stores (cost, name)
    heapq.heappush(costs, (0, start))

    while costs:
        cost, name = heapq.heappop(costs)
        if name in dist:
            continue
        dist[name] = cost

        for nname, ncost in graph[name]:
            if nname not in dist:
                heapq.heappush(costs, (cost + ncost, nname))

    return dist


graph = {
    "a": [("b", 10), ("c", 3)],
    "b": [("d", 2)],
    "c": [("b", 4), ("d", 8), ("e", 2)],
    "d": [("e", 5)],
    "e": []
}

res = dijkstra(graph, "a")

print(res)