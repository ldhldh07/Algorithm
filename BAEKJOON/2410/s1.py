N = int(input())

dp = [0] * (N+1)
dp[1] = 1

for n in range(2, N+1):
    a = 0
    while n > 2**a:
        a += 1
    if n % 2:
        dp[n] = dp[n-1]
    else:
        dp[n] = dp[n-1] + dp[n//2] 
print(dp[N] % 1000000000)