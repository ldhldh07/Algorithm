import heapq

def prim(start, n, adj_list):
    priority_queue = [(0, start)]
    visited = [0 for _ in range(n+1)]
    sum_cost = 0

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if visited[node]:
            continue

        sum_cost += cost
        visited[node] = 1
        for next_cost, next_node in adj_list[node]:
            if not visited[next_node]:
                heapq.heappush(priority_queue, (next_cost, next_node))
    return sum_cost
    
    


N, M = int(input()), int(input())

adjs = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adjs[a].append((c, b))
    adjs[b].append((c, a))

print(prim(1, N, adjs))