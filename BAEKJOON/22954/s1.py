import sys

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]
        self.indgree = [0 for _ in range(n)]


    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    
    def union(self, x, y):
        adj_list
        x_root = self.find(x)
        y_root = self.find(y)

        self.parent[y_root] = x_root
        self.size[x_root] += self.size[y_root]
        self.indgree[y] += 1
        self.indgree[x] += 1


def dfs(start, adjs):
    stack = [(start, -1)]
    node_list = [start+1]
    vertex_list = []
    prev_node = -1
    while stack:
        current_node, prev_node = stack.pop()

        for next_node, vertex_index in adjs[current_node]:
            if next_node != prev_node:
                node_list.append(next_node+1)
                vertex_list.append(vertex_index+1)
                stack.append((next_node, current_node))
    return node_list, vertex_list



si = sys.stdin.readline

N, M = map(int, si().strip().split())

disjoint_set = DisjointSet(N)

v_list = []
adj_list = [[] for _ in range(N)]

for vi in range(M):
    u, v = map(int, si().strip().split())

    if disjoint_set.find(u-1) != disjoint_set.find(v-1):
        disjoint_set.union(u-1,v-1)
    
        v_list.append((u, v, vi+1))
        adj_list[u-1].append((v-1, vi))
        adj_list[v-1].append((u-1, vi))


parent_list = list(set([disjoint_set.find(i) for i in range(N)]))
parent_count = len(parent_list)

if parent_count == 1:
    if disjoint_set.size[parent_list[0]] == 2:
        print(-1)
        exit()
    else:
        ans_list = []
        for j in range(N):
            if disjoint_set.indgree[j] == 1:
                only_node = j + 1
                break
        for n in range(1, N+1):
            if n != j:
                ans_list.append(n)
        ver_list=[]
        for a, b, i in v_list:
            if a == only_node or b== only_node:
                continue
            ver_list.append(i)
        print(N-1, 1)
        print(*ans_list, sep=" ")
        print(*ver_list, sep=" ")
        print(only_node)
        print()
if parent_count > 2:
    print(-1)
    exit()


if parent_count ==2:
    if disjoint_set.size[parent_list[0]] == disjoint_set.size[parent_list[1]]:
        print(-1)
        exit()
    else:
        print(disjoint_set.size[parent_list[0]], disjoint_set.size[parent_list[1]])
        for parent in parent_list:
            nodes, vertexes = dfs(parent, adj_list)
            print(*nodes, sep=" ")
            print(*vertexes, sep=" ")