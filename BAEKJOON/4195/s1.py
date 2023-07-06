class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

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
                self.size[y_root] += self.size[x_root]
            else:
                self.parent[y_root] = x_root
                self.size[x_root] += self.size[y_root]
                if self.rank[x_root] == self.rank[y_root]:
                    self.rank[x_root] += 1

T = int(input())
ans_list = []

for _ in range(T):
    F = int(input())

    names = {}
    index = 1
    friendships = []
    
    for _ in range(F):
        a, b = input().split()
        
        if a not in names:
            names[a] = index
            index += 1
        
        if b not in names:
            names[b] = index
            index += 1

        friendships.append((names[a], names[b]))

    disjoint_set = DisjointSet(index)


    for ai, bi in friendships:
        disjoint_set.union(ai, bi)
        ans_list.append(disjoint_set.size[disjoint_set.find(ai)]) 

print(*ans_list, sep='\n')
