N = int(input())

num_list = list(map(int, input().split()))
ans = 0
for n in num_list:
    nlist = 0
    for m in range(1, n+1):
        if n % m == 0:
            nlist += 1
    if nlist == 2:
        ans += 1

print(ans)