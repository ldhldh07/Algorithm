import sys

si = sys.stdin.readline
N, M = map(int, si().strip().split())

farm = [[0 for _ in range(N)] for _ in range(N)]

fruit_set = set()
for _ in range(M):
    X, Y, L, F = map(int, si().strip().split())
    for x in range(L):
        for y in range(L):
            farm[X+x][Y+y] = F
    fruit_set.add(F)

fruit_set = list(fruit_set)
answer = 0

for i in range(len(fruit_set)):
    for j in range(i, len(fruit_set)):
        combo_fruit = set([fruit_set[i], fruit_set[j]])

        dp = [[0 for _ in range(N)] for _ in range(N)]

        for si in range(N):
            for sj in range(N):
                if farm[si][sj] in combo_fruit and farm[si][sj] != 0:
                    dp[si][sj] = min(dp[si-1][sj-1] if si > 0 and sj > 0 else 0, 
                                    dp[si][sj-1] if sj > 0 else 0, 
                                    dp[si-1][sj] if si > 0 else 0) + 1
        max_dp = max(max(row) for row in dp)
        answer = max(answer, max_dp)

print(answer ** 2)
