T = int(input())

for t in range(1, 1+T):
    N = int(input())
    A_B = []

    for _ in range(N):
        start_end = list(map(int, input().split()))
        A_B.append(start_end)

    P = int(input())
    print('#{}'.format(t), end=' ')
    ans_list = []
    for p in range(P):
        C = int(input())
        cnt = 0
        for a in A_B:
            if a[0] <= C <= a[1]:
                cnt += 1
        ans_list.append(str(cnt))
    print(' '.join(ans_list))
