T = int(input())
ans_list=[]

for _ in range(T):
    N = int(input())
    coin_list = list(map(int, input().split()))
    M = int(input())
    dp = [0 for _ in range(M+1)]
    dp[0] = 1
    for coin in coin_list:
        for i in range(coin, M+1):
            dp[i] = dp[i] + dp[i-coin]
    ans_list.append(dp[M])

print(*ans_list, sep='\n')