class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0 for _ in range(n+1)]


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


N, M = int(input()), int(input())

disjoint_set = DisjointSet(N)
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            disjoint_set.union(i+1, j+1)
plan_list = list(map(int, input().split()))

first_root = disjoint_set.find(plan_list[0])
answer = 'YES'

for i in range(1, M):
    if disjoint_set.find(plan_list[i]) != first_root:
        answer = 'NO'
        break

print(answer)