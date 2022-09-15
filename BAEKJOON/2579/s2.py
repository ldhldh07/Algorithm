N = int(input())
arr = [0] * (N + 1)
for i in range(1, N + 1):
    arr[i] = int(input())

dp = [0]
dp.append(10)
dp.append(30)
for a in range(3, N+1):
    dp.append(max(dp[a-3] + arr[a-1], dp[a-2]) + arr[a])
print(dp.pop())
