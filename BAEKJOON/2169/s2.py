N, M = map(int, input().split())

mars_map = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0] for _ in range(M)] for _ in range(N)]

dp[0][0][0] = mars_map[0][0]
dp[0][0][1] = mars_map[0][0]

for j in range(1, M):
    dp[0][j][0] = dp[0][j-1][0] + mars_map[0][j]
    dp[0][j][1] = dp[0][j-1][1] + mars_map[0][j]

for i in range(1, N):
    dp[i][0][0] = max(dp[i-1][0]) + mars_map[i][0]
    dp[i][M-1][1] = max(dp[i-1][M-1]) + mars_map[i][M-1]
    for j in range(1, M):
        dp[i][j][0] = max(max(dp[i-1][j]), dp[i][j-1][0]) + mars_map[i][j]
        dp[i][M-1-j][1] = max(max(dp[i-1][M-1-j]), dp[i][M-j][1]) + mars_map[i][M-1-j]

print(max(dp[N-1][M-1]))
