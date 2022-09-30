def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = []
    rep = [i for i in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        edge.append([u, v, w])
    edge.sort(key=lambda x: x[2])

    cnt = 0
    ans = 0
    for u, v, w in edge:
        if find_set(u) != find_set(v):
            cnt += 1
            union(u, v)
            ans += w
        if cnt == V+1:
            break

    print('#{} {}'.format(tc, ans))