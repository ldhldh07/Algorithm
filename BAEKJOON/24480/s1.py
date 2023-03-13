import sys
sys.setrecursionlimit(100000)

def dfs(v):
    global cnt
    cnt += 1
    visited[v] = cnt
    for w in adjList[v]:
        if not visited[w]:
            # print(w)
            dfs(w)
    return

N, M, R = map(int, input().split())

adjList = [[] for _ in range(N + 1)]
for _ in range(N):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

for i in range(1, N+1):
    adjList[i].sort(reverse=True)


# print(adjList)

visited = [0] * (N+1)
cnt = 0
dfs(R)

print(*visited[1:], sep='\n')