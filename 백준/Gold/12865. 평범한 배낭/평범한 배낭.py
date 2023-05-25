N, K = map(int, input().split())
items = [[0,0]] + [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for n in range(1, N+1):
    for k in range(1, K+1):
        dp[n][k] = max(dp[n-1][k], dp[n-1][k-items[n][0]] + items[n][1] if  k >= items[n][0] else 0)

print(dp[N][K])