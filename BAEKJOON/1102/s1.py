import sys

si = sys.stdin.readline

N = int(si().strip())

matrix = [list(map(int, si().strip().split())) for _ in range(N)]

base_mask = int(si().strip().replace('Y', '1').replace('N', '0'), 2)
P = int(si().strip())

min_memo = [[0 for _ in range(1 << N)] for _ in range(N)]

for u in range(N):
    for mask in range(1<<N):
        temp_list = [matrix[i][u] for i in range(N) if mask & (1<<(N-i-1))]
        min_memo[u][mask] = min(temp_list) if temp_list else float('inf')

dp = [float('inf') for _ in range(1 << N)]

dp[base_mask] = 0
answer = float('inf')

if bin(base_mask).count('1') >= P:
    answer = 0

else:
    for mask in range(base_mask, 1 << N):
        for u in range(N):
            v = N-u-1
            if mask & (1 << v):
                continue
            dp[mask | 1 << v] = min(dp[mask | 1 << v], dp[mask] + min_memo[u][mask])
            if bin(mask | 1 << v).count('1') == P:
                answer = min(answer, dp[mask | 1 << v] )

print(answer if answer != float('inf') else -1)