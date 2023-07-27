import heapq

def dijkstra(start, n, adj_list):
    priority_queue = [(0, start)]
    times = [10**4 for _ in range(n+1)]
    times[start] = 0
    prevs = [-1 for _ in range(n+1)]

    while priority_queue:
        time, node = heapq.heappop(priority_queue)
        
        if time > times[node]:
            continue

        for next_time, next_node in adj_list[node]:
            new_time = next_time + time

            if new_time < times[next_node]:
                prevs[next_node] = node
                times[next_node] = new_time
                heapq.heappush(priority_queue, (new_time, next_node))
    
    return prevs

N, M = map(int, input().split())

adjs = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, time = map(int, input().split())
    adjs[start].append((time, end))
    adjs[end].append((time, start))

visited = [0 for _ in range(N)]

print(N-1)
prev_end_from_one = dijkstra(1, N, adjs)
for check_node in range(2, 1+N):
    print(check_node, prev_end_from_one[check_node])