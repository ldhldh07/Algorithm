import heapq

def prim(n, start, adj_list):
    result = 0
    priority_queue = [(0, start)]
    visited = [0 for _ in range(n+1)]
    
    while priority_queue:
        weight, node = heapq.heappop(priority_queue)
        if visited[node]:
            continue

        result += weight
        visited[node] = 1
        
        for next_weight, next_node in adj_list[node]:
            if not visited[next_node]:
                heapq.heappush(priority_queue, (next_weight, next_node))
    return result




V, E = map(int, input().split())

adjs = [[] for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    adjs[A].append((C, B))
    adjs[B].append((C, A))

print(prim(V, 1, adjs))