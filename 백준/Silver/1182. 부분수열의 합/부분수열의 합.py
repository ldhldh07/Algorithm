N, S = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(1 << N):
    sum_li = 0
    len_li = 0
    for j in range(N):
        if i & (1 << j):
            len_li += 1
            sum_li += arr[j]
    if sum_li == S and len_li != 0:
        ans += 1
print(ans)
