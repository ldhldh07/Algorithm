class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.tree = [0] * (len(array) * 4)
        self.build(0, len(array)-1, 1)

    def build(self, start, end, node):
        if start == end:
            self.tree[node] = self.array[start]
        else:
            mid = (start + end) // 2
            self.build(start, mid, node * 2)
            self.build(mid+1, end, node * 2 + 1)
            self.tree[node] = self.tree[2*node] + self.tree[node * 2 + 1]

    def query(self, start, end, node, left, right):
        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.query(start, mid, 2 * node, left, right)
        right_sum = self.query(mid+1, end, 2 * node+1, left, right)
        return left_sum + right_sum
    
    def get_sum(self, left, right):
        return self.query(0, len(self.array) -1, 1, left, right)
    
    def update(self, start, end, node, index, diff):
        if index < start or index > end:
            return
        self.tree[node] += diff
        if start != end:
            mid = (start + end) // 2
            self.update(start, mid, node * 2, index, diff)
            self.update(mid + 1, end, node * 2 + 1, index, diff)

    def update_value(self, index, value):
        diff = value - self.array[index]
        self.array[index] = value
        self.update(0, len(self.array)-1, 1, index, diff)

N, M, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))

segment_tree = SegmentTree(arr)

for _ in range(M+K):
    a, b, c = map(int, input().split())

    if a == 1:
        segment_tree.update_value(b-1, c)
    elif a == 2:
        print(segment_tree.get_sum(b-1, c-1))