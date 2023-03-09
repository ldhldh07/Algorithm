def dfs(v, N, cnt):
    visited = [0]  * (N + 1)    
    visited[v] = cnt
    stack = [v]
    
    while True:
        for w in adjList[v]:
            if not visited[w]:
                stack.append(v)
                v = w
                cnt += 1
                visited[v] = cnt
                break
        else:
            if stack:
                v = stack.pop()
            else:
                return visited


N, M, R = map(int, input().split())

adjList = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

for i in range(1, N+1):
    adjList[i].sort()
ans_list = dfs(R, N, 1)

print(*ans_list[1:], sep = "\n")