N, M = map(int, input().split())
p = [0] * M

for i in range(0, N):
    for j in range(i+1, N):
        print(i, j)
