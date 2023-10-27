import sys

si = sys.stdin.readline

H, W = map(int, si().strip().split())

heights = list(map(int, si().strip().split()))
limit_heights = [0 for _ in range(W)]

limit_height = 0

for h_index in range(W):
    limit_height = max(limit_height, heights[h_index])
    limit_heights[h_index] = limit_height

limit_height = 0

for h_index in range(W-1, 0, -1):
    limit_height = max(limit_height, heights[h_index])
    limit_heights[h_index] = min(limit_heights[h_index], limit_height)

print(sum([l - h for l, h in zip(limit_heights, heights)]))