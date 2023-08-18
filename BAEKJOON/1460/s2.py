import sys, pprint

def get_square_count(i, j, length):
    return touch_sum[i][j] - get_contain_count(i-length, N-1) - get_contain_count(N-1, j-length) + get_contain_count(i-length, j-length)

def get_contain_count(x, y):
    return 0 if x < 0 or y < 0 else contain_sum[x][y]


si = sys.stdin.readline

N, M = map(int, si().strip().split())

touch_sum = [[0 for _ in range(N)] for _ in range(N)]
contain_sum = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    X, Y, L, F = map(int, si().strip().split())
    for start_i in range(X, N):
        for start_j in range(Y, N):
            touch_sum[start_i][start_j] += 1
    
    for end_i in range(X+L-1, N):
        for end_j in range(Y+L-1, N):
            contain_sum[end_i][end_j] += 1
            
            

pprint.pprint(touch_sum)
pprint.pprint(contain_sum)

print(get_square_count(3, 6, 2))
print(get_square_count(6, 6, 1))
print(get_square_count(3, 6, 2))
print(get_square_count(6, 2, 1))
print(get_square_count(6, 2, 2))
