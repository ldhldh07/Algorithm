import heapq


INF = int(1e9)
def dijkstra(n, start, adjList):
    distance_list = [float("INF")] * (n + 1)
    # print(distance_list)
    distance_list[start] = 0

    priority_queue = [(0, start)]
    
    while priority_queue:
        distance, node = heapq.heappop(priority_queue)

        if distance > distance_list[node]:
            continue

        for next_node, next_distance in adjList[node]:
            new_distance = distance + next_distance
            # print(next_node)
            if new_distance < distance_list[next_node]:
                distance_list[next_node] = new_distance
                heapq.heappush(priority_queue, (new_distance, next_node))

    return distance_list

V, E = map(int, input().split())

K = int(input())
adjList = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjList[u].append((v, w))
    # adjList[v].append((u, w))

# print(adjList)

# print(*dijkstra(V, K, adjList)[1:], sep='\n')

for distance in dijkstra(V, K, adjList)[1:]:
    if distance == float('inf'):
        print('INF')
    else:
        print(distance)