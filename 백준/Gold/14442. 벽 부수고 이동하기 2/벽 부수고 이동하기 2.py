from collections import deque

delta = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

def bfs(n, m, k, arr):
    visited = [[[10 ** 6] * (k + 1) for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    queue = deque([(0, 0, 0)])

    while queue:
        x, y, cnt = queue.popleft()
        if x == n - 1 and y == m - 1:
            return min(visited[x][y])

        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visited[x][y][cnt] + 1 < visited[nx][ny][cnt]:
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1
                    queue.append((nx, ny, cnt))
                elif arr[nx][ny] == 1 and cnt < k and visited[x][y][cnt] + 1 < visited[nx][ny][cnt + 1]:
                    visited[nx][ny][cnt + 1] = visited[x][y][cnt] + 1
                    queue.append((nx, ny, cnt + 1))

    return -1

N, M, K = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
print(bfs(N, M, K, arr))