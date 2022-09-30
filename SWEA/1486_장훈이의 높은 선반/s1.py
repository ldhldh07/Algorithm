T = int(input())
for t in range(1, 1+T):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    min_sum = 987654321
    for i in range(1 << N):
        part_sum = 0
        for j in range(N):
            if i & (1 << j):
                part_sum += arr[j]
        if B <= part_sum < min_sum:
            min_sum = part_sum
    ans = min_sum - B

    print('#{} {}'.format(t, ans))