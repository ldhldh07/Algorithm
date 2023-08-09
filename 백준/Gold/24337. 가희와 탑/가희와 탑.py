N, a, b = map(int, input().split())

if a + b > N + 1:
    print(-1)
    exit()

max_height = max(a, b)

heights = [1 for _ in range(N)]

current_index = N
for building_i in range(b-1):
    current_index -= 1
    heights[current_index] = building_i + 1

if a == 1:
    heights[0] = max_height
else:
    current_index -= 1
    heights[current_index] = max_height

for building_j in range(a-1):
    current_index -= 1
    heights[current_index] = a - building_j - 1

print(" ".join(map(str, heights)))