import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n):
        self.size = 2 ** (n - 1).bit_length()
        self.tree = [0] * (2 * self.size)

    def update(self, i, x):
        i += self.size
        self.tree[i] = x
        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def query(self, l, r):
        l += self.size
        r += self.size
        res = 0
        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.tree[r]
            l >>= 1
            r >>= 1
        return res

n, m = map(int, input().split())
points = []
for _ in range(m):
    a, b = map(int, input().split())
    points.append((a, b))
points.sort()

seg_tree = SegmentTree(n + 1)
res = 0
for a, b in points:
    res += seg_tree.query(b + 1, n + 1)
    seg_tree.update(b, 1)
print(res)
