N = int(input())
arr = [0] * (N+2)
for i in range(1, N+1):
    arr[i] = int(input()) 


dp = [0] * (N+2)
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]

for n in range(3, N+1):
    dp[n] = max(dp[n-3]+arr[n-1], dp[n-2]) + arr[n]

print(dp[N])