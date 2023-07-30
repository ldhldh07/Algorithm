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

        if x_root == y_root:
            return
        
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1


def kruskal(n, adj_list):
    adj_list.sort(key=lambda adj:adj[2])
    sum_cost = 0
    disjoint_set = DisjointSet(n)
    count = 0

    for start_node, end_node, distance in adj_list:
        if disjoint_set.find(start_node) != disjoint_set.find(end_node):
            disjoint_set.union(start_node, end_node)
            sum_cost += distance
            count += 1

        if count == n-1:
            break
    
    return sum_cost


N = int(input())
planets = [tuple(map(int, input().split()))+(index,) for index in range(N)]

adjs = []

for criteria in range(3):
    planets.sort(key=lambda planet:planet[criteria])
    for i in range(1, N):
        adjs.append((planets[i-1][3], planets[i][3], abs(planets[i-1][criteria] - planets[i][criteria])))

print(kruskal(N, adjs))