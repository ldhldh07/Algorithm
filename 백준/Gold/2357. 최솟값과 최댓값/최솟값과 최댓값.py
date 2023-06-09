class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.min_tree = [0 for _ in range(len(array) * 4)]
        self.max_tree = [0 for _ in range(len(array) * 4)]
        self.build(0, len(array)-1, 1)

    
    def build(self, start, end, node):
        if start == end:
            self.min_tree[node] = self.array[start]
            self.max_tree[node] = self.array[start]
        else:
            mid = (start + end) // 2
            self.build(start, mid, node * 2)
            self.build(mid + 1, end, node * 2 + 1)
            self.min_tree[node] = min(self.min_tree[node * 2], self.min_tree[node * 2 + 1])
            self.max_tree[node] = max(self.max_tree[node * 2], self.max_tree[node * 2 + 1])


    def query_min(self, start, end, node, left, right):
        if left > end or right < start:
            return float('inf')
        if left <= start and right >= end:
            return self.min_tree[node]
        mid = (start + end) // 2
        left_min = self.query_min(start, mid, node * 2, left, right)
        right_min = self.query_min(mid + 1, end, node * 2 + 1, left, right)
        return min(left_min, right_min)
    

    def get_min(self, left, right):
        return self.query_min(0, len(self.array)-1, 1, left, right)
    

    def query_max(self, start, end, node, left, right):
        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return self.max_tree[node]
        mid = (start + end) // 2
        left_max = self.query_max(start, mid, node * 2, left, right)
        right_max = self.query_max(mid+1, end, node * 2 + 1, left, right)
        return max(left_max, right_max)
    

    def get_max(self, left, right):
        return self.query_max(0, len(self.array)-1, 1, left, right)


N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
segment_tree = SegmentTree(arr)

ans_list = []
for _ in range(M):
    a, b = map(int, input().split())
    ans_list.append((segment_tree.get_min(a-1, b-1), segment_tree.get_max(a-1, b-1)))
                    
for ans in ans_list:
    print(*ans)