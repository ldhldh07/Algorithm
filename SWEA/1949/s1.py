T = int(input())

for t in range(1, 1+T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(arr)