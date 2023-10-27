import sys, heapq

def dijkstra(start, n, adj_list):
    priority_queue = [(0, start)]
    distances = [float('inf') for _ in range(n)]
    distances[start] = 0

    while priority_queue:
        distance, node = heapq.heappop(priority_queue)

        if distances[node] < distance:
            continue

        for next_distance, next_node in adj_list[node]:
            new_distance = distance + next_distance

            if new_distance < distances[next_node]:
                distances[next_node] = new_distance
                heapq.heappush(priority_queue, (new_distance, next_node))

    return distances


si = sys.stdin.readline

N, M = map(int, si().strip().split())

adj_list = [[] for _ in range(N)]

for _ in range(M):
    A, B, C = map(int, si().strip().split())
    adj_list[A-1].append((C, B-1))
    adj_list[B-1].append((C, A-1))

print(dijkstra(0, N, adj_list)[N-1])
