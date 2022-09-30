T = int(input())

for t in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:                  # 0,0엔 값 그대로
                dp[i][j] = arr[i][j]
            elif i == 0:                           # 맨 윗줄은 옆에값 그대로 더해야 최솟값
                dp[i][j] = dp[i][j-1] + arr[i][j]
            elif j == 0:                           # 왼쪽줄도 위에값 그대로 더해야 최솟값
                dp[i][j] = dp[i-1][j] + arr[i][j]
            else:                                  # 그 외에는 왼쪽값이랑 위에값중 작은값에서 더한것이 최솟값
                dp[i][j] = (dp[i][j - 1] if dp[i][j - 1] < dp[i - 1][j] else dp[i - 1][j]) + arr[i][j]

    print('#{} {}'.format(t, dp.pop().pop()))