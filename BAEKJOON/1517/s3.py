class SegmentTree:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (4 * n)

    def update(self, node, start, end, index):
        if index < start or end < index:
            return
        self.tree[node] += 1
        if start != end:
            mid = (start + end) // 2
            self.update(node * 2, start, mid, index)
            self.update(node * 2 + 1, mid + 1, end, index)

    def query(self, node, start, end, left, right):
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(node * 2, start, mid, left, right) + self.query(node * 2 + 1, mid + 1, end, left, right)

N = int(input())
arr = list(map(int, input().split()))

temp = sorted(list(set(arr)))
rank = {temp[i]: i for i in range(len(temp))}

seg_tree = SegmentTree(len(rank))

ans = 0
for i, num in enumerate(arr):
    if i > 0:
        ans += seg_tree.query(1, 0, seg_tree.size - 1, rank[num] + 1, len(rank) - 1)
    seg_tree.update(1, 0, seg_tree.size - 1, rank[num])

print(ans)
