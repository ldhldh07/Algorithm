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

def kruskal(n, adj_list):
    adj_list.sort(key=lambda adj : adj[2])
    disjoint_set = DisjointSet(n)
    sum_distance = 0
    count = 0

    for start_node, end_node, distance in adj_list:
        if disjoint_set.find(start_node) != disjoint_set.find(end_node):
            disjoint_set.union(start_node, end_node)
            sum_distance += distance
            count += 1
        
        if count == n-1:
            break
    
    return sum_distance

def distance_node(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2) ** 0.5


n = int(input())
stars = []
adjs = []

for index in range(n):
    x, y = map(float, input().split())
    for prev_index, (prev_x, prev_y) in enumerate(stars):
        distance = distance_node(x, y, prev_x, prev_y)
        adjs.append((index, prev_index, distance))
    stars.append((x, y))

print(kruskal(n, adjs))