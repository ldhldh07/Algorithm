import bisect

N, H = map(int, input().split())

base_blocks = [0] * (H + 1)
top_blocks = [0] * (H + 1)

for _ in range(N // 2):
    base = int(input())
    top = int(input())
    base_blocks[base] += 1
    top_blocks[top] += 1

for i in range(H - 1, 0, -1):
    base_blocks[i - 1] += base_blocks[i]
    top_blocks[i - 1] += top_blocks[i]

blocks = [0] * H

for i in range(H):
    blocks[i] = base_blocks[i] + top_blocks[H - i]

blocks.sort()

min_crush = blocks[0]
min_crush_count = bisect.bisect_right(blocks, min_crush)

print(min_crush, min_crush_count)