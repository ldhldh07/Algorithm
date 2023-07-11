class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            else:
                self.parent[y_root] = x_root
                if self.rank[x_root] == self.rank[y_root]:
                    self.rank[x_root] += 1



n, m = map(int, input().split())
disjoint_set = DisjointSet(n)
ans = 0
for i in range(1, m+1):
    a, b = map(int, input().split())
    if ans:
        continue
    if disjoint_set.find(a) == disjoint_set.find(b):
        ans = i
    else:
        disjoint_set.union(a, b)

print(ans)