from collections import deque

def dfs(sp):
    global cnt
    route.append(sp)
    visited[sp] = 1
    while route:
        node = route.popleft()
        cnt += 1
        order[node] = cnt
        for next_node in adjList[node]:
            if not visited[next_node]:
                route.append(next_node)
                visited[next_node] = visited[node] + 1




N, M, R = map(int, input().split())

adjList = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
order = [0] * (N + 1)
cnt = 0
route = deque()

for _ in range(M):
    u, v = map(int, input().split())
    
    adjList[u].append(v)
    adjList[v].append(u)

for i in range(1, N + 1):
    adjList[i].sort()

dfs(R)

print(*order[1:], sep=('\n'))