import sys

si = sys.stdin.readline

N = int(si().strip())

cost_matrix = [list(map(int, si().strip().split())) for _ in range(N)]    

answer = float('inf')

for sp in range(N):
    dp = [[float('inf') for _ in range(1<<N)] for _ in range(N)]
    dp[sp][1<<sp] = 0

    for mask in range(1<<N):
        if mask == 1 << sp:
            continue
        for u in range(N):
            if not mask & (1<<u):
                continue
            for v in range(N):
                if not mask & (1<<v) or not cost_matrix[v][u]:
                    continue
            
                dp[u][mask] = min(dp[u][mask], dp[v][mask ^ (1<<u)] + cost_matrix[v][u])

    for ep in range(N):
        if cost_matrix[ep][sp]:
            answer = min(answer, dp[ep][(1<<N)-1] + cost_matrix[ep][sp])

print(answer)