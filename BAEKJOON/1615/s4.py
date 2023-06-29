import sys
input = sys.stdin.readline

def update(i, x):
    while i <= max_b:
        tree[i] += x
        i += (i & -i)

def get(i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= (i & -i)
    return res

n, m = map(int, input().split())
points = []
tree = [0] * (n+1)
max_b = 0

for _ in range(m):
    a, b = map(int, input().split())
    points.append((a, b))
    max_b = max(max_b, b)

points.sort()

res = 0
for a, b in points:
    res += get(max_b) - get(b)
    update(b, 1)

print(res)
