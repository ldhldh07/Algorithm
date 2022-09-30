T = int(input())

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, -1, 1]

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    bacteria = []
    for _ in range(K):
        a, b, n, d = map(int, input().split())
        bacteria.append([a, b, n, d])

    for _ in range(M):
        for i in range(K):
            bacteria[i][0] += di[bacteria[i][3]]
            bacteria[i][1] += dj[bacteria[i][3]]
            if not bacteria[i][0] or not bacteria[i][1]:
                bacteria[i][3] = bacteria[i][3] - 1 + 2 * (bacteria[i][3] % 2)
                bacteria[i][2] //= 2

        arr = [[[]] * N for _ in range(N)]
        for s in range(K):
            arr[bacteria[s][0]][bacteria[s][1]].append((bacteria[s][2], s))
        for ii in range(N):
            for jj in range(N):
                if len(arr[ii][jj]) > 1:
                    max_n = arr[ii][jj][0][0]
                    max_s = arr[ii][jj][0][1]
                    sum_n = 0
                    for n, s in arr[ii][jj]:
                        if max_n < n:
                            max_n = n
                            max_s = s
                        sum_n += n
                    for n, s in arr[ii][jj]:
                        if n == max_n:
                            bacteria[s][2] = sum_n
                        else:
                            bacteria[s][2] = 0

    print('#{} {}'.format(tc, sum(a[2] for a in bacteria)))
