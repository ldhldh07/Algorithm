n, k = map(int,input().split())

coin_list = []
dp = [0] * (k+1)
dp[0] = 1
for _ in range(n):
    coin = int(input())
    for i in range(1, k+1):
        if i >= coin:
            dp[i] += dp[i-coin]
print(dp[k])