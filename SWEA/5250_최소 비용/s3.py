def ride(x1, y1, x2, y2):
    if arr[x2][y2] > arr[x1][y1]:
        return arr[x2][y2] - arr[x1][y1] + 1
    else:
        return 1


def dij(x, y, n):   # 출발 좌표 # n은 한변의 길이, n^2가 갯수
    U = [(x, y)]
    for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            cost_arr[nx][ny] = ride(x, y, nx, ny)

    for _ in range(n*n-1):
        wi = wj = 0
        for i in range(N):
            for j in range(N):
                if (i, j) not in U and cost_arr[i][j] < cost_arr[wi][wj]:
                    wi, wj = i, j
        U.append((wi, wj))
        for vi in range(N):
            for vj in range(N):
                if abs(vi - wi) + abs(vj - wj) == 1 and (vi, vj) != (0, 0):
                    cost_arr[vi][vj] = min(cost_arr[vi][vj], cost_arr[wi][wj] + ride(wi,wj,vi,vj))

    return cost_arr[n-1][n-1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cost_arr = [[1001 * N * N] * N for _ in range(N)]

    print('#{} {}'.format(tc, dij(0, 0, N)))
