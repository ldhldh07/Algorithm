import bisect

N, H = map(int, input().split())

blocks = [0] * H

for _ in range(N//2):
    base = int(input())
    top = int(input())
    for index in range(H):
        if index < base:
            blocks[index] += 1
        if index >= H - top:
            blocks[index] += 1

blocks.sort()

min_crush = blocks[0]
min_crush_count = bisect.bisect_right(blocks, min_crush)

print(min_crush, min_crush_count)