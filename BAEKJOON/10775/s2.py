class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0 for _ in range(size+1)]

    def update(self, idx, diff):
        while idx <= self.size:
            self.tree[idx] += diff
            idx += (idx & -idx)

    def sum(self, idx):
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= (idx & -idx)
        return result
    
G, P = int(input()), int(input())

fenwick_tree = FenwickTree(G)
flag = True
for i in range(1, P+1):
    g = int(input())
    if flag:
        fenwick_tree.update(g, 1)
        if fenwick_tree.sum(g) > g:
            ans = i-1
            flag = False

print(ans)