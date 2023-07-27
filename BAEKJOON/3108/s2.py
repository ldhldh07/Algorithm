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


def inside_rectangle(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    return ax1 > bx1 and ax2 < bx2 and ay1 > by1 and ay2 < by2

def overlap_rectangle(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    overlap = not (ax1 > bx2 or ax2 < bx1 or ay1 > by2 or ay2 < by1)
    inside = inside_rectangle(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) or inside_rectangle(bx1, by1, bx2, by2, ax1, ay1, ax2, ay2)
    return overlap and not inside


N = int(input())
rectangles = [(0,0,0,0)]

disjoint_set = DisjointSet(N+1)
for i in range(1, N+1):
    x1, y1, x2, y2 = map(int, input().split())
    for prev_i, (prev_x1, prev_y1, prev_x2, prev_y2) in enumerate(rectangles):
        if overlap_rectangle(x1, y1, x2, y2, prev_x1, prev_y1, prev_x2, prev_y2):
            disjoint_set.union(i, prev_i)
    rectangles.append((x1, y1, x2, y2))

group_list = set(disjoint_set.find(point) for point in range(N+1))
print(len(group_list)-1)
