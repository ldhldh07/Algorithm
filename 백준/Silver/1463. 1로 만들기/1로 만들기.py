N = int(input())

dp = [0, 0]
for a in range(2, N + 1):
    if a % 6 == 0:
        dp.append(min(dp[a // 2], dp[a // 3], dp[a - 1])+1)
    elif a % 3 == 0:
        dp.append(min(dp[a // 3], dp[a - 1])+1)
    elif a % 2 == 0:
        dp.append(min(dp[a // 2], dp[a - 1])+1)
    else:
        dp.append(dp[a-1]+1)
print(dp.pop())