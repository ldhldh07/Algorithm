import sys

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0 for _ in range(size+1)]
    
    def update(self, idx, diff):
        while idx <= self.size:
            self.tree[idx] += diff
            idx += (idx & -idx)
    
    def sum(self, idx):
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= (idx & -idx)
        return s

n, m = map(int, sys.stdin.readline().split())
points = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    points.append((a, b))

points.sort()

tree = FenwickTree(n)
res = 0

for a, b in points:
    res += tree.sum(n) - tree.sum(b)
    tree.update(b, 1)

print(res)