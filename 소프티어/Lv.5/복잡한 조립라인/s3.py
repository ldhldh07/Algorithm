K, N = map(int, input().split())

lines = []
jump_time = [0 for _ in range(K-1)]

for line_index in range(K):
    times = list(map(int, input().split()))
    if line_index != K-1:
        jump_time[line_index] = times.pop()
    lines.append(times)

dp = [[0 for _ in range(N)] for _ in range(K)]

# 첫번째 작업장의 작업 시간 초기화
for i in range(K):
    dp[i][0] = lines[i][0]

for i in range(1, K):
    for j in range(1, N):
        dp[i][j] = min(dp[i-1][j] + jump_time[i-1], dp[i][j-1]) + lines[i][j]
print(min(dp[-1]))
