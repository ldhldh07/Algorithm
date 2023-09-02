import sys

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

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1


def kruskal(adjs, disjoint_set, count, n):
    adjs.sort(key = lambda adj: adj[2])
    sum_distance = 0

    for u, v, distance in adjs:
        if disjoint_set.find(u) == disjoint_set.find(v):
            continue
        disjoint_set.union(u, v)
        sum_distance += distance
        count += 1

        if count == n-1:
            break

    return sum_distance


def get_distance(x1, y1, x2, y2):
    return (abs(x1-x2) ** 2 + abs(y1-y2) ** 2) ** 0.5


si = sys.stdin.readline

N, M = map(int, si().strip().split())

gods = []
adjs = []

for current_i in range(N):
    X, Y = map(int, si().strip().split())
    for prev_i, (prev_x, prev_y) in enumerate(gods):
        adjs.append((current_i, prev_i, get_distance(prev_x, prev_y, X, Y)))
    gods.append((X, Y))

disjoint_set = DisjointSet(N)
count = 0

for _ in range(M):
    a, b = map(int, si().strip().split())
    if disjoint_set.find(a-1) != disjoint_set.find(b-1):
        disjoint_set.union(a-1, b-1)
        count += 1

answer = kruskal(adjs, disjoint_set, count, N)

print("{:.2f}".format(answer))