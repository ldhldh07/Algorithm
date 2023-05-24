from collections import deque

def bfs(queue):
    ans = 1
    while queue:
        ci, cj = queue.popleft()
        for di, dj in [(1, 0),(0, 1),(-1, 0),(0, -1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < M and 0 <= nj < N:
                if not arr[ni][nj]:
                    arr[ni][nj] = arr[ci][cj] + 1
                    ans = arr[ni][nj]
                    queue.append((ni, nj))
    return ans - 1

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(M)]

ripe_apples = deque()
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            ripe_apples.append((i, j))

ans = bfs(ripe_apples)

flag = False
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            ans = -1
            break

print(ans)