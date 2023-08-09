import sys, bisect

si = sys.stdin.readline

N = int(si().strip())

stones = list(map(int, si().strip().split()))

lis = [stones[0]]

for i in range(1, N):
    stone = stones[i]
    if stone > lis[-1]:
        lis.append(stone)
    else:
        lis[bisect.bisect_left(lis, stone)] = stone

print(len(lis))