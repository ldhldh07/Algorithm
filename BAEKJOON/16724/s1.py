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

arr = [list(input()) for _ in range(N)]
disjoint_set = DisjointSet(N * M)
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'D':
            disjoint_set.union(M*i + j, M*(i+1) + j)
        elif arr[i][j] == 'U':
            disjoint_set.union(M*i + j, M*(i-1) + j)
        elif arr[i][j] == 'L':
            disjoint_set.union(M*i + j, M*i + j - 1)
        elif arr[i][j] == 'R':
            disjoint_set.union(M*i + j, M*i + j + 1)

print(len(set(disjoint_set.find(x) for x in range(N * M))))