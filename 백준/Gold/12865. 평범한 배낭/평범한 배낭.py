N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for n in range(1, N+1):
    for k in range(1, K+1):
        dp[n][k] = max(dp[n-1][k], dp[n-1][k-items[n-1][0]] + items[n-1][1]) if k >= items[n-1][0] else dp[n-1][k]

print(dp[N][K])