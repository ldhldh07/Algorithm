import sys, pprint

si = sys.stdin.readline

N, M = map(int, si().strip().split())

farm = [[0 for _ in range(N)] for _ in range(N)]
matrix = [[[[] for _ in range(7-max(i, j))] for j in range(N)] for i in range(N)]

pprint.pprint(matrix)
print(matrix[0][1])
for _ in range(M):
    X, Y, L, F = map(int, si().strip().split())
    for x in range(L):
        for y in range(L):
            farm[X+x][Y+y] = F


pprint.pprint(farm)

for i in range(N):
    for j in range(N):
        print('체크하려는 점', i, j)
        max_length = max(i, j) + 1
        print(max_length)
        for l in range(max_length):
            for ci in range(max(0, i-max_length), i+1):
                for cj in range(max(0, j-max_length), i+1):
                    print(ci, cj)
                    # print(l-1)
                    # # pprint.pprint(matrix)
                    # print(matrix[ci][cj])
                    # print(farm[i][j])
                    matrix[ci][cj][l-1].append(farm[i][j])

pprint.pprint(matrix)
    