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
            length = 1
            while True:
                if arr[i + length * di[a]][j + length * dj[a]] + w_b == 3:   # 다른 색깔 돌을 만난면
                    length += 1                                              # length 1증가
                elif arr[i + length * di[a]][j + length * dj[a]] == w_b and length > 1:  # 같은 색깔을 만나면
                    for l in range(1, length):            # i, j에서 length만큼 이동하면서 색 바꿔줌
                        cnt_wb[2 - w_b] -= 1
                        cnt_wb[w_b - 1] += 1
                        arr[i + l * di[a]][j + l * dj[a]] = w_b
                    break
                elif arr[i + length * di[a]][j + length * dj[a]] == 0:   # 벽 혹은 빈공간(0)을 만나면 break해준다
                    break
print('#{} {} {}'.format(t, cnt_wb[0], cnt_wb[1]))