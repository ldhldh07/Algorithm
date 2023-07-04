import heapq

N, K = map(int, input().split())
jewel_list = sorted([(weight, -value) for weight, value in [map(int, input().split()) for _ in range(N)]])
bag_list = sorted([int(input()) for _ in range(K)])

total_value = 0
capable_jewel = []

for bag in bag_list:
    while jewel_list and bag >= jewel_list[0][0]:
        weight, value = heapq.heappop(jewel_list)
        heapq.heappush(capable_jewel, value)
    if capable_jewel:
        total_value -= heapq.heappop(capable_jewel)
    elif not jewel_list:
        break

print(total_value)