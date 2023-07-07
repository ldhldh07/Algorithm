A, B = map(int, input().split())
ans = 0
for num in range(A, B+1):
    ans += bin(num).count('1')
print(ans)