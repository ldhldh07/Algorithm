from collections import deque

N = int(input())

home = [[1] + list(map(int, input().split())) + [1] for _ in range(N)]
home = [[1] * (N + 2)] + home + [[1] * (N + 2)]
# 우, 우하, 하로 들어오는 dp
dp = [[[0, 0, 0] for _ in range(N + 2)] for _ in range(N + 2)]
dp[1][2][0] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == 1 and j <= 2:
            continue
        if not home[i][j]:
            # 오른쪽으로 들어오려면 왼쪽칸에서 오른쪽으로 들어왔을때, 대각선으로 들어왔을 때
            if not home[i][j - 1]:
                dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][1]
            # 대각선으로 들어오려면 좌상에 왔던 모든 경우 가능
            if not home[i - 1][j] and not home[i][j - 1]:
                dp[i][j][1] += (
                    dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]
                )
            # 위에서 들어오려면 대각선으로 오거나 위에서 들어왔던 경우
            if not home[i - 1][j]:
                dp[i][j][2] = dp[i - 1][j][1] + dp[i - 1][j][2]

print(sum(dp[N][N]))
