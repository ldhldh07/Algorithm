import heapq

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_x] += 1


N, M = map(int, input().split())
bridges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    heapq.heappush(bridges, (-C, A, B))
F1, F2 = map(int, input().split())

disjoint_set = DisjointSet(N)

for _ in range(M):
    minus_c, a, b = heapq.heappop(bridges)
    disjoint_set.union(a-1, b-1)
    if disjoint_set.find(F1-1) == disjoint_set.find(F2-1):
        answer = -minus_c
        break

print(answer)
