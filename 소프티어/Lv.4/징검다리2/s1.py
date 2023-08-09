import sys
from bisect import bisect_left

si = sys.stdin.readline

N = int(si().strip())
stones = list(map(int, si().strip().split()))


lis_list = [0 for _ in range(N)]
lis = [stones[0]]
lis_list[0] = 1


for i in range(1, N):
    stone = stones[i]
    if stone > lis[-1]:
        lis.append(stone)
        lis_list[i] = len(lis)
    else:
        index_of_stone = bisect_left(lis, stone)
        lis[index_of_stone] = stone
        lis_list[i] = index_of_stone + 1

reversed_lis = [stones[-1]]
lis_list[-1] += 1

for i in range(N-2, -1, -1):
    stone = stones[i]
    if stone > reversed_lis[-1]:
        reversed_lis.append(stone)
        lis_list[i] += len(reversed_lis)
    else:
        index_of_stone = bisect_left(reversed_lis, stone)
        reversed_lis[index_of_stone] = stone
        lis_list[i] += index_of_stone + 1
        
print(max(lis_list)-1)