N, M, L, K = map(int, input().split())

stars = []
for _ in range(K):
    stars.append(tuple(map(int, input().split())))

max_count = 0
for n in range(N-L+1):
    for m in range(M-L+1):
        count = 0
        for x, y in stars:
            if n <= x and x <= n+L and m <= y and y <= m+L:
                count += 1
        max_count = max(max_count, count)

print(K - max_count)