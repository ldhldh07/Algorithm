import sys

si = sys.stdin.readline

N = int(si().strip())
costs = [list(map(int, si().strip())) for _ in range(N)]

dp = [[11 for _ in range(N)] for _ in range(1<<N)]

dp[1][0] = 0
max_ans = 1

for mask in range(1 << N):
    for u in range(N):
        if not mask & (1 << u):
            continue
        for v in range(N):
            if not mask & (1<<v) or u == v:
                continue
            if costs[v][u] >= dp[mask ^ (1 << u)][v]:
                max_ans = max(max_ans, bin(mask).count('1'))
                dp[mask][u] = min(dp[mask][u], costs[v][u])

print(max_ans)