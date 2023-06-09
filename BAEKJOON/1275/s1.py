class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.tree = [0 for _ in range(4 * len(self.array))]
        self.build(0, len(array)-1, 1)
    
    def build(self, start, end, node):
        if start == end:
            self.tree[node] = self.array[start]
        else:
            mid = (start + end) // 2
            self.build(start, mid, node * 2)
            self.build(mid + 1, end, node * 2 + 1)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
    
    def update(self, start, end, node, index, diff):
        if index < start or index > end:
            return
        self.tree[node] += diff
        if start != end:
            mid = (start + end) // 2
            self.update(start, mid, node * 2, index, diff)
            self.update(mid+1, end, node * 2 + 1, index, diff)

    def update_value(self, index, value):
        diff = value - self.array[index]
        self.array[index] = value
        self.update(0, len(self.array)-1, 1, index, diff)

    def query(self, start, end, node, left, right):
        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.query(start, mid, node * 2, left, right)
        right_sum = self.query(mid + 1, end, node * 2 + 1, left, right)
        return left_sum + right_sum
    
    def get_sum(self, left, right):
        return self.query(0, len(self.array) - 1, 1, left, right)


N, Q = map(int, input().split())
arr = list(map(int, input().split()))
segment_tree = SegmentTree(arr)

ans_list = []
for _ in range(Q):
    x, y, a, b = map(int, input().split())
    ans_list.append(segment_tree.get_sum(x-1, y-1) if y > x else segment_tree.get_sum(y-1, x-1))
    segment_tree.update_value(a-1, b)

print(*ans_list, sep='\n')