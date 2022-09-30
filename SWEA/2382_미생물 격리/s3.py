T = int(input())

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [[[] * N for _ in range(N)] for _ in range(N)]

    for i in range(K):
        a, b, n, d = map(int, input().split())
        arr[a][b].append([n, d])

    for _ in range(M):
        arr2 = [[[] * N for _ in range(N)] for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if arr[x][y]:
                    nx, ny = x+di[arr[x][y][0][1]], y+dj[arr[x][y][0][1]]
                    arr2[nx][ny].append(arr[x][y][0])
                    if nx in [0, N-1] or ny in [0, N-1]:
                        arr2[nx][ny][0][1] = arr2[nx][ny][0][1] - 1 + 2 * (arr2[nx][ny][0][1] % 2)
                        arr2[nx][ny][0][0] //= 2
        arr = arr2

        for i in range(N):
            for j in range(N):
                if len(arr[i][j]) > 1:
                    max_n = arr[i][j][0][0]
                    max_d = arr[i][j][0][1]
                    sum_n = 0
                    for n, d in arr[i][j]:
                        if n > max_n:
                            max_n = n
                            max_d = d
                        sum_n += n
                    arr[i][j] = [[sum_n, max_d]]

    sum_num = 0
    for a in range(N):
        for b in range(N):
            if arr[a][b]:
                sum_num += arr[a][b][0][0]

    print('#{} {}'.format(tc, sum_num))