class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.tree = [0 for _ in range(4 * max(array))]
    
    # def update(self, start, end, node, value):
    #     self.tree = [0 for _ in range(4 * len(array))]
    #     if start == end:
    #         self.tree[node] = 1 if self.array[start] > value else 0
    #     else:
    #         mid = (start + end) // 2
    #         self.build(start, mid, node * 2, value)
    #         self.build(mid+1, end, node * 2 + 1, value)
    #         self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, start, end, node, left, right):
        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        left_max = self.query(start, mid, node * 2, left, right) 
        right_max = self.query(mid + 1, end, node * 2 + 1, left, right)
        return left_max + right_max
    
    def update(self, start, end, node, index):
        if index < start or index > end:
            return
        if start == end:
            self.tree[index] += 1
        mid = (start + end) // 2
        self.update(start, mid, node * 2, index)
        self.update(mid, end, node * 2 + 1, index)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def update_value(self, value):
        self.update(0, len(self.array)-1, 1, value)


arr = [3, 2, 1, 2 , 3]
st = SegmentTree(arr)

print(st.tree)
st.update_value(3)
print(st.tree)