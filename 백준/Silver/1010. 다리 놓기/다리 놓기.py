N = int(input())
for _ in range(N):
    N, M = map(int, input().split())
    dp = [1, 1]
    for n in range(M+1):
        if n > 1:
            dp.append(dp[n-1] * n)
    print(dp[M] //  (dp[M-N] * dp[N]))
