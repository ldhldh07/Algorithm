T = int(input())

for t in range(1, T+1):
    N = int(input())
    
    dp = [0] * (12)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    for i in range(4, N+1):
        dp[i] = dp[i-3] + dp[i-2] +dp[i-1]    
    
    print(dp[N])