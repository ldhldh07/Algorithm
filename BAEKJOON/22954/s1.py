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


N, M = map(int, input().split())

adj_list = [tuple(map(int, input().split()))for _ in range(M)]

disjoint_set = DisjointSet(N)
for u, v in adj_list:
    disjoint_set.union(u-1, v-1)

print(disjoint_set.parent)
print(disjoint_set.rank)
