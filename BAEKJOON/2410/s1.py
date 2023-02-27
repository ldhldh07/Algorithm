N = int(input())

dp = [0] * (N+1)
dp[1] = 1
dp[2] = 2
for a in range(1, N+1):
