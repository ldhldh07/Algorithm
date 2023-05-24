import sys
sys.setrecursionlimit(10 ** 5)


def dfs(v, cnt):
    visited[v] = cnt
    for w in adjList[v]:
        if visited[w] == -1:
            dfs(w, cnt + 1)

N, M, R = map(int, input().split())

adjList = [[] for _ in range(N+1)]
visited = [-1] * (N+1)

for m in range(M):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

for i in range(1, N+1):
    adjList[i].sort()

dfs(R, 0)

print(*visited[1:], sep='\n')