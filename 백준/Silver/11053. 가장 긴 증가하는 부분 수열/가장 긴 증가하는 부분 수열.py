N = int(input())
A_list = list(map(int, input().split()))
ans = 0
dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if A_list[i] > A_list[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))