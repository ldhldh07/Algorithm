from bisect import bisect_left

N, H = map(int, input().split())

base_blocks = []
top_blocks = []

for i in range(N):
    if i % 2 == 0:
        base_blocks.append(int(input()))
    else:
        top_blocks.append(int(input()))

base_blocks.sort()
top_blocks.sort()

min_crush = N
count = 0

for i in range(1, H + 1):
    base_crush = len(base_blocks) - bisect_left(base_blocks, i)
    top_crush = len(top_blocks) - bisect_left(top_blocks, H - i + 1)

    total_crush = base_crush + top_crush

    if total_crush < min_crush:
        min_crush = total_crush
        count = 1
    elif total_crush == min_crush:
        count += 1

print(min_crush, count)