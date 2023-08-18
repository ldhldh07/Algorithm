from pprint import pprint

N, M = map(int, input().split())


farm = [[0] * N for _ in range(N)]

for _ in range(M):
    X, Y, L, F = map(int, input().split())
    for i in range(X, X + L):
        for j in range(Y, Y + L):
            farm[i][j] = F
pprint(farm)
max_fruit = max([max(row) for row in farm])
prefix_sums = [[[0] * N for _ in range(N)] for _ in range(max_fruit + 1)]
for f in range(1, max_fruit + 1):
    for i in range(N):
        for j in range(N):
            # print(f, i, j)
            # print((farm[i][j] == f))
            # print((prefix_sums[f][i-1][j] if i > 0 else 0))
            # print((prefix_sums[f][i][j-1] if j > 0 else 0))
            # print(prefix_sums[f][i-1][j-1] if i > 0 and j > 0 else 0)
            prefix_sums[f][i][j] = (farm[i][j] == f) + (prefix_sums[f][i-1][j] if i > 0 else 0) + (prefix_sums[f][i][j-1] if j > 0 else 0) - (prefix_sums[f][i-1][j-1] if i > 0 and j > 0 else 0)

# 3. Helper function to get sum for a fruit type in a square
def get_sum(f, x1, y1, x2, y2):
    return prefix_sums[f][x2][y2] - (prefix_sums[f][x1-1][y2] if x1 > 0 else 0) - (prefix_sums[f][x2][y1-1] if y1 > 0 else 0) + (prefix_sums[f][x1-1][y1-1] if x1 > 0 and y1 > 0 else 0)
pprint(prefix_sums)
# 4. Find the largest valid square
max_area = 0
for i in range(N):
    for j in range(N):
        for k in range(i, N):
            for l in range(j, N):
                if k - i == l - j:  # Only consider squares
                    fruits = [get_sum(f, i, j, k, l) for f in range(1, max_fruit + 1)]
                    unique_fruits = sum([1 for f in fruits if f > 0])
                    if unique_fruits <= 2 and get_sum(0, i, j, k, l) == 0:
                        max_area = max(max_area, (k - i + 1) * (l - j + 1))

print(max_area)
