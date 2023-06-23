import heapq

def dijkstra(start, end):
    priority_queue = [(0, start)]
    distance = [-1 for _ in range(10**5+1)]
    distance[start] = 0

    while priority_queue:
        dist, node = heapq.heappop(priority_queue)
        
        if distance[node] != dist:
            continue

        for index, next_node in enumerate([node*2, node+1, node-1]):
            if 0 <= next_node < 10**5+1:
                cost = dist if index == 0 else dist+1
                if distance[next_node] == -1 or cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(priority_queue, (cost, next_node))
    return distance[end]

start, end = map(int, input().split())
print(dijkstra(start, end))
