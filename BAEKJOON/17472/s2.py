
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

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

def kruskal(adjs, n):
    adjs.sorted(key = lambda item:item[2])
    disjoint_set = DisjointSet(n)
    total_distance = 0
    count = 0

    for u, v, distance in adjs:
        if disjoint_set.find(u) == disjoint_set.find(v):
            continue
        disjoint_set.union(u, v)
        total_distance += distance
        count += 1

        if count == n-1:
            break
    return total_distance