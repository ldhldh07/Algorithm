def find(g):
    if g != parent[g]:
        parent[g] = find(parent[g])
    return parent[g]

G, P = int(input()), int(input())
parent = [i for i in range(G+2)]
count = 0

for _ in range(P):
    g = find(int(input()))
    if g == 0:
        break
    parent[g] = find(g - 1)
    count += 1
print(count)
