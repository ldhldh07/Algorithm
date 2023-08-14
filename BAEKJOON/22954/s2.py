import sys

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]

def dfs(start, adjs):
    stack = [start]
    nodes = set()
    edges = set()

    while stack:
        node = stack.pop()
        nodes.add(node)
        for neighbor, edge in adjs[node]:
            if neighbor not in nodes:
                stack.append(neighbor)
                edges.add(edge)
    return nodes, edges

si = sys.stdin.readline

N, M = map(int, si().strip().split())
disjoint_set = DisjointSet(N)
adj_list = [[] for _ in range(N)]
indgree = [0 for _ in range(N)]

for i in range(M):
    u, v = map(int, si().strip().split())
    disjoint_set.union(u-1, v-1)
    adj_list[u-1].append((v-1, i+1))
    adj_list[v-1].append((u-1, i+1))
    indgree[u-1] += 1
    indgree[v-1] += 1

unique_parents = set([disjoint_set.find(i) for i in range(N)])
parent_count = len(unique_parents)

if parent_count == 1:
    if all(degree == 2 for degree in indgree):
        print(-1)
    else:
        leaf_nodes = [i for i, degree in enumerate(indgree) if degree == 1]
        for leaf in leaf_nodes:
            nodes, edges = dfs(leaf, adj_list)
            if len(nodes) < N:
                remaining_nodes = set(range(N)) - nodes
                remaining_edges = set(range(1, M+1)) - edges
                print(len(nodes), N-len(nodes))
                print(*sorted(nodes), sep=" ")
                print(*sorted(edges), sep=" ")
                print(*sorted(remaining_nodes), sep=" ")
                print(*sorted(remaining_edges), sep=" ")
                break
else:
    if parent_count > 2:
        print(-1)
    else:
        for parent in unique_parents:
            nodes, edges = dfs(parent, adj_list)
            print(len(nodes))
            print(*sorted(nodes), sep=" ")
            print(*sorted(edges), sep=" ")

