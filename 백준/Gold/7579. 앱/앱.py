N, M = map(int, input().split())

memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [float('inf') for _ in range(M + 1)]
dp[0] = 0

for n in range(N):
    for m in range(M, -1, -1):
        if m >= memories[n]:
            dp[m] = min(dp[m], dp[m-memories[n]]+costs[n])
        else:
            dp[m] = min(dp[m], costs[n])

print(dp[M])