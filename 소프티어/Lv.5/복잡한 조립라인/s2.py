K, N = map(int, input().split())

lines = []
jump_time = [0 for _ in range(N-1)]

for line_index in range(N):
    times = list(map(int, input().split()))
    if line_index != N-1:
        jump_time[line_index] = times.pop()
    lines.append(times)
    
dp = [[0 for _ in range(K)] for _ in range(N)]

dp[0] = lines[0].copy()

for i in range(1, N):
    min_of_jump = min(dp[i-1]) + jump_time[i-1]
    for j in range(K):
        dp[i][j] = min(dp[i-1][j], min_of_jump) + lines[i][j]
print(min(dp[N-1]))