N, M, R = map(int, input().split())

adjList = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)


print(adjList)