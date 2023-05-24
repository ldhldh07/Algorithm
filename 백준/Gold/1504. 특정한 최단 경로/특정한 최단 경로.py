import heapq

def dijkstra(n, start, adjList):
    priority_queue = [(0, start)]
    distance_list = [800 * 1000 + 1] * (n + 1)
    distance_list[start] = 0

    while priority_queue:
        distance, node = heapq.heappop(priority_queue)

        if distance > distance_list[node]:
            continue

        for next_node, next_distance in adjList[node]:
            new_distance = distance + next_distance
            if new_distance < distance_list[next_node]:
                distance_list[next_node] = new_distance
                heapq.heappush(priority_queue, (new_distance, next_node,))

    return distance_list


def min_distance(s, first, second, e):
    if dijkstra(N, s, adjList)[first] != 800 * 1000 + 1 and dijkstra(N, first, adjList)[second] != 800 * 1000 + 1 and dijkstra(N, second, adjList)[e] != 800 * 1000 + 1:
        return dijkstra(N, s, adjList)[first] + dijkstra(N, first, adjList)[second] + dijkstra(N, second, adjList)[e]
    else:
        return (800 * 1000 + 1) * 3

N, E = map(int, input().split())

adjList = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adjList[a].append((b, c))
    adjList[b].append((a, c))

u, v = map(int, input().split())

ans = min(min_distance(1, u, v, N),min_distance(1, v, u, N))

if ans == (800 * 1000 + 1) * 3:
    print(-1)
else:
    print(ans)