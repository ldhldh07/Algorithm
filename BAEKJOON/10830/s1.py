def procession_multiply(first_procession, second_procession, n):
    multiplied_procession = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            for index in range(n):
                temp += first_procession[i][index] * second_procession[index][j]
            multiplied_procession[i][j] = temp
    return multiplied_procession


def procession_square(procession, n):
    squared_procession = procession_multiply(procession, procession, n)
    return squared_procession


def procession_thousand_divided(procession):
    for i in range(N):
        for j in range(N):
            procession[i][j] %= 1000
    return procession


N, B = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

ans = [[0] * N for _ in range(N)]
for n in range(N):
    ans[n][n] = 1

while B:
    if B % 2:
        ans = procession_multiply(ans, arr, N)
        ans = procession_thousand_divided(ans)
    arr = procession_square(arr, N)
    arr = procession_thousand_divided(arr)
    B = B // 2

for ans in procession_thousand_divided(ans):
    print(*ans)