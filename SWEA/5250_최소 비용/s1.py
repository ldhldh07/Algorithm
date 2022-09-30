
def move(x, y, n, s):
    global min_route
    visited[x][y] = 1
    if x == n-1 and y == n-1:
        if s < min_route:
            min_route = s
    if s >= min_route:
        return
    if s + (n-x)+(n-y) >= min_route:
        return
    else:
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if arr[nx][ny] > arr[x][y]:
                    move(nx, ny, n, s + 1 + abs(arr[nx][ny]-arr[x][y]))
                    visited[nx][ny] = 0
                else:
                    move(nx, ny, n, s + 1)
                    visited[nx][ny] = 0



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1

    min_route = 1001 * N * N
    move(0, 0, N, 0)
    print('#{} {}'.format(tc, min_route))
