from collections import defaultdict

def check_fruit(f, x1, y1, x2, y2):
    square_sum = prefix_sums[f][x2][y2] - (prefix_sums[f][x1-1][y2] if x1 > 0 else 0) - (prefix_sums[f][x2][y1-1] if y1 > 0 else 0) + (prefix_sums[f][x1-1][y1-1] if x1 > 0 and y1 > 0 else 0)
    return (square_sum > 0)

def find_largest_square(N, fruit_set):
    for length in range(N, 0, -1):
        for si in range(N - length + 1):
            for sj in range(N - length + 1):
                ei = si + length - 1
                ej = sj + length - 1
                
                square_fruits = [check_fruit(fruit, si, sj, ei, ej) for fruit in fruit_set]
                fruits_count = sum(square_fruits)
                
                if fruits_count <= 2 and not check_fruit(0, si, sj, ei, ej):
                    return length**2
    return 0

N, M = map(int, input().split())

farm = [[0 for _ in range(N)] for _ in range(N)]
fruit_set = set()

for _ in range(M):
    X, Y, L, F = map(int, input().split())
    for x in range(L):
        for y in range(L):
            farm[X+x][Y+y] = F
    fruit_set.add(F)

prefix_sums = defaultdict(lambda: [[0 for _ in range(N)] for _ in range(N)])

for fruit in fruit_set:
    for i in range(N):
        for j in range(N):
            prefix_sums[fruit][i][j] = (farm[i][j] == fruit) + (prefix_sums[fruit][i-1][j] if i > 0 else 0) + (prefix_sums[fruit][i][j-1] if j > 0 else 0) - (prefix_sums[fruit][i-1][j-1] if i > 0 and j > 0 else 0)

print(find_largest_square(N, fruit_set))
