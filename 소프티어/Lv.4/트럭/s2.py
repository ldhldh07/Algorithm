import sys, heapq
from collections import defaultdict
from bisect import bisect_left, bisect_right

si = sys.stdin.readline

N = int(si().strip())
customers = []
max_car_size = 0
offer_map = defaultdict(int)
for _ in range(N):
    A, *query = map(int, si().strip().split())
    offers = []
    for i in range(A):
        heapq.heappush(offers,(query[2*i], query[2*i+1]))
    prev_size, prev_offer = 0, 0
    while offers:
        car_size, offer = heapq.heappop(offers)
        if prev_offer < offer:
            offer_map[car_size] += offer - prev_offer
        prev_size, prev_offer = car_size, offer

offers = sorted(offer_map.items())
result = []
culcumative_count = 0
for size, offer_count in offers:
    culcumative_count += offer_count
    result.append((culcumative_count, size))

M = int(si().strip())
Q_list = list(map(int, si().strip().split()))

for q in Q_list:
    if q > result[-1][0]:
        print(-1, end=" ")
    else:
        print(result[bisect_right(result, (q, ))][1], end=" ")