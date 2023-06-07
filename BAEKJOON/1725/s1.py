import sys
sys.setrecursionlimit(10**5)

class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.tree = [0] * (4 * len(array))
        self.build(0, len(array)-1, 1)

    def build(self, start, end, node):
        if start == end:
            self.tree[node] = start
        else:
            mid = (start + end) // 2
            left = self.build(start, mid, node * 2)
            right = self.build(mid + 1, end, node * 2 + 1)
            self.tree[node] = left if self.array[left] <= self.array[right] else right
        return self.tree[node]

    def query(self, start, end, node, left, right):
        if right < start or end < left:
            return -1
        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_index = self.query(start, mid, node * 2, left, right)
        right_index = self.query(mid + 1, end, node * 2 + 1, left, right)

        if left_index == -1:
            return right_index
        if right_index == -1:
            return left_index
        return left_index if self.array[left_index] <= self.array[right_index] else right_index


    def get_min(self, left, right):
        return self.query(0, len(self.array)-1, 1, left, right)


def find_max(start, end, segment_tree):
    if start > end:
        return 0
    if start == end:
        return heights[start]
    min_index = segment_tree.get_min(start, end)
    max_area = max(
                    find_max(start, min_index-1, segment_tree),
                    (end-start+1) * heights[min_index], 
                    find_max(min_index+1, end, segment_tree)
                )
    return max_area

ans_list = []

N = int(input())
heights = []
for _ in range(N):
    heights.append(int(input()))

segment_tree = SegmentTree(heights)

print(find_max(0, len(heights)-1, segment_tree))