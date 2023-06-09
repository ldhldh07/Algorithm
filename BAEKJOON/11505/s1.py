class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.tree = [0 for _ in range(4 * len(array))]
        self.build(0, len(array)-1, 1)


    def build(self, start, end, node):
        if start == end:
            self.tree[node] = self.array[start]
        else:
            mid = (start + end) // 2
            self.build(start, mid, node * 2)
            self.build(mid + 1, end, node * 2 + 1)
            self.tree[node] = (self.tree[node * 2] * self.tree[node * 2 + 1]) % 1000000007


    def update(self, start, end, node, index, diff):
        if start > index or end < index:
            return
        self.tree[node] = (self.tree[node] *  diff) % 1000000007
        if start != end:
            mid = (start + end) // 2
            self.update(start, mid, node * 2, index, diff)
            self.update(mid+1, end, node * 2 + 1, index, diff)

    def update_from_zero(self, start, end, node, index, value):
        if start > index or end < index:
            return
        if start == end:
            self.tree[node] = value
            return
        mid = (start + end) // 2
        self.update_from_zero(start, mid, node * 2, index, value)
        self.update_from_zero(mid+1, end, node * 2 + 1, index, value)
        self.tree[node] = (self.tree[node * 2] * self.tree[node * 2 + 1]) % 1000000007

    
    def update_value(self, index, value):
        if not self.array[index]:
            self.array[index] = value
            self.update_from_zero(0, len(self.array)-1, 1, index, value)
        else:
            diff = (value / self.array[index])
            self.array[index] = value
            self.update(0, len(self.array)-1, 1, index, diff)
            


    def query(self, start, end, node, left, right):
        if left > end or right < start:
            return 1
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        left_multiply = self.query(start, mid, node * 2, left, right)
        right_multiply = self.query(mid + 1, end, node * 2 + 1, left, right)
        return (left_multiply * right_multiply) % 1000000007


    def get_multiply(self, left, right):
        return self.query(0, len(self.array)-1, 1, left, right)
    

N, M, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))

segment_tree = SegmentTree(arr)
ans_list=[]
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        segment_tree.update_value(b-1, c)
    elif a == 2:
        ans_list.append(segment_tree.get_multiply(b-1, c-1) % 1000000007)

print(*ans_list, sep='\n')