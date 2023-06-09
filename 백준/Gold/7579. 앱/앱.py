N, M = map(int, input().split())

memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [0] + [10 ** 9 for _ in range(M)]

for n in range(N):
    for m in range(M, -1, -1):
        dp[m] = min(dp[m], (dp[m-memories[n]] if m >= memories[n] else 0) + costs[n])

print(dp[M])