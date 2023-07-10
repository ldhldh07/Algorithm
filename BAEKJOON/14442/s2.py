from collections import deque

delta = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

def bfs(n, m, k, arr):
    visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0, 0, 1)])

    while queue:
        x, y, cnt, distance = queue.popleft()
        if x == n - 1 and y == m - 1:
            return distance

        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny][cnt]:
                    if arr[nx][ny] == 0:
                        queue.appendleft((nx, ny, cnt, distance + 1))
                    elif cnt < k:
                        queue.append((nx, ny, cnt + 1, distance + 1))
                    visited[nx][ny][cnt] = True

    return -1

N, M, K = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
print(bfs(N, M, K, arr))
