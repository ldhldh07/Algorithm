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


def two_d_to_one_d(x, y, min_x, min_y , max_x, max_y):
    return (y-min_y) * (max_x-min_x+1) + x - min_x 


N = int(input())
min_x = 0
min_y = 0
max_x = 0
max_y = 0
rectangles = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    min_x = min(min_x, x1)
    min_y = min(min_y, y1)
    max_x = max(max_x, x2)
    max_y = max(max_y, y2)
    rectangles.append((x1, y1, x2, y2))

coordinate_row = max_x - min_x + 1
coordinate_column = max_y - min_y + 1

coordinate_n = coordinate_row * coordinate_column
disjoint_set = DisjointSet(coordinate_n)

for x1, y1, x2, y2 in rectangles:
    first_dot = two_d_to_one_d(x1, y1, min_x, min_y, max_x, max_y)
    row_length = x2 - x1
    column_length = y2 - y1
    current_dot = first_dot
    for _ in range(row_length):
        current_dot += 1
        disjoint_set.union(first_dot, current_dot)
    for _ in range(column_length):
        current_dot += coordinate_row
        disjoint_set.union(first_dot, current_dot)
    for _ in range(row_length):
        current_dot -= 1
        disjoint_set.union(first_dot, current_dot)
    for _ in range(column_length):
        current_dot -= coordinate_row
        disjoint_set.union(first_dot, current_dot)

print([disjoint_set.find(point) for point in range(coordinate_n)])