import heapq

def dijkstra(n, start, adjList):
    distance_list = [10**5] * (n + 1)
    distance_list[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        distance, node = heapq.heappop(priority_queue)

        if distance_list[node] < distance:
            continue

        for next_node, cost in adjList[node]:
            new_distance = distance + cost
            if new_distance < distance_list[next_node]:
                distance_list[next_node] = new_distance
                heapq.heappush(priority_queue, (new_distance, next_node))
    return distance_list


N, M, X = map(int, input().split())

adjList = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, Ti = map(int, input().split())
    adjList[s].append((e, Ti))

min_distance_list = dijkstra(N, X, adjList)
max_ans = 0
for a in range(1, 1+N):
    ans = dijkstra(N, a, adjList)[X] + min_distance_list[a]
    if max_ans < ans:
        max_ans = ans

print(max_ans)