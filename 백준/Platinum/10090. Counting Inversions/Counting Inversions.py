class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0 for _ in range(size + 1)]

    def update(self, index, diff):
        while index <= self.size:
            self.tree[index] += diff
            index += (index & -index)

    def sum(self, index):
        currunt_sum = 0
        while index > 0:
            currunt_sum += self.tree[index]
            index -= (index & -index)
        return currunt_sum


n = int(input())
num_list = list(map(int, input().split()))

fenwick_tree = FenwickTree(n)
ans = 0

for num in num_list:
    ans += fenwick_tree.sum(n) - fenwick_tree.sum(num)
    fenwick_tree.update(num, 1)

print(ans)