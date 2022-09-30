di = [0, 1, 0, -1, 1, -1, 1, -1]
dj = [1, 0, -1, 0, 1, -1, -1, 1]

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+2)] * 1 + [[0] * 1 + [0] * N + [0] * 1 for _ in range(N)] + [[0]*(N+2)] * 1
    arr[N//2][N//2] = arr[N//2+1][N//2+1] = 2
    arr[N//2+1][N//2] = arr[N//2][N//2+1] = 1

    for _ in range(M):             # 알을 둘 때마다
        j, i, w_b = map(int, input().split())  # j: 행, i : 열, w_b : 흑백여부

        arr[i][j] = w_b          # 알 놓은 곳에 흑백 여부 표기
        for a in range(8):       # 상하좌우와 대각선 4방향으로 델타 탐색
            length = 1           # 델타탐색 진행한 길이
            while True:
                if arr[i + length * di[a]][j + length * dj[a]] + w_b == 3:
                    length += 1
                elif arr[i + length * di[a]][j + length * dj[a]] == w_b and length > 1:
                    for l in range(1, length):
                        arr[i + l * di[a]][j + l * dj[a]] = w_b
                    break
                elif arr[i + length * di[a]][j + length * dj[a]] + w_b != 0:
                    break
    cnt = [0, 0]
    for a in range(1, 1+N):
        for b in range(1, 1+N):
            cnt[arr[a][b]-1] += 1
print('#{} {} {}'.format(t, cnt[0], cnt[1]))