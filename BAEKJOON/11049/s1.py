N = int(input())

procession_list = []

for _ in range(N):
    r, c = map(int, input().split())
    procession_list.append((r, c))

INF = 2 ** 31
dp = [[INF for _ in range(N)] for _ in range(N)]

for a in range(N):
    dp[a][a] = 0

for length in range(2, N+1):
    for i in range(N - length + 1):
        j = i + length - 1
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + procession_list[i][0] * procession_list[k][1] * procession_list[j][1])

print(dp[0][N-1])
