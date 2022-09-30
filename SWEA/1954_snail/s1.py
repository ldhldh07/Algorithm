T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for t in range(1, 1+T):
    N = int(input())

    arr = [[0] * N for _ in range(N)]                          # NxN의 2차원 배열

    i = j = 0                                                  # 위치의 초기값
    k = 0                                                      # 방향의 초기값값
    for idx in range(1, N*N+1):                                # N*N만큼 반복

        arr[i][j] = idx                                        # 인덱스값 현위치에 입력

        if 0 <= i + di[k%4] < N and 0 <= j + dj[k%4] < N :     # 이동후 범위 벗어나지 않도록
            if arr[i + di[k%4]][j + dj[k%4]] != 0:             # 이동시 이미 값이 들어간 경우
                k += 1                                         # 방향 바꾸고
                i += di[k%4]                                   # 위치 전환
                j += dj[k%4]
            else:                                              # 아니면 진행하던 방향으로 이동
                i += di[k%4]
                j += dj[k%4]
        else:                                                  # 범위 밖으로 가면 방향 바꿔서 이동
            k += 1
            i += di[k % 4]
            j += dj[k % 4]

    print('#{}'.format(t))
    for a in range(N):

        for b in range(N):
            print(arr[a][b], end=' ')
        print()
