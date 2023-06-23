from collections import deque
import sys
sys.setrecursionlimit(10**6)
    
def dfs(cur, old):
    if visited[cur]: 
        return
    visited[cur] = True
    for i in adj[cur]:
        if visited[i]: 
            continue
        people[int(not old)] += 1
        dfs(i, not old)

N = int(input())
adj = [[] for _ in range(N)]
visited = [False for _ in range(N)]
res = 0

for i in range(N):
    report = list(map(int, list(input())))
    for j in range(N):
        if report[j] == 1:
            adj[i].append(j)
            adj[j].append(i)

for i in range(N):
    if not visited[i]:
        people = [0, 0]
        dfs(i, True)
        res += max(people[0], people[1] + 1)

print(res)