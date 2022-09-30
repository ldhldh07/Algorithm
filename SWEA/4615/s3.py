di = [0, 1, 0, -1, 1, -1, 1, -1]
dj = [1, 0, -1, 0, 1, -1, -1, 1]

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+2)] * 1 + [[0] * 1 + [0] * N + [0] * 1 for _ in range(N)] + [[0]*(N+2)] * 1
    arr[N//2][N//2] = arr[N//2+1][N//2+1] = 2
    arr[N//2+1][N//2] = arr[N//2][N//2+1] = 1
    cnt_wb = [2, 2]                # 흰색돌 갯수, 검은돌 갯수

    for _ in range(M):             # 알을 둘 때마다
        j, i, w_b = map(int, input().split())  # j: 행, i : 열, w_b : 흑백여부

        arr[i][j] = w_b          # 알 놓은 곳에 흑백 여부 표기
        cnt_wb[w_b-1] += 1       # 놓은 알 갯수 하나 증가
        for a in range(8):       # 상하좌우와 대각선 4방향으로 델타 탐색

            stack = [0] * N
            top = -1

            while True:
                i += di[a]
                j += dj[a]
                if arr[i][j] + w_b == 3:   # 다른 색깔 돌을 만난면
                    top += 1
                    stack[top] = (i, j)
                elif arr[i][j] == w_b:
                    while top > -1:
                        cnt_wb[2 - w_b] -= 1
                        cnt_wb[w_b - 1] += 1
                        arr[stack[top][0]][stack[top][1]] = w_b
                        top -= 1
                    break
                elif arr[i][j] + w_b != 0:
                    break
print('#{} {} {}'.format(t, cnt_wb[0], cnt_wb[1]))