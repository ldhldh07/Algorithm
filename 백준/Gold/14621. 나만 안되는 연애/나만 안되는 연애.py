import heapq

def prim(start, n, adj_list):
    priority_queue = [(0, start)]
    visited = [0 for _ in range(n)]

    sum_distance = 0

    while priority_queue:
        distance, node = heapq.heappop(priority_queue)

        if visited[node]:
            continue

        sum_distance += distance
        visited[node] = 1

        for next_distance, next_node in adj_list[node]:
            if not visited[next_node]:
                heapq.heappush(priority_queue, (next_distance, next_node))

    if visited.count(0):
        return -1
    
    return sum_distance


N, M = map(int, input().split())
genders = [1 if university == 'M' else 0 for university in input().split()]
adjs = [[] for _ in range(N)]
for _ in range(M):
    u, v, d = map(int, input().split())
    if genders[u-1] != genders[v-1]:
        adjs[u-1].append((d, v-1))
        adjs[v-1].append((d, u-1))

print(prim(0, N, adjs))