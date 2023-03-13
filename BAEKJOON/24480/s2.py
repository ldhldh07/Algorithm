import sys
sys.setrecursionlimit(10**5)

def dfs(node):
    global cnt
    cnt += 1
    visited[node] = cnt
    for next_node in adjList[node]:
        if not visited[next_node]:
            dfs(next_node)
    return


N, M, R = map(int, input().split())

adjList = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

for i in range(1, N+1):
    adjList[i].sort(reverse=True)

visited = [0]  * (N + 1)    
cnt = 0
dfs(R)

for i, ans in enumerate(visited):
    if i:
        print(ans)