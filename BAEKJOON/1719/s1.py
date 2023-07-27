import heapq

def dijkstra(start, N, adj_list):
    priority_queue = [(0, start)]
    times = [10**7 for _ in range(N)]
    times[start] = 0
    first_route = [-1 for _ in range(N)]
    first_route[start] = '-'

    while priority_queue:
        time, node = heapq.heappop(priority_queue)

        if time > times[node]:
            continue

        for next_time, next_node in adj_list[node]:
            new_time = time + next_time

            if new_time < times[next_node]:
                times[next_node] = new_time
                first_route[next_node] = next_node + 1 if node == start else first_route[node]
                heapq.heappush(priority_queue, (new_time, next_node))
    return first_route

n, m = map(int, input().split())

adjs = [[] for _ in range(n)]
for _ in range(m):
    start, end, time = map(int, input().split())
    adjs[start-1].append((time, end-1))
    adjs[end-1].append((time, start-1))

for start_point in range(n):
    print(*dijkstra(start_point, n, adjs))