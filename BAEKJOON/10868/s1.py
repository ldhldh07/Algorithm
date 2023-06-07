class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.tree = [0] * (4 * len(array))
        self.build(0, len(array)-1, 1)

    def build(self, start, end, node):
        if start == end:
            self.tree[node] = self.array[start]
        else:
            mid = (start + end) // 2
            self.build(start, mid, node * 2)
            self.build(mid+1, end, node * 2+1)
            self.tree[node] = min(self.tree[node*2], self.tree[node*2+1])
    
    def query(self, start, end, node, left, right):
        if left > end or right < start:
            return 10 ** 9
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        return min(self.query(start, mid, 2 * node, left, right), self.query(mid+1, end, 2*node +1, left, right))

    def range_min(self, left, right):
        return self.query(0, len(self.array)-1, 1, left, right)


N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
segment_tree = SegmentTree(arr)
ans = []
for _ in range(M):
    a, b = map(int, input().split())
    ans.append(segment_tree.range_min(a-1, b-1))

print(*ans, sep='\n')