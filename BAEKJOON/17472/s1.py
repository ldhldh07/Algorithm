import sys, heapq
from collections import deque

def find_island(n, m):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    island_id = 1
    coasts = []
    for i in range(n):
        for j in range(m):
            if island_map[i][j] == 1 and not visited[i][j]:
                bfs(i, j, n, m, island_id, visited, coasts)
                island_id += 1
    make_bridge(coasts, n, m)
    return island_id - 1


def bfs(si, sj, n, m, island_id, visited, coasts):
    
    queue = deque([(si, sj)])
    visited[si][sj] = 1
    island_map[si][sj] = island_id

    while queue:
        ci, cj = queue.popleft()

        for i in range(4):
            ni, nj = ci + di[i], cj + dj[i]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                if island_map[ni][nj] == 1:
                    visited[ni][nj] = 1
                    island_map[ni][nj] = island_id
                    queue.append((ni, nj))
                elif i > 1:
                    coasts.append((island_id, ni, nj, i))


def make_bridge(coasts, n, m):
    for start_island, ci, cj, delta_index in coasts:
        distance = 0
        while True:
            ci, cj = ci + di[delta_index], cj + dj[delta_index]
            distance += 1
            if ci < 0 or ci >= n or cj < 0 or cj >= m:
                break
            next_point = island_map[ci][cj]
            if next_point == start_island:
                break
            if next_point:
                if adj_map[start_island][next_point] > distance and distance > 1:
                    adj_map[start_island][next_point] = distance
                break


def prim(start, n, adjs):
    priority_queue = [(0, start)]
    visited = [0 for _ in range(n)]
    total_distance = 0
    count = 0

    while priority_queue:
        distance, node = heapq.heappop(priority_queue)

        if visited[node]:
            continue
        visited[node] = 1
        count += 1
        total_distance += distance

        for next_distance, next_node in adjs[node]:
            if not visited[next_node]:
                heapq.heappush(priority_queue, (next_distance, next_node))
                
    return total_distance if count == island_count else -1


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

si = sys.stdin.readline

N, M = map(int, si().strip().split())

island_map = [list(map(int, si().strip().split())) for _ in range(N)]
adj_map = [[float('inf') for _ in range(7)] for _ in range(7)]
island_count = find_island(N, M)
adj_list = [[] for _ in range(island_count+1)]
for ai in range(7):
    for aj in range(7):
        if adj_map[ai][aj] != float('inf'):
            adj_list[ai].append((adj_map[ai][aj], aj))
            adj_list[aj].append((adj_map[ai][aj], ai))

print(prim(1, island_count+1, adj_list))