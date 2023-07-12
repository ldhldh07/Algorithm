from collections import defaultdict

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


N, M, K = map(int, input().split())
candy_list = list(map(int, input().split()))

disjoint_set = DisjointSet(N)
for _ in range(M):
    a, b = map(int, input().split())
    disjoint_set.union(a-1, b-1)

root_dict = defaultdict(lambda: [0, 0])
for i in range(N):
    root_i = disjoint_set.find(i)
    root_dict[root_i][0] += 1
    root_dict[root_i][1] += candy_list[i]

dp = [0 for _ in range(K)]

for child, candy in root_dict.values():
    for j in range(K-1, child-1, -1):
        dp[j] = max(dp[j], dp[j-child] + candy)

print(dp[K-1])