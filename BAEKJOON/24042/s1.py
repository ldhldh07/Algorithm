import heapq
from collections import defaultdict

def dijkstra(start, n, m, adj_list):
    priority_queue = [(0, start)]
    times = [float('inf') for _ in range(n+1)]
    times[start] = 0

    while priority_queue:
        time, area = heapq.heappop(priority_queue)

        if time > times[area]:
            continue
        for next_area, cycle_list in adj_list[area].items():
            next_time = min((cycle-time) % m for cycle in cycle_list) + 1
            new_time = time + next_time
            if new_time < times[next_area]:
                times[next_area] = new_time
                heapq.heappush(priority_queue, (new_time, next_area))

    return times

N, M = map(int, input().split())

adjs = [defaultdict(list) for _ in range(N+1)]
for index in range(M):
    A, B = map(int, input().split())
    adjs[A][B].append(index)
    adjs[B][A].append(index)

print(dijkstra(1, N, M, adjs)[N])