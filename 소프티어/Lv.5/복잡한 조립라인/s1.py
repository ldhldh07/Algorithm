K, N = map(int, input().split())

lines = []
jump_time = [0 for _ in range(N-1)]

for line_index in range(N):
    times = list(map(int, input().split()))
    if line_index != N-1:
        jump_time[line_index] = times.pop()
    lines.append(times)

dp = [float('inf') for _ in range(K)]

dp = lines[0].copy()

for i in range(1, N):
    min_prefix = [float('inf')] + [0 for _ in range(K-1)]
    min_surfix = [0 for _ in range(K-1)] + [float('inf')]

    for prefix_i in range(1, K):
        min_prefix[prefix_i] = min(min_prefix[prefix_i-1], dp[prefix_i-1])

    for suffix_i in range(K-2, -1, -1):
        min_surfix[suffix_i] = min(min_surfix[suffix_i+1], dp[suffix_i+1])
    
    for j in range(K):
        dp[j] = min(dp[j], min(min_prefix[j], min_surfix[j]) + jump_time[i-1]) + lines[i][j]
print(min(dp))