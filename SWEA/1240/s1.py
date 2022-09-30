T = int(input())
shift = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

for t in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    code = ''
    find_1 = False
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                for a in range(55, -1, -1):
                    code += arr[i][j-a]
                    find_1 = True
                break
        if find_1:
            break
    ans1 = 0
    ans2 = 0
    sn = ''
    for i, c in enumerate(code):
        sn += c
        if i % 14 == 13:
            for ii, s in enumerate(shift):
                if sn == s:
                    ans2 += ii
            sn = ''
        elif i % 7 == 6:
            for ii, s in enumerate(shift):
                if sn == s:
                    ans1 += ii
            sn = ''
    if (ans1 * 3 + ans2) % 10:
        print('#{} 0'.format(t))
    else:
        print('#{} {}'.format(t, ans1 + ans2))