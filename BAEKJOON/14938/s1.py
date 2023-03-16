
def dijkstra(N, start, adj, d):
    for i in range(N+1):
        d[i] = adj[start][i]
    visited = [start]
    for _ in range(N-1):
        min_i = 0
        for i in range(1, N+1):
            if i not in visited and d[i] < d[min_i]:
                min_i = i
        visited.append(min_i)
        for next_node in range(1, n+1):
            if 0 < adj[min_i][next_node] < 1501:
                distance[next_node] = min(distance[next_node], distance[min_i] + adjList[min_i][next_node])



n, m, r = map(int, input().split())
item_list = list(map(int, input().split))

adjList = [1501 for _ in range(n + 1)  for _ in range(n + 1)]
for _ in range():
    a, b, l = map(int, input().split())
    adjList[a][b] = l

distance = [0] * (n + 1)
