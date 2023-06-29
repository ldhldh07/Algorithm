import sys

class SegmentTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (4*n)

    def update(self, node, start, end, index, diff):
        if index < start or end < index:
            return
        self.tree[node] += diff
        if start != end:
            mid = (start + end) // 2
            self.update(node*2, start, mid, index, diff)
            self.update(node*2+1, mid+1, end, index, diff)

    def query(self, node, start, end, left, right):
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(node*2, start, mid, left, right) + self.query(node*2+1, mid+1, end, left, right)

n, m = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
edges.sort()
seg_tree = SegmentTree(n)
result = 0

for a, b in edges:
    result += seg_tree.query(1, 1, n, b+1, n)
    seg_tree.update(1, 1, n, b, 1)

print(result)