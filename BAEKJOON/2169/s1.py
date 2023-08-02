N, M = map(int, input().split())

mars_map = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0] for _ in range(M)] for _ in range(N)]

dp[0][0][0] = mars_map[0][0]
dp[0][0][1] = mars_map[0][0]


for i in range(N):
    if not i:
        for j in range(1, M):
            dp[i][j][0] = dp[i][j-1][0] + mars_map[i][j]
            dp[i][j][1] = dp[i][j-1][1] + mars_map[i][j]
        continue
    for j in range(M):
        dp[i][j][0] = max(dp[i-1][j]) + mars_map[i][j]
        dp[i][M-1-j][1] = max(dp[i-1][M-1-j]) + mars_map[i][M-1-j]
        if j:
            dp[i][j][0] = max(dp[i][j][0], dp[i][j-1][0] + mars_map[i][j])
            dp[i][M-1-j][1] = max(dp[i][M-1-j][1], dp[i][M-1-j+1][1] + mars_map[i][M-1-j])

print(dp[N-1][M-1][0])